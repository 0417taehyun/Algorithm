-- [ LeetCode ] 1355. Activity Participants

/*
아래와 같이 문제를 풀었는데 두 가지 질문을 생각해봤다.

1. Friends 테이블에서 동일한 name 필드의 값을 가졌는데 id 필드의 값이 다른 경우 혹은 똑같은 사람이 동일한 activity 필드에 대해 또다시 참여하여 id 필드의 값만 다른 경우의 발생 여부
2. 단 하나의 최대 및 최소값이 존재하는지 아니면 동일한 값을 가진 최대 및 최소값이 여러 개 존재할 수 있는지

1번의 문제를 해결하기 위해서는 COUNT 함수의 대상이 달라진다.
만약 중복되는 사람을 제거해야 하는 경우, 다시 말해 한 명이 동일한 activity 필드에 대해 여러 번 참여하는 게 테이블에 레코드로 저장되어 이 중복을 없애줘야 하는 경우 DISTINCT 키워드를 name 필드에 걸어줘서 COUNT 함수를 사용할 수 있다.
반대로 중복되는 사람을 제거하지 않아도 되는 경우, 단순히 셈을 하기만 하면 되는 경우 id 필드의 값을 COUNT 함수의 대상으로 사용하면 된다.

동일한 최대 및 최소값이 존재하는 경우를 따져주기 위해 NOT IN 키워드를 사용하지 않고 숫자의 셈을 활용했다.
그래서 아래 쿼리에서는 DENSE_RANK 윈도우 함수(Window Function)를, 다른 풀이에서는 서브쿼리 내에서 COUNT 함수를 사용하며 문제를 푼 것이다.
더욱이 NOT IN 조건을 사용할 경우 인덱스 여부와 상관없이 해당 구간을 전부 비교해야 하기 때문에 별로 효율이 좋지 않다.

추가적으로 조금 의문이었던 두 가지가 있는데
먼저 JOIN 구를 사용하지 않더라도 문제를 해결할 수는 있다는 것과
두 번째로 언제 WITH 구를 활용하여 CTE(Common Table Expression)을 사용하면 좋은지에 대한 부분이었다.

특히 CTE 관련해서는 조금 천천히 알아봐야겠다.
*/

SELECT name AS activity
FROM (
    SELECT
        name,
        DENSE_RANK() OVER(ORDER BY cnt DESC) AS highest_rnk,
        DENSE_RANK() OVER(ORDER BY cnt ASC) AS lowest_rnk
    FROM (
        SELECT
            Activities.name AS name,
            COUNT(Friends.id) AS cnt
        FROM Activities
        JOIN Friends
        ON Activities.name = Friends.activity
        GROUP BY Activities.name
    ) AS GroupedActivities
) AS ActivitiesRank
WHERE (
    highest_rnk <> 1
    AND
    lowest_rnk <> 1
);


/*
아래와 같이 조금 더 간단하게 HAVING 구에 서브쿼리를 사용해서 문제를 해결할 수 있다.
서브쿼리에서 반복되는 부분인 ORDER BY 구 전까지는 WITH 구를 사용하여 정의해둬도 좋을 것 같다.
*/

SELECT activity
FROM Friends
GROUP BY activity
HAVING (
    COUNT(id) > (SELECT COUNT(id) AS cnt FROM Friends GROUP BY activity ORDER BY cnt ASC LIMIT 1)
    AND
    COUNT(id) < (SELECT COUNT(id) AS cnt FROM Friends GROUP BY activity ORDER BY cnt DESC LIMIT 1)
);
