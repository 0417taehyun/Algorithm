-- [ LeetCode ] 2238. Number of Times a Driver Was a Passenger

SELECT
    EachDrivers.driver_id,
    COUNT(Rides.ride_id) AS cnt
FROM (
    SELECT DISTINCT driver_id
    FROM Rides
) AS EachDrivers
LEFT JOIN Rides
ON EachDrivers.driver_id = Rides.passenger_id
GROUP BY EachDrivers.driver_id;
