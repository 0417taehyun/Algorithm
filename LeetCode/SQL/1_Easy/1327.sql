-- [ LeetCode ] 1327. List the Products Ordered in a Period

SELECT
    product_name,
    unit
FROM Products
JOIN (
    SELECT
        product_id,
        SUM(unit) AS unit
    FROM Orders
    WHERE YEAR(order_date) = 2020 AND MONTH(order_date) = 2
    GROUP BY product_id
    HAVING SUM(unit) >= 100
) AS Counted_Orders
USING (product_id)
ORDER BY unit DESC, product_name ASC;