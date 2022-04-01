-- [ LeetCode ] 1303. Find the Team Size

SELECT
    Employee.employee_id,
    team_size
FROM Employee
JOIN (
    SELECT
        team_id,
        COUNT(employee_id) AS team_size
    FROM Employee
    GROUP BY team_id
) AS Teams
USING (team_id)