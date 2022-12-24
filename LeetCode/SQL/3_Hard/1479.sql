-- [ LeetCode ] 1479. Sales by Day of the Week

-- DAYNAME 함수를 사용하면 아래와 같이 해당 일자의 요일을 알 수 있다.

SELECT
    Items.item_category AS Category,
    SUM(IF(DAYNAME(Orders.order_date) = 'Monday', Orders.quantity, 0)) AS Monday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Tuesday', Orders.quantity, 0)) AS Tuesday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Wednesday', Orders.quantity, 0)) AS Wednesday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Thursday', Orders.quantity, 0)) AS Thursday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Friday', Orders.quantity, 0)) AS Friday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Saturday', Orders.quantity, 0)) AS Saturday,
    SUM(IF(DAYNAME(Orders.order_date) = 'Sunday', Orders.quantity, 0)) AS Sunday
FROM Items
LEFT JOIN Orders
USING (item_id)
GROUP BY Items.item_category
ORDER BY Category ASC;
