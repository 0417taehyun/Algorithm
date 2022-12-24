-- [ LeetCode ] 1468. Calculate Salaries

SELECT
    Salaries.company_id,
    Salaries.employee_id,
    Salaries.employee_name,
    ROUND(Salaries.salary * Taxes.tax) AS salary
FROM Salaries
JOIN (
    SELECT
        company_id,
        CASE
            WHEN MAX(salary) < 1000 THEN (1 - 0)
            WHEN (MAX(salary) >= 1000) AND (MAX(salary) <= 10000) THEN (1 - 0.24)
            ELSE (1 - 0.49)
        END AS tax
    FROM Salaries
    GROUP BY company_id
) AS Taxes
USING (company_id);


/*
위와 같이 문제를 풀 경우 CASE 문에서 조건을 따질 때마다 매번 MAX 함수를 실행하기 때문에 성능이 떨어질 수밖에 없다.
따라서 GROUP BY 구를 활용한 JOIN 구의 서브쿼리 내에서는 MAX 함수를 사용한 max_salary 필드만 구하고 각 범위에 따른 salary 필드에 대한 계산은 원래의 Salaries 테이블에서 하는 게 좋다.

따라서 정답은 아래와 같다.

추가적으로 유의할 사항은 이러한 맥락에서 윈도우 함수(Window Function)를 사용해 서브쿼리 및 JOIN 구를 사용하지 않고 하나의 테이블 내에서만 문제를 풀 경우
결국 MAX 윈도우 함수를 매번 반복해야 하기 때문에 성능이 안 좋다.
*/

SELECT
    Salaries.company_id,
    Salaries.employee_id,
    Salaries.employee_name,
    ROUND(
        CASE
            WHEN max_salary < 1000 THEN salary * (1 - 0)
            WHEN (max_salary >= 1000) AND (max_salary <= 10000) THEN salary * (1 - 0.24)
            ELSE salary * (1 - 0.49)
        END
    ) AS salary
FROM Salaries
JOIN (
    SELECT
        company_id,
        MAX(salary) AS max_salary
    FROM Salaries
    GROUP BY company_id
) AS CompanySalaries
USING (company_id);
