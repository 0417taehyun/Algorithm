-- [ LeetCode ] 569. Median Employee Salary

WITH cte (id, company, salary, salary_rank, mid_rank, flag) AS (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary DESC, id DESC) AS salary_rank,
        ROUND(COUNT(id) OVER(PARTITION BY company) / 2) AS mid_rank,
        MOD(COUNT(id) OVER(PARTITION BY company), 2) AS flag
    FROM Employee
)

SELECT
    id,
    company,
    salary
FROM cte
WHERE (
    (
        flag = FALSE
        AND
        (
            salary_rank = mid_rank
            OR
            salary_rank = mid_rank + 1
        )
    )
    OR
    (
        flag = TRUE
        AND
        salary_rank = mid_rank
    )
);


/*
위와 같이 문제를 풀었는데 아래와 같이 훨씬 간단하게 풀 수 있다.

ROW_NUMBER 윈도우 함수(Window Function)를 사용하여 상향, 하향 두 가지 경우를 나누어 구한다.
그리고 해당 두 결괏값을 뺐을 때 `0` 또는 `1`인 경우가 바로 중간값이 된다.
개수가 홀수인 경우 중간값은 두 차이가 `0`이지만 짝수인 경우 `1`인 경우도 포함이기 때문이다.

이때 유의할 점은 ROW_NUMBER 윈도우 함수의 경우 `1`부터 시작하기 때문에 그 자료형이 UNSIGNED 자료형이다.
따라서 CAST 함수를 사용하여 차이를 구할 수 있게 SIGNED 자료형으로 변환을 해줘야 오류가 발생하지 않는다.
*/

SELECT
    id,
    company,
    salary
FROM (
    SELECT
        id,
        company,
        salary,
        ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary ASC, id ASC) AS bottom_to_top,
        ROW_NUMBER() OVER(PARTITION BY company ORDER BY salary DESC, id DESC) AS top_to_bottom
    FROM Employee
) AS SalaryRank
WHERE ABS(CAST(bottom_to_top AS SIGNED) - CAST(top_to_bottom AS SIGNED)) BETWEEN 0 AND 1;
