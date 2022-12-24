-- [ LeetCode ] 1077. Project Employees III

SELECT
    project_id,
    employee_id
From (
    SELECT
        project_id,
        employee_id,
        RANK() OVER(PARTITION BY project_id ORDER BY experience_years DESC) AS year_rank
    FROM Project
    JOIN Employee
    USING (employee_id)
) AS YearRank
WHERE year_rank = 1;
