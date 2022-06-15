-- [ LeetCode ] 1651. Hopper Company Queries III

WITH RECURSIVE Months (month) AS (
    SELECT 1 AS month
    UNION ALL
    SELECT month + 1 AS month
    FROM Months
    WHERE month BETWEEN 1 AND 11
), MonthlyRides (month, monthly_distance, monthly_duration) AS (
    SELECT
        MONTH(Rides.requested_at) AS month,
        SUM(Acceptedrides.ride_distance) AS monthly_distance,
        SUM(Acceptedrides.ride_duration) AS monthly_duration
    FROM Rides
    JOIN AcceptedRides
    USING (ride_id)
    WHERE YEAR(Rides.requested_at) = 2020
    GROUP BY month
), MonthlyTotal (month, monthly_distance, monthly_duration) AS (
    SELECT
        Months.month,
        IFNULL(MonthlyRides.monthly_distance, 0) AS monthly_distance,
        IFNULL(MonthlyRides.monthly_duration, 0) AS monthly_duration
    FROM Months
    LEFT JOIN MonthlyRides
    USING (month)
), ThreeMonthlyAverage (month, average_ride_distance, average_ride_duration) AS (
    SELECT
        JanuaryToOctober.month,
        ROUND(AVG(MonthlyTotal.monthly_distance), 2) AS average_ride_distance,
        ROUND(AVG(MonthlyTotal.monthly_duration), 2) AS average_ride_duration
    FROM (
        SELECT month
        FROM Months
        WHERE month BETWEEN 1 AND 10
    ) AS JanuaryToOctober
    JOIN MonthlyTotal
    ON (MonthlyTotal.month - JanuaryToOctober.month) BETWEEN 0 AND 2
    GROUP BY JanuaryToOctober.month
)


SELECT
    month,
    average_ride_distance,
    average_ride_duration
FROM ThreeMonthlyAverage
ORDER BY month ASC;
