-- [ LeetCode ] 2324. Product Sales Analysis IV

SELECT user_id, product_id
FROM (
    SELECT
        Sales.user_id,
        Sales.product_id,
        RANK() OVER(PARTITION BY Sales.user_id ORDER BY SUM(Product.price * Sales.quantity) DESC) AS spent_rank
    FROM Sales
    JOIN Product
    USING (product_id)
    GROUP BY Sales.user_id, Sales.product_id
) AS SalesRankings
WHERE spent_rank = 1;
