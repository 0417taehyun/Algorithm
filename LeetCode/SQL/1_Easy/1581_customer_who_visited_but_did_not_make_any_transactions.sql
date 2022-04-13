-- [ LeetCode ] 1581. Customer Who Visited but Did Not Make Any Transactions

/*
SQL에서 COUNT 함수는 NULL 값을 자동으로 제외하고 셈한다는 것을 잊지 말아야겠다.
이러한 이유 때문에 값을 셈하기 위해서 `transaction_id IS NULL`이라는 조건식을 SUM 함수 내에 넣었다.
만약 해당 조건이 참일 경우 `1`을 반환해서 결국 NULL 값을 세는 것과 동일하기 때문이다.

또한 FROM - JOIN - WHERE - GROUP BY - HAVING - SELECT 구 순서로 쿼리가 실행되기 때문에,
transaction_id 필드의 값이 `NULL`인 경우에 대한 조건을 걸기 위해서는 GROUP BY 구의 대상이 customer_id 필드라서
HAVING 구에서 이를 사용하지 못하고 그 전에 WHERE 구에서 사용해야 한다.
*/

SELECT
    customer_id,
    SUM(transaction_id IS NULL) AS count_no_trans
FROM Visits
LEFT JOIN Transactions
USING (visit_id)
WHERE transaction_id IS NULL
GROUP BY customer_id;