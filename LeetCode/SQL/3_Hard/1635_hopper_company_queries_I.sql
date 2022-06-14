-- [ LeetCode ] 1635. Hopper Company Queries I

/*
처음에 WITH RECURSIVE 구 자체에 GROUP BY 구와 함께 LEFT JOIN 구를 사용해서 문제를 해결하려 했는데
Recursive CTE (Common Table Expression) 에서는 집계 함수(Aggregation Function) 또는 윈도우 함수(Window Function)를 사용하지 못한다는 걸 알게 되었다.

이후 단순히 Months 테이블만 WITH RECURSIVE 구를 활용해 임시 테이블로 만들고
해당 테이블에 각각의 ActiverDriversCount 테이블과 AcceptedRidesCount 테이블을 LEFT JOIN 구로 결합하려 했는데
이럴 경우 한번만 작성되고 SUM 또는 COUNT 함수가 작동되어야 하는 게 여러 번 중복되는 레코드로 인해 오작동하게 되어 원하는 값보다 훨씬 큰 값을 얻게 된다.
예를 들어 3월 이전의 ActiverDriversCount 테이블의 수가 6개이면 결국 Months 테이블에 만들어지는 month 필드의 값이 `3`인 행이 6개이기 때문에 AcceptedRides 테이블이 하나씩 결합이 되더라도 6번 반복되게 된다.

이러한 문제를 해결하기 위해서는 서브쿼리를 사용할 수도 있지만 WITH RECURSIVE 구를 사용하는 김에 각각의 LEFT JOIN 구를 나눠 공통 테이블 표현식(CTE)에서 실행했다.
*/

WITH RECURSIVE Months (month) AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 AS month
    FROM Months
    WHERE month BETWEEN 1 AND 11
), ActiveDriversCount (month, active_drivers) AS (
    SELECT
        Months.month,
        SUM(IFNULL(ActiveDriversCount.active_drivers, 0)) AS active_drivers
    FROM Months
    LEFT JOIN (
        SELECT
            IF(YEAR(join_date) = 2020, MONTH(join_date), 1) AS month,
            COUNT(driver_id) AS active_drivers
        FROM Drivers
        WHERE YEAR(join_date) <= 2020
        GROUP BY month
    ) AS ActiveDriversCount
    ON Months.month >= ActiveDriversCount.month
    GROUP BY Months.month
), AcceptedRidesCount (month, active_drivers, accepted_rides) AS (
    SELECT
        ActiveDriversCount.month,
        ActiveDriversCount.active_drivers,
        IFNULL(AcceptedRidesCount.accepted_rides, 0) AS accepted_rides
    FROM ActiveDriversCount
    LEFT JOIN (
        SELECT
            MONTH(Rides.requested_at) AS month,
            COUNT(AcceptedRides.ride_id) AS accepted_rides
        FROM Rides
        JOIN AcceptedRides
        USING (ride_id)
        WHERE YEAR(Rides.requested_at) = 2020
        GROUP BY month
    ) AS AcceptedRidesCount
    USING (month)
)

SELECT
    month,
    active_drivers,
    accepted_rides
FROM AcceptedRidesCount
ORDER BY month ASC;
