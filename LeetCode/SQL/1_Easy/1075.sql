-- [ LeetCode ] 1075. Project Employees I

SELECT
    project_id,
    ROUND(AVG(experience_years), 2) AS average_years
FROM Project
JOIN Employee
USING (employee_id)
GROUP BY project_id;