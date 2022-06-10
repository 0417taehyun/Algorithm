-- [ LeetCode ] 1127. User Purchase Platform

SELECT
    DateSpendings.spend_date,
    DateSpendings.platform,
    IFNULL(TotalReports.total_amount, 0) AS total_amount,
    IFNULL(TotalReports.total_users, 0) AS total_users
FROM (
    SELECT
        DISTINCT Spending.spend_date,
        Platforms.platform
    FROM Spending
    CROSS JOIN (
        SELECT 'mobile' AS platform
        UNION ALL
        SELECT 'desktop'
        UNION ALL
        SELECT 'both'
    ) AS Platforms
) AS DateSpendings
LEFT JOIN (
    SELECT
        spend_date,
        platform,
        SUM(amount) AS total_amount,
        COUNT(user_id) AS total_users
    FROM (
        SELECT
            user_id,
            spend_date,
            IF(COUNT(platform) = 2, 'both', platform) AS platform,
            SUM(amount) AS amount
        FROM Spending
        GROUP BY user_id, spend_date
    ) AS UserReports
    GROUP BY spend_date, platform
) AS TotalReports
USING (spend_date, platform);
