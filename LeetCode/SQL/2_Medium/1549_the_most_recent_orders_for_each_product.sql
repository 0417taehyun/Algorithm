-- [ LeetCode ] 1549. The Most Recent Orders for Each Product

SELECT
    Products.product_name,
    Products.product_id,
    OrderDateRank.order_id,
    OrderDateRank.order_date
FROM Products
JOIN (
    SELECT
        order_id,
        order_date,
        product_id,
        DENSE_RANK() OVER(PARTITION BY product_id ORDER BY order_date DESC) AS date_rank
    FROM Orders
) AS OrderDateRank
ON (
    OrderDateRank.date_rank = 1
    AND
    Products.product_id = OrderDateRank.product_id
)
ORDER BY product_name, product_id, order_id;
