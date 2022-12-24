-- [ LeetCode ] 2004. The Number of Seniors and Juniors to Join the Company

-- NULL 값이 반환되는 상황을 항항 주의하자.

WITH Cumulatives (employee_id, experience, cumulative_salaries) AS (
    SELECT 
        employee_id,
        experience,
        SUM(salary) OVER(PARTITION BY experience ORDER BY salary ASC) AS cumulative_salaries
    FROM Candidates
), Seniors (experience, accepted_candidates, remained_budget) AS (
    SELECT
        'Senior' AS experience,
        COUNT(employee_id) AS accepted_candidates,
        70000 - IFNULL(MAX(cumulative_salaries), 0) AS remained_budget
    FROM Cumulatives
    WHERE (
        experience = 'Senior'
        AND
        cumulative_salaries <= 70000
    )
), Juniors (experience, accepted_candidates) AS (
    SELECT
        'Junior' AS experience,
        COUNT(employee_id) AS accepted_candidates
    FROM Cumulatives
    WHERE (
        experience = 'Junior'
        AND
        cumulative_salaries <= (SELECT remained_budget FROM Seniors)
    )
)

SELECT
    experience,
    accepted_candidates
FROM Seniors
UNION ALL
SELECT
    experience,
    accepted_candidates
FROM Juniors;
