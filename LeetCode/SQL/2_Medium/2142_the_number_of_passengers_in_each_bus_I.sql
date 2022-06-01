-- [ LeetCode ] 2142. The Number of Passengers in Each Bus I

SELECT
    BusTimeTables.bus_id,
    COUNT(Passengers.passenger_id) AS passengers_cnt
FROM (
    SELECT
        bus_id,
        LAG(arrival_time, 1, -1) OVER(ORDER BY arrival_time ASC) AS previous_bus_time,
        arrival_time
    FROM Buses
) AS BusTimeTables
LEFT JOIN Passengers
ON Passengers.arrival_time BETWEEN previous_bus_time + 1 AND BusTimeTables.arrival_time
GROUP BY BusTimeTables.bus_id
ORDER BY bus_id ASC;
