-- [ LeetCode ] 1068. Product Sales Analysis I

SELECT product_name, year, price
FROM Sales
JOIN Product
USING (product_id);
