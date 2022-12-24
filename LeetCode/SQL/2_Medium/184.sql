-- [ LeetCode ] 184. Department Highest Salary

SELECT
    Department.name AS Department,
    Salary_Rank.name AS Employee,
    Salary_Rank.salary AS Salary
FROM Department
JOIN (
    SELECT
        name,
        salary,
        departmentId,
        RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
) AS Salary_Rank
ON (
    Department.id = Salary_Rank.departmentId
    AND
    Salary_Rank.salary_rank = 1
);


/*
아래와 같이 RANK 윈도우 함수 또는 DENSE_RANK 윈도우 함수를 사용하지 않더라도 WHERE 구에 서브쿼리를 활용하여 문제를 해결할 수도 있다.
이때 유의할 점은 부서 별로 가장 높은 연봉이 책정되어 있는 사람을 조회해야 하기 때문에 서브쿼리에 반환되는 값이 부서 아이디를 의미하는 departmentId 필드와 연봉인 salary 필드 두 개이다.
따라서 IN 구 앞에 튜플 형태로 일치되는 값을 묶어 `(Department.id, Employee.salary)`와 같은 형태로 표현해야 한다.
*/

SELECT
    Department.name AS Department,
    Employee.name AS Employee,
    Employee.salary AS Salary
FROM Employee
JOIN Department
ON Employee.departmentId = Department.id
WHERE (Department.id, Employee.salary) IN (
    SELECT
        departmentId,
        MAX(salary) AS salary
    FROM Employee
    GROUP BY departmentId
);
