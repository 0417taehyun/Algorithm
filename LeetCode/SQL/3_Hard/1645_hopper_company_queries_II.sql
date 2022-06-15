-- [ LeetCode ] 1645. Hopper Company Queries II

/*
앞서 풀었던 [ 1635. Hopper Company Queries I ]과 거의 유사하게 풀 수 있다.

몇 가지 유의해야 할 점은 available_drivers_count 필드 값을 계산할 때 중복된 값을 제거해줘야 한다는 것이고
다른 하나는 해당 나눗셈을 구할 때 만약 분모가 `0` 이거나 `NULL` 값을, 또는 분자가 `NULL` 값일 때 반환되는 값이 결국 `NULL` 이기 때문에 이를  `0` 으로 치환해주기 위한 `IFNULL` 함수가 필요하다는 것이다.

잊지 말아야 할 것은 모든 사칙연산은 NULL 값에 대한 연산 결과를 NULL 값으로 반환한다는 것이다.

추가적으로 어떤 수를 `0`으로 나누는 경우 원래 기본적으로 ERROR_FOR_DIVISION_BY_ZERO 오류를 반환한다.
그러나 MySQL의 경우 SQL 모드에 따라서 해당 오류를 처리하는 방법이 달라진다.

1. ERROR_FOR_DIVISION_BY_ZERO 모드가 꺼져 있을 경우 `NULL` 값을 반환하고 어떠한 문구도 띄워주지 않는다.
2. ERROR_FOR_DIVISION_BY_ZERO 모드가 켜져 있을 경우 `NULL` 값을 반환하며 주의(Warning) 문구를 띄워준다.
3. ERROR_FOR_DIVISON_BY_ZERO 모드와 함께 Strict SQL 모드가 켜져 있을 경우 오류(Error)를 반환하고 연산 자체를 무시한다.
   이때 만약 `IGNORE` 키워드가 삽입 되어 있을 경우 `NULL` 값을 반환하고 주의(Warning) 문구를 띄워준다.

LeetCode의 경우 기본적으로 모든 모드가 꺼져있다.
*/

WITH RECURSIVE Months (month) AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 AS month
    FROM Months
    WHERE month BETWEEN 1 AND 11
), AvailableDrivers (month, available_drivers_count) AS (
    SELECT
        Months.month,
        SUM(available_drivers_count) AS available_drivers_count
    FROM Months
    LEFT JOIN (
        SELECT
            IF(YEAR(join_date) <> 2020, 1, MONTH(join_date)) AS month,
            COUNT(driver_id) AS available_drivers_count
        FROM Drivers
        WHERE YEAR(join_date) <= 2020
        GROUP BY IF(YEAR(join_date) <> 2020, 1, MONTH(join_date))
    ) AS AvailableDriversCount
    ON Months.month >= AvailableDriversCount.month
    GROUP BY Months.month
), AcceptedDrivers (month, working_percentage) AS (
    SELECT
        AvailableDrivers.month,
        ROUND(
            IFNULL(AcceptedDriversCount.available_drivers_count / AvailableDrivers.available_drivers_count, 0) * 100,
            2
        ) AS working_percentage
    FROM AvailableDrivers
    LEFT JOIN (
        SELECT
            MONTH(Rides.requested_at) AS month,
            COUNT(DISTINCT AcceptedRides.driver_id) AS available_drivers_count
        FROM Rides
        JOIN AcceptedRides
        USING (ride_id)
        WHERE YEAR(Rides.requested_at) = 2020
        GROUP BY MONTH(Rides.requested_at)
    ) AS AcceptedDriversCount
    USING (month)
)

SELECT
    month,
    working_percentage
FROM AcceptedDrivers
ORDER BY month ASC;
