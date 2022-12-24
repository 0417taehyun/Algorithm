-- [ LeetCode ] 1378. Replace Employee ID With The Unique Identifier

SELECT unique_id, name
FROM Employees
LEFT JOIN EmployeeUNI
USING (id);