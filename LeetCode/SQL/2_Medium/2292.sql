-- [ LeetCode ] 2292. Products With Three or More Orders in Two Consecutive Years

SELECT DISTINCT product_id
FROM (
    SELECT
        product_id,
        YEAR(purchase_date) - ROW_NUMBER() OVER(PARTITION BY product_id ORDER BY YEAR(purchase_date) ASC) AS diff
    FROM Orders
    GROUP BY product_id, YEAR(purchase_date)
    HAVING COUNT(order_id) >= 3
) AS MoreThanThreeOrders
GROUP BY product_id, diff
HAVING COUNT(product_id) >= 2;
