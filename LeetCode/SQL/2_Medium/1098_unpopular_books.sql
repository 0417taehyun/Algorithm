-- [ LeetCode ] 1098. Unpopular Books

SELECT
    Books.book_id AS book_id,
    Books.name AS name
FROM Books
LEFT JOIN Orders
USING (book_id)
WHERE available_from  < DATE_SUB("2019-06-23", INTERVAL 1 MONTH)
GROUP BY book_id
HAVING SUM(IF(DATEDIFF("2019-06-23", dispatch_date) <= 365, quantity, 0)) < 10;