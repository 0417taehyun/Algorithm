-- [ LeetCode ] 1821. Find Customers With Positive Revenue this Year

SELECT customer_id
FROM Customers
WHERE year = '2021' AND revenue > 0;
