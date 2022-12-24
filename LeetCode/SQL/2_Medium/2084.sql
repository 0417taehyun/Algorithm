-- [ LeetCode ] 2084. Drop Type 1 Orders for Customers With Type 0 Orders

SELECT
    DISTINCT order_id,
    customer_id,
    order_type
FROM (
    SELECT
        Orders.order_id,
        Orders.customer_id,
        CASE SubOrders.order_type
            WHEN 0 THEN NULL
            ELSE Orders.order_type
        END AS order_type
    FROM Orders
    LEFT JOIN Orders AS SubOrders
    ON (
        Orders.customer_id = SubOrders.customer_id
        AND
        Orders.order_type <> SubOrders.order_type
    )
) AS Results
WHERE order_type IS NOT NULL;


SELECT
    order_id,
    customer_id,
    order_type
FROM (
    SELECT
        order_id,
        customer_id,
        order_type,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_type ASC) AS type_rank
    FROM Orders
) AS OrderTypesRank
WHERE type_rank = 1;