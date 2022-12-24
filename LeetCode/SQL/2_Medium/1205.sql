-- [ LeetCode ] 1205. Monthly Transactions II

/*
Transactions 테이블에는 존재하지 않는데 Chargebacks 테이블에 존재하는 월에 대한 값도 결과로 반환해줘야 한다.
이 부분을 고려하다가 결국 문제를 해결하지 못했는데 처음에는 WITH 구와 함께 UNION 키워드를 활용해서 월에 대한 값만 따로 뺀 다음 이에 대해 JOIN 구를 활용해 문제를 해결하려 했다.

예를 들어 WITH 구를 다음과 같이 작성할 수 있다.

WITH cte (month) AS (
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month
    FROM Transactions
    UNION
    SELECT DATE_FORMAT(trans_date, '%Y-%m') AS month
    FROM Chargebacks
)

결론적으로 JOIN 구를 활용하는 부분에서 잘 해결되지 않아 포기했다. 다른 사람의 풀이를 보니 단순히 UNION 키워드를 활용해 문제를 해결했다.
평소 UNION 키워드를 잘 사용하지 않아서 언제 사용해야 할 지 몰랐던 것이 문제를 해결하지 못한 이유 같았다.

JOIN 구의 경우 수평 결합을, UNION 키워드의 경우 수직 결합을 행한다는 것을 잊지 말아야겠다.
어떤 한 테이블에는 존재하는데 다른 테이블에 값이 존재하지 않을 경우, 그리고 그런 값 또한 수직적으로 표현해야 하는 경우 UNION 키워드를 사용하는 방법을 생각해보자.

아래와 같이 문제를 해결할 때 유의할 점은 같은 country 및 month 필드 값을 같더라도 trans_id 필드의 값이 다르면 다른 경우이기 때문에
걀과적으로 횟수를 세고 amount 필드의 총 합산을 구할 때 개별적으로 필요한 레코드들이다. 따라서 이를 위해, 다시 말해 중복을 없애지 않기 위해 UNION 키워드가 아닌 UNION ALL 키워드를 사용한다.
*/

SELECT
    month,
    country,
    SUM(state='approved') AS approved_count,
    SUM(IF(state='approved', amount, 0)) AS approved_amount,
    SUM(state='chargeback') AS chargeback_count,
    SUM(IF(state='chargeback', amount, 0)) AS chargeback_amount
FROM (
    SELECT
        DATE_FORMAT(Chargebacks.trans_date, '%Y-%m') AS month,
        Transactions.country AS country,
        Transactions.amount AS amount,
        'chargeback' AS state
    FROM Chargebacks
    LEFT JOIN Transactions
    ON Chargebacks.trans_id = Transactions.id
    UNION ALL
    SELECT
        DATE_FORMAT(trans_date, '%Y-%m') AS month,
        country,
        amount,
        'approved' AS state
    FROM Transactions
    WHERE state='approved'
) AS AllTransactions
GROUP BY month, country;
