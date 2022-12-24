-- [ LeetCode ] 182. Duplicate Emails

SELECT email AS Email
FROM Person
GROUP BY email
HAVING COUNT(email) >= 2;