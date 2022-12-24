-- [ LeetCode ] 2010. The Number of Seniors and Juniors to Join the Company II

WITH CumulativeSalaries (employee_id, experience, cumulative_salary) AS (
    SELECT
        employee_id,
        experience,
        SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS cumulative_salary
    FROM Candidates
), Seniors (employee_id, cumulative_salary) AS (
    SELECT
        employee_id,
        cumulative_salary
    FROM CumulativeSalaries
    WHERE (
        experience = 'Senior'
        AND
        cumulative_salary <= 70000
    )
), Juniors (employee_id) AS (
    SELECT employee_id
    FROM CumulativeSalaries
    WHERE (
        experience = 'Junior'
        AND
        cumulative_salary <= 70000 - (SELECT IFNULL(MAX(cumulative_salary), 0) FROM Seniors)
    )
)


SELECT employee_id
FROM Seniors
UNION ALL
SELECT employee_id
FROM Juniors;
