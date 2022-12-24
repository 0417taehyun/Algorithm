-- [ LeetCode ] 2020. Number of Accounts That Did Not Stream

SELECT COUNT(DISTINCT Subscriptions.account_id) AS accounts_count
FROM Subscriptions
LEFT JOIN Streams
ON (
    YEAR(Streams.stream_date) = '2021'
    AND
    Subscriptions.account_id = Streams.account_id
)
WHERE (
    (
        YEAR(Subscriptions.start_date) = '2021'
        OR
        YEAR(Subscriptions.end_date) = '2021'
    )
    AND
    Streams.session_id IS NULL
);


/*
위와 같은 풀이는 실질적으로 잘못된 풀이라 할 수 있다.

우선 틀리지는 않았지만 비효율적인 부분은 Subscription 테이블의 start_date 필드의 값이 무조건적으로 end_date 필드의 값보다 작기 때문에
2021년에 구독한 사용자를 찾는 로직에 대해서는 end_date 필드에 대한 유효성 검사만 진행하면 된다.

다음으로 아래와 같이 Streams 테이블이 주어졌을 때를 고려하지 않아 틀렸다.
아래와 같이 account_id 필드의 값이 `9`인 경우 stream_date 필드의 연도 값이 `2021`인 경우가 존재하는데 `2020`인 경우도 존재하기 때문에 `9`는 제외되어야 한다.

+------------+------------+-------------+
| session_id | account_id | stream_date |
+------------+------------+-------------+
| 14         | 9          | 2020-05-16  |
| 16         | 9          | 2021-10-27  |
| 18         | 11         | 2020-04-29  | 
| 17         | 13         | 2021-08-08  |
| 19         | 4          | 2020-12-31  |
| 13         | 5          | 2021-01-05  |
+------------+------------+-------------+

물론 문제의 정답은 이 부분을 굳이 고려하지 않고 `9` 또한 정답에 포함시켜야 하는데 제대로 따져보면 사실 빠지는 게 맞다.

이러한 부분을 고려하기 위해 NOT IN 문법을 WHERE 구에 사용하는 방법이 있는데 NOT IN 문법의 경우 모든 값을 비교해야 하기 때문에 성능이 별로 좋지 않다.
따라서 NOT IN 문법 보다는 LEFT JOIN 구를 통해 결합되지 않아 NULL 값을 가지는 경우를 따지고 기본 키(Primary Key)를 다루는 게 훨씬 성능이 좋다.
이러한 접근에 따라 아래와 같이 GROUP BY 구 및 HAVING 구에서의 조건에 따른 SUM 함수를 사용했다.

그런데 사실 아래의 경우 또한 Streams 테이블 내에서 stream_date 필드의 값이 기본 키가 아니기 때문에
인덱스 테이블을 사용하지 않아서 NOT IN 문법과 비교했을 때 그렇게까지 많은 차이가 발생할 것 같지는 않다.
결론적으로 모든 값을 비교하기 때문이다.
*/

SELECT COUNT(account_id) AS accounts_count
FROM (
    SELECT Subscriptions.account_id
    FROM Subscriptions
    LEFT JOIN Streams
    USING (account_id)
    WHERE YEAR(end_date) = '2021'
    GROUP BY Subscriptions.account_id
    HAVING SUM(YEAR(Streams.stream_date) = '2021') = 0
) AS MetAccounts;
