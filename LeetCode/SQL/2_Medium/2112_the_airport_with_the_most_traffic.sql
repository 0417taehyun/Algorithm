-- [ LeetCode ] 2112. The Airport With the Most Traffic

WITH cte (airport_id, flights_count) AS (
    SELECT
        departure_airport AS airtport_id,
        flights_count
    FROM Flights
    UNION ALL
    SELECT
        arrival_airport AS airport_id,
        flights_count
    FROM Flights
)

SELECT airport_id
FROM (
    SELECT
        airport_id,
        DENSE_RANK() OVER(ORDER BY SUM(flights_count) DESC) AS flights_count_rank
    FROM cte
    GROUP BY airport_id
) AS AirportsRank
WHERE flights_count_rank = 1;
