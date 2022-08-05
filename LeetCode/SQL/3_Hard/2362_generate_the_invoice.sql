-- [ LeetCode ] 2362. Generate the Invoice

WITH cte (invoice_id, product_id, quantity, price, price_sum) AS (
    SELECT
        invoice_id,
        Purchases.product_id,
        quantity,
        quantity * price AS price,
        SUM(quantity * price) OVER(PARTITION BY invoice_id) AS price_sum
    FROM Purchases
    JOIN Products
    USING (product_id)
)

SELECT
    product_id,
    quantity,
    price
FROM cte
WHERE invoice_id = (
    SELECT invoice_id
    FROM cte
    ORDER BY price_sum DESC, invoice_id ASC
    LIMIT 1
);
