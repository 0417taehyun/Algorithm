-- [ LeetCode ] 2153. The Number of Passengers in Each Bus II

WITH RECURSIVE cte1 (row_num, bus_id, capacity, current_passengers_count) AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY Periods.arrival_time ASC) AS row_num,
        bus_id,
        capacity,
        COUNT(Passengers.passenger_id) AS current_passengers_count
    FROM (
        SELECT
            bus_id,
            LAG(arrival_time, 1, -1) OVER(ORDER BY arrival_time ASC) AS previous_time,
            arrival_time,
            capacity
        FROM Buses
    ) AS Periods
    LEFT JOIN Passengers
    ON (
        Periods.previous_time < Passengers.arrival_time
        AND
        Periods.arrival_time >= Passengers.arrival_time
    )
    GROUP BY Periods.bus_id
), cte2 (row_num, bus_id, diff, passengers_cnt) AS (
    SELECT
        row_num,
        bus_id,
        IF(capacity < current_passengers_count, current_passengers_count - capacity, 0) AS diff,
        IF(capacity < current_passengers_count, capacity, current_passengers_count) AS passengers_cnt
    FROM cte1
    WHERE row_num = 1
    UNION ALL
    SELECT
        cte1.row_num,
        cte1.bus_id,
        IF(cte1.capacity < cte1.current_passengers_count + cte2.diff, cte1.current_passengers_count + cte2.diff - cte1.capacity, 0) AS diff,
        IF(cte1.capacity < cte1.current_passengers_count + cte2.diff, cte1.capacity, cte1.current_passengers_count + cte2.diff) AS passengers_cnt
    FROM cte1
    JOIN cte2
    ON cte1.row_num = cte2.row_num + 1
)

SELECT
    bus_id,
    passengers_cnt
FROM cte2
ORDER BY bus_id ASC;
