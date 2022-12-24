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
USING (team_id);


-- 아래와 같이 WINDOW 함수를 사용하여 해결할 수도 있다.

SELECT
    employee_id,
    COUNT(employee_id) OVER(PARTITION BY team_id) AS team_size
FROM Employee
ORDER BY team_size DESC, employee_id ASC;