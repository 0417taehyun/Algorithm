-- [ LeetCode ] 1587. Bank Account Summary II

SELECT
    name,
    SUM(amount) AS balance
FROM Transactions
JOIN Users
USING (account)
GROUP BY account
HAVING balance > 10000;
