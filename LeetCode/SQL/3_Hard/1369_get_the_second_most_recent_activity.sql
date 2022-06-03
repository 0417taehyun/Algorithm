-- [ LeetCode ] 1369. Get the Second Most Recent Activity

SELECT
    DISTINCT username,
    activity,
    startDate,
    endDate
FROM (
    SELECT
        username,
        activity,
        startDate,
        endDate,
        DENSE_RANK() OVER(PARTITION BY username ORDER BY endDate DESC) AS recent_rank,
        COUNT(username) OVER(PARTITION BY username) AS activity_count
    FROM UserActivity
) AS UserRecentActivity
WHERE (
    (
        activity_count = 1
        AND
        recent_rank = 1
    )
    OR recent_rank = 2
);
