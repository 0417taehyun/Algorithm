-- 2688. Find Active Users

WITH cte (user_id, created_at, row_num) AS (
    SELECT
        user_id,
        created_at,
        ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY created_at ASC) AS row_num
    FROM Users
)

SELECT DISTINCT PreviousPurchase.user_id AS user_id
FROM cte AS PreviousPurchase
JOIN cte AS SecondPurchase
ON (
    PreviousPurchase.user_id = SecondPurchase.user_id
    AND
    PreviousPurchase.row_num + 1 = SecondPurchase.row_num
    AND
    DATEDIFF(SecondPurchase.created_at, PreviousPurchase.created_at) BETWEEN 0 AND 7
);

