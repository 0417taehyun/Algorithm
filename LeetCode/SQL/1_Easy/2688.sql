-- [ LeetCode ] 2668. Find Latest Salaries

SELECT
    Salary.emp_id,
    Salary.firstname,
    Salary.lastname,
    Salary.salary,
    Salary.department_id
FROM Salary
JOIN (
    SELECT 
        emp_id,
        MAX(salary) AS salary
    FROM Salary
    GROUP BY emp_id
) AS CurrentSalary
USING (emp_id, salary)
ORDER BY emp_id ASC;
