-- [ LeetCode ] 1731. The Number of Employees Which Report to Each Employee

SELECT
    Managers.employee_id AS employee_id,
    Managers.name AS name,
    COUNT(Employees.name) AS reports_count,
    ROUND(AVG(Employees.age)) AS average_age
FROM Employees AS Managers
JOIN Employees
ON Managers.employee_id = Employees.reports_to
GROUP BY Managers.employee_id
ORDER BY employee_id;