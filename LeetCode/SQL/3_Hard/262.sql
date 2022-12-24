-- [ LeetCode ] 262. Trips and Users

SELECT
    Trips.request_at AS Day,
    ROUND(AVG(Trips.status <> 'completed'), 2) AS 'Cancellation Rate'
FROM Trips
JOIN (
    SELECT users_id AS client_id
    FROM Users
    WHERE (
        banned = 'No'
        AND
        role = 'client'
    )
) AS Clients
USING (client_id)
JOIN (
    SELECT users_id AS driver_id
    FROM Users
    WHERE (
        banned = 'No'
        AND
        role = 'driver'
    )
) AS Drivers
USING (driver_id)
WHERE request_at BETWEEN '2013-10-01' AND '2013-10-03'
GROUP BY Trips.request_at;
