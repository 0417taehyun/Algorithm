-- [ LeetCode ] 1321. Restaurant Growth

/*
처음에 문제를 푸는 방법을 상당히 많이 고민했다.
DENSE_RANK 함수를 사용하여, 다시 말해 윈도우 함수를 사용하여 문제를 해결할 수 있게 고민했었는데 포기하고 다르게 풀었다.

아래 쿼리를 보면 알 수 있듯 중복이 제거된 날짜 값만 얻고 해당 날짜를 기준으로 INNER JOIN 구를 실행한다.
이때 DATEDIFF 함수를 사용해 결합의 조건이 날짜 차이가 되게 하여 해당 날은 물론 최대 6일까지, 다시 말해 7일씩 결합이 되도록 한다.

결합이 된 테이블 쪽의 visited_on 필드 수를 COUNT 함수를 사용하여 셈을 하면 레코드가 시작되는 날짜 기준으로 7일이 아직 안 지난 경우 7을 넘지 못하기 때문에
이를 필터링 해주기 위해 앞서 중복이 제거된 날짜 값 필드인 visited_on 필드를 기준으로 GROUP BY 구를 실행하고 HAVING 구에서 해당 조건을 걸어 필터링한다.

끝으로 이렇게 얻어진 값들을 활용해 SUM 함수를 통해 각 구간별 합과 SUM 및 COUNT 함수를 사용해 각 구간별 평균을 구한다.
이때 COUNT(DISTINCT Customer.visited_on) 표현은 `7`로 대체되어도 좋지만 확장석을 위해 COUNT 함수를 사용하였다.
기준이 되는 날짜가 `7`이 아닌 `14` 등으로 변경되었을 때 SELECT 구에서도 `7`이라는 해당 값을 변경해야 하는 것이 아닌 ON 구의 조건 속 BETWEEN 키워드의 범위와 HAVING 구 부분만 수정하면 되기 때문이다.
*/

SELECT
    UniqueVisitedDate.visited_on AS visited_on,
    SUM(Customer.amount) AS amount,
    ROUND((SUM(Customer.amount) / COUNT(DISTINCT Customer.visited_on)), 2) AS average_amount
FROM (
    SELECT DISTINCT visited_on
    FROM Customer
) AS UniqueVisitedDate
JOIN Customer
ON DATEDIFF(UniqueVisitedDate.visited_on, Customer.visited_on) BETWEEN 0 AND 6
GROUP BY UniqueVisitedDate.visited_on
HAVING COUNT(DISTINCT Customer.visited_on) = 7;


/*
아래와 같이 윈도우 함수(Window Function)를 사용해서 문제를 해결할 수도 있다.

먼저 날짜를 기준으로 행의 순서를 찾아 7일 기준으로 계산을 해야하기 때문에 DENSE_RANK 함수를 사용해준다.
동일한 날짜가 존재할 때 차이가 생기지 않도록 RANK 함수가 아닌 DENSE_RANK 함수를 사용하는 것에 유의해야 한다.

다음으로 SUM 함수를 사용할 때 프레임(Frame) 부분을 설정해준다. RANGE 키워드를 통해 실제로 계산이 이뤄질 구역을 지정하게 되는데,
INTERVAL 6 DAY 표현을 통해 6일의 차이가 존재하는 곳에서 현재 행(`CURRENT ROW` 키워드)까지의 합을 구해 반환한다.
*/

SELECT
    DISTINCT visited_on,
    amount,
    ROUND((amount / 7), 2) AS average_amount
FROM (
    SELECT
        visited_on,
        SUM(amount) OVER(ORDER BY visited_on ASC RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
        DENSE_RANK() OVER(ORDER BY visited_on ASC) AS date_order
    FROM Customer
) AS OrderedVisitedDate
WHERE date_order >= 7;
