-- [ LeetCode ] 1454. Active Users

/*
이전에 ROW_NUMBER 윈도우 함수(Window Function)를 활용해서 연속되는 수와의 차이가 동일한 경우를 그룹핑해 풀었던 기억이 나 이를 적용해보려다 조금 복잡하게 풀었다.
아래와 같은 풀이 이전에 시도하려다 실패한 경우가 있었는데 SUM 윈도우 함수를 사용하여 DATEDIFF 함수를 활용해 얻어낸 결괏값의 차이가 `1`인 경우 그대로 더하고 아니면 더하지 않게 한 것이었다.
이를 통해 연속된 날짜 수를 구할 수 있을 것이라 생각했는데 결국 SUM 윈도우 함수가 누적(Cumulative)이기 때문에 연속되지 않고 끊어지고 난 뒤에도 이전의 연속되어 합산된 수가 이어지게 되서 문제를 해결하지 못한다.
한 가지 추가적으로 알게된 건 COUNT 함수를 윈도우 함수로 사용할 때는 내부에 DISTINCT 키워드를 사용할 수 없다는 것이다.
*/

SELECT
    DISTINCT id,
    name
FROM Accounts
JOIN (
    SELECT
        id,
        DATE_SUB(login_date, INTERVAL ROW_NUMBER() OVER(PARTITION BY id ORDER BY login_date ASC) DAY) AS diff
    FROM (
        SELECT
            DISTINCT login_date,
            id
        FROM Logins
    ) AS DistinctLoginDate
) AS LoginDateDifference
USING (id)
GROUP BY Accounts.id, LoginDateDifference.diff
HAVING COUNT(LoginDateDifference.id) >= 5
ORDER BY id;


/*
아래와 같이 훨씬 간단하게 JOIN 구를 사용하여 문제를 해결할 수 있다.
JOIN 구에 BETWEEN 키워드를 활용해 구간을 설정할 수 있다는 걸 잊지 말아야겠다.
*/

SELECT
    DISTINCT Accounts.id,
    Accounts.name
FROM Accounts
JOIN Logins
USING (id)
JOIN Logins AS ConsecutiveDays
ON (
    Accounts.id = ConsecutiveDays.id
    AND
    DATEDIFF(Logins.login_date, ConsecutiveDays.login_date) BETWEEN 0 AND 4
)
GROUP BY Accounts.id, Logins.login_date
HAVING COUNT(DISTINCT ConsecutiveDays.login_date) >= 5
ORDER BY id ASC;
