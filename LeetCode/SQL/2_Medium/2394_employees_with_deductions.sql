-- [ LeetCode ] 2394. Employees With Deductions

SELECT Employees.employee_id
FROM Employees
LEFT JOIN Logs
USING (employee_id)
GROUP BY Employees.employee_id, Employees.needed_hours
HAVING (
    Employees.needed_hours
    >
    SUM(CEIL(IFNULL(TIMESTAMPDIFF(second, in_time, out_time), 0) / 60) / 60)
);
