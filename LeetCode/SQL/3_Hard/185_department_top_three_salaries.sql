-- [ LeetCode ] 185. Department Top Three Salaries

SELECT
    Department.name AS Department,
    EmployeeSalaryRank.name AS Employee,
    EmployeeSalaryRank.salary AS Salary
FROM Department
JOIN (
    SELECT
        name,
        salary,
        departmentId,
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS salary_rank
    FROM Employee
) AS EmployeeSalaryRank
ON (
    EmployeeSalaryRank.salary_rank <= 3
    AND
    Department.id = EmployeeSalaryRank.departmentId
);
