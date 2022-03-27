-- [ LeetCode ] 1069. Product Sales Analysis II

SELECT
    product_id,
    SUM(quantity) AS total_quantity
FROM Sales
JOIN Product
USING (product_id)
GROUP BY product_id;