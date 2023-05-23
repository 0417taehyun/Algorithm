-- 2686. Immediate Food Delivery III

SELECT
    order_date,
    ROUND(AVG(IF(order_date = customer_pref_delivery_date, 1, 0)) * 100, 2) AS immediate_percentage
FROM Delivery
GROUP BY order_date
ORDER BY order_date ASC;
