-- [ LeetCode ] 1174. Immediate Food Delivery II

SELECT ROUND(COUNT(FirstOrders.customer_id) / COUNT(DISTINCT Delivery.customer_id) * 100, 2) AS immediate_percentage
FROM Delivery
LEFT JOIN (
    SELECT
        customer_id,
        MIN(order_date) AS first_order_date
    From Delivery
    GROUP BY customer_id
) AS FirstOrders
ON (
    Delivery.customer_id = FirstOrders.customer_id
    AND
    Delivery.order_date = FirstOrders.first_order_date
    AND
    Delivery.customer_pref_delivery_date = FirstOrders.first_order_date
);


-- 굳이 복잡하게 접근할 필요 없이 아래와 같이 훨씬 간단하게 풀이할 수 있다.

SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT
        customer_id,
        MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);