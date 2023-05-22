-- [ LeetCode ] 2687. Bikes Last Time Used

SELECT
    bike_number,
    MAX(end_time) AS end_time
FROM Bikes
GROUP BY bike_number
ORDER BY end_time DESC;
