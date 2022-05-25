-- [ LeetCode ] 1843. Suspicious Bank Accounts

/*
먼저 처음에 단순히 '2019-06'과 같이 연도와 월까지만 존재하는 시간에 대해 DATE_SUB 함수 등을 사용하려고 했는데 반환 값이 전부 'NULL'이었다.
왜냐하면 DATE 관련 함수를 사용한다는 것 자체가 온전히 연도, 월, 그리고 일 이상의 값들이 나열되어 있는 형태라는 의미이기 때문이다.

그래서 이러한 문제를 해결하고자 Transactions 테이블 day 필드에 MONTH 함수를 사용하여 diff 필드 값을 계산해서 문제를 풀었다.
제출 자체는 정상적으로 전부 통과했지만 문제는 아래 레코드 예시와 같이 값이 주어지면 예외 상황이 발생한다는 것이다.

+----------------+------------+----------+--------+---------------------+
| transaction_id | account_id | type     | amount | day                 |
+----------------+------------+----------+--------+---------------------+
| 4              | 4          | Creditor | 59300  | 2019-04-20 12:39:18 |
| 1              | 4          | Creditor | 49300  | 2021-05-03 16:11:04 |
+----------------+------------+----------+--------+---------------------+

연도 자체는 2년의 차이가 있기 때문에 연속된 월이라 할 수 없는데 MONTH 함수를 사용하여 월만 사용했을 때는 연속된 월이 된다.
이러한 문제를 해결하기 위해 결국 연도까지를 함께 고려해야 했다.

그래서 연도와 월까지만 존재하는 transaction_date 필드에 아래 정답과 같이 CONCAT 함수를 사용해 `01` 문자열을 붙여 매월 첫 날이 되게 만들고
그 결괏값을 ROW_NUMBER 윈도우 함수(Window Function)를 사용해 구한 행 번호를 DATE_SUB 함수를 활용해서 월만 뺐다.

이렇게 되면 결국 연도는 동일하게 남고 월이 행 번호에 따라 차감되기 때문에 정상적으로 GROUP BY 구를 활용해서 이전 문제가 되었던 예외 케이스까지 커버할 수 있다.
*/

SELECT DISTINCT account_id
FROM (
    SELECT
        Accounts.account_id,
        DATE_SUB(
            CONCAT(transaction_date, "-01"),
            INTERVAL ROW_NUMBER() OVER(PARTITION BY account_id ORDER BY transaction_date ASC) MONTH
        ) AS diff
    FROM Accounts
    JOIN (
        SELECT
            account_id,
            DATE_FORMAT(day, '%Y-%m') AS transaction_date,
            SUM(IF(type = 'Creditor', amount, 0)) AS total_income
        FROM Transactions
        GROUP BY account_id, transaction_date
    ) AS GroupedTransactions
    ON (
        Accounts.account_id = GroupedTransactions.account_id
        AND
        Accounts.max_income < GroupedTransactions.total_income
    )
) AS GroupedAccounts
GROUP BY account_id, diff
HAVING COUNT(account_id) >= 2
ORDER BY account_id;
