-- [ LeetCode ] 2720. Popularity Percentage

WITH Relationship (user1, friend) AS (
    SELECT
        user1 AS user1,
        user2 AS friend
    FROM Friends
    UNION
    SELECT
        user2 AS user1,
        user1 AS friend
    FROM Friends
)

SELECT
    user1,
    ROUND(COUNT(friend) / (SELECT COUNT(DISTINCT user1) FROM Relationship) * 100, 2) AS percentage_popularity
FROM Relationship
GROUP BY user1
ORDER BY user1 ASC;
