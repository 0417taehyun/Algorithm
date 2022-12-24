-- [ LeetCode ] 607. Sales Person

SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT sales_id
    FROM Orders
    JOIN Company
    USING (com_id)
    WHERE Company.name = "RED"
);
