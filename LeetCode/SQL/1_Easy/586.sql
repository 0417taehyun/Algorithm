-- [ LeetCode ] 586. Customer Placing the Largest Number of Orders

-- ORDER BY 구의 기본값은 오름차순으로 ASC이다.

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY COUNT(customer_number) DESC
LIMIT 1;
