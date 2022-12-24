-- [ LeetCode ] 1613. Find the Missing IDs

WITH RECURSIVE AllIDs (customer_id) AS (
    SELECT 1
    UNION ALL
    SELECT customer_id + 1
    FROM AllIDs
    WHERE customer_id BETWEEN 1 AND ((SELECT MAX(customer_id) FROM Customers) - 1)
)

SELECT customer_id AS ids
FROM AllIDs
LEFT JOIN Customers
USING (customer_id)
WHERE Customers.customer_id IS NULL
ORDER BY ids ASC;
