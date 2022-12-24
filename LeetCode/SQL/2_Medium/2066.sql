-- [ LeetCode ] 2066. Account Balance

SELECT
    account_id,
    day,
    SUM(IF(type = 'Deposit', amount, -amount)) OVER(PARTITION BY account_id ORDER BY day ASC) AS balance
FROM Transactions
ORDER BY account_id ASC, day ASC;
