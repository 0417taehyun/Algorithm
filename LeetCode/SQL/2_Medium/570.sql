-- [ LeetCode ] 570. Managers with at Least 5 Direct Reports

SELECT Manager.name AS name
From Employee AS Manager
JOIN Employee
ON Manager.id = Employee.ManagerId
GROUP BY Manager.id
HAVING COUNT(Employee.id) >= 5;
