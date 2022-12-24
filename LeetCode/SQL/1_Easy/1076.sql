-- [ LeetCode ] 1076. Project Employees II

SELECT project_id
FROM Project
GROUP BY project_id
HAVING COUNT(employee_id) = (
    SELECT MAX(cnt)
    FROM (
        SELECT COUNT(employee_id) AS cnt
        FROM Project
        GROUP BY project_id
    ) AS Counted_Project
);