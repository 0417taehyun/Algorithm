-- [ LeetCode ] 2329. Product Sales Analysis V

SELECT
    Sales.user_id,
    SUM(Sales.quantity * Product.price) AS spending
FROM Sales
JOIN Product
USING (product_id)
GROUP BY Sales.user_id
ORDER BY spending DESC, user_id ASC;
