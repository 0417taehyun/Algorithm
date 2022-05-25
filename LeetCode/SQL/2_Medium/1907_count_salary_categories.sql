-- [ LeetCode ] 1907. Count Salary Categories

SELECT
    Categories.category,
    COUNT(account_id) AS accounts_count
FROM (
    SELECT "Low Salary" AS category
    UNION ALL
    SELECT "Average Salary"
    UNION ALL
    SELECT "High Salary"
) AS Categories
LEFT JOIN (
    SELECT
        account_id,
        income,
        CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income > 50000 THEN "High Salary"
            ELSE "Average Salary"
        END AS category
    FROM Accounts
) AS AccountWithCategories
USING (category)
GROUP BY Categories.category;


/*
위에서도 WITH 구를 활용한 공통 테이블 표현식(CTE_Common Table Expression)을 사용할 수 있었음에도 굳이 안 써도 괜찮을 것 같아 쓰지 않았다.
아래 풀이에서 중요한 점은 WITH 구에 대한 부분이라기 보다는 accounts_count 필드를 WITH 구 내부에 생성하는데
Accounts 테이블의 각 행에 대해 CASE 구에 대한 결괏값을 실행하고 그에 대해 accounts_count 필드의 값을 `1`로 준다는 점이다.
이후 이를 UNION ALL 키워드를 통해서 수직 결합하여 이후 category 필드를 기준으로 GROUP BY 구를 실행하고 accounts_count 필드를 SUM 함수로 합산하면 간단하게 문제를 풀 수 있다.

COUNT 함수를 써야하는 경우에 SUM 함수를 사용할 수 있는 방법에 대해서 고민해보면 좋을 것 같다.
매번 고민을 하긴 하는데 이번처럼 아예 `0`과 `1` 등으로 값을 미리 설정하여 하는 것은 조금 신기했다.
*/

WITH cte AS (
    SELECT
        CASE
            WHEN income < 20000 THEN "Low Salary"
            WHEN income > 50000 THEN "High Salary"
            ELSE "Average Salary"
        END category,
        1 AS accounts_count
    FROM accounts
    UNION ALL
    SELECT "Low Salary" AS category, 0 AS accounts_count
    UNION ALL
    SELECT "Average Salary" AS category, 0 AS accounts_count
    UNION ALL
    SELECT "High Salary" AS category, 0 AS accounts_count
)

SELECT
    category,
    SUM(accounts_count) AS accounts_count
FROM cte
GROUP BY category;
