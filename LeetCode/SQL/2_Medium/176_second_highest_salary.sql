-- [ LeetCode ] 176. Second Highest Salary

SELECT
    CASE COUNT(salary)
        WHEN 1 THEN null
        ELSE MIN(salary)
    END AS SecondHighestSalary
FROM (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 2
) AS salaries;


/*
아래와 같이 WHERE 구에 서브쿼리를 활용하여 문제를 훨씬 간단하게 해결할 수 있었다.
추가적으로 LIMIT 및 OFFSET 키워드를 활용하여 문제를 접근할 수도 있긴 한데 두 번째 값이 항상 존재할 것이라는 보장이 없기 때문에
만약 두 번째 값이 존재하지 않을 경우 NULL 값을 다룰 방법이 없어 문제가 된다.
*/

SELECT
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);
