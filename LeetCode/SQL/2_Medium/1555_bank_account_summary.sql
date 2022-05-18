-- [ LeetCode ] 1555. Bank Account Summary

/*
처음에 아래와 같이 문제를 풀었는데 SUM 함수 부분을 재사용해야 하는 게 마음에 걸렸다.
더욱이 LEFT JOIN 구의 조건을 따질 때 OR 키워드를 활용해 필드의 값을 읽어 비교하는 게 그렇게 효율적이지는 않을 것 같았다.
*/

SELECT
    Users.user_id,
    Users.user_name,
    Users.credit + SUM(
        CASE user_id
            WHEN paid_by THEN -amount
            WHEN paid_to THEN amount
            ELSE 0
        END
    ) AS credit,
    IF(Users.credit + SUM(
        CASE user_id
            WHEN paid_by THEN -amount
            WHEN paid_to THEN amount
            ELSE 0
        END
    ) > 0, 'No', 'Yes') AS credit_limit_breached
FROM Users
LEFT JOIN Transactions
ON (
    Users.user_id = Transactions.paid_by
    OR
    Users.user_id = Transactions.paid_to
)
GROUP BY Users.user_id;


/*
아래 처럼 서브쿼리를 활용하여 SUM 함수에 대한 부분을 미리 계산해서 재사용할 수 있다.
이렇게 할 경우 위 정답보다는 조금 더 최적화가 되었다고 볼 수 있다.
*/

SELECT
    user_id,
    user_name,
    credit,
    IF(credit > 0, 'No', 'Yes') AS credit_limit_breached
FROM (
    SELECT
        Users.user_id,
        Users.user_name,
        Users.credit + SUM(
            CASE user_id
                WHEN paid_by THEN -amount
                WHEN paid_to THEN amount
                ELSE 0
            END
        ) AS credit
    FROM Users
    LEFT JOIN Transactions
    ON (
        Users.user_id = Transactions.paid_by
        OR
        Users.user_id = Transactions.paid_to
    )
    GROUP BY Users.user_id
) AS TransactionResults;


/*
아래와 같이 JOIN 구를 나누어 사용해서 최적화가 가능하다.
SUM 함수 내부에서 조건을 판단하는 것보다 한번에 합산을 하는 게 훨씬 효율이 더 좋기 때문이다.
이를 위해 기존에 OR 키워드를 통해 LEFT JOIN 구를 한번 사용하지 않고 LEFT JOIN 구를 두번 나누어 사용한다.
LEFT JOIN 구의 대상이 되는 테이블의 갯수가 많다면 해당 방법이 오히려 비효율적일 수 있으나 두번 정도만 하면 되고, 더욱이 LEFT JOIN 구의 대상이 되는 테이블의 레코드 수는 이때 성능 비교 측면에서는 무관하다.
*/

SELECT
    Users.user_id,
    Users.user_name,
    (Users.credit - IFNULL(MinusTransactions.withdrawal, 0) + IFNULL(PlusTransactions.deposit, 0)) AS credit,
    IF((Users.credit - IFNULL(MinusTransactions.withdrawal, 0) + IFNULL(PlusTransactions.deposit, 0)) > 0, 'No', 'Yes') AS credit_limit_breached
FROM Users
LEFT JOIN (
    SELECT
        paid_by AS user_id,
        SUM(amount) AS withdrawal
    FROM Transactions
    GROUP BY paid_by
) MinusTransactions
USING (user_id)
LEFT JOIN (
    SELECT
        paid_to AS user_id,
        SUM(amount) AS deposit
    FROM Transactions
    GROUP BY paid_to
) AS PlusTransactions
USING (user_id)
GROUP BY Users.user_id;