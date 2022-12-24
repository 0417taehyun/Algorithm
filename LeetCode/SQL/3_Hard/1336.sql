-- [ LeetCode ] 1336. Number of Transactions per Visit

-- COUNT 함수는 `0` 또한 셈한다는 걸 잊지 말자. NULL 값만 무시해서 결과로 `0`을 반환할 수 있다.

WITH RECURSIVE cte1 (user_id, transactions_count) AS (
    SELECT
        Visits.user_id,
        IFNULL(COUNT(Transactions.user_id), 0) AS transactions_count
    FROM Visits
    LEFT JOIN Transactions
    ON (
        Visits.user_id = Transactions.user_id
        AND
        Visits.visit_date = Transactions.transaction_date
    )
    GROUP BY Visits.user_id, Visits.visit_date
), cte2 (transactions_count) AS (
    SELECT 0 AS transactions_count
    UNION ALL
    SELECT transactions_count + 1
    FROM cte2
    WHERE transactions_count BETWEEN 0 AND (SELECT MAX(transactions_count) FROM cte1) - 1
)

SELECT
    cte2.transactions_count,
    IFNULL(COUNT(cte1.user_id), 0) AS visits_count
FROM cte2
LEFT JOIN cte1
USING (transactions_count)
GROUP BY cte2.transactions_count
ORDER BY transactions_count ASC;
