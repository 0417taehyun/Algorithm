-- [ LeetCode ] 1831. Maximum Transaction Each Day

SELECT transaction_id
FROM (
    SELECT
        transaction_id,
        DENSE_RANK() OVER(PARTITION BY DATE(day) ORDER BY amount DESC) AS amount_rank
    FROM Transactions
) AS TransactionAmountRank
WHERE amount_rank = 1
ORDER BY transaction_id ASC;
