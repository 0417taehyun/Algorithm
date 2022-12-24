-- [ LeetCode ] 2372. Calculate the Influence of Each Salesperson

SELECT
    Salesperson.salesperson_id,
    Salesperson.name,
    IFNULL(SUM(Sales.price), 0) AS total
FROM Salesperson
LEFT JOIN Customer
USING (salesperson_id)
LEFT JOIN Sales
USING (customer_id)
GROUP BY Salesperson.salesperson_id;
