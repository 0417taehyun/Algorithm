-- [ LeetCode ] 1225. Report Contiguous Dates

WITH FailTasks (period_state, start_date, end_date) AS (
    SELECT
        'failed' AS period_state,
        MIN(fail_date) AS start_date,
        MAX(fail_date) AS end_date
    FROM (
        SELECT
            fail_date,
            DATE_SUB(fail_date, INTERVAL ROW_NUMBER() OVER(ORDER BY fail_date ASC) DAY) AS grouping_option
        FROM Failed
        WHERE YEAR(fail_date) = 2019    
    ) AS SubFailed
    GROUP BY grouping_option
), SuccessTasks (period_state, start_date, end_date) AS (
    SELECT
        'succeeded' AS period_state,
        MIN(success_date) AS start_date,
        MAX(success_date) AS end_date
    FROM (
        SELECT
            success_date,
            DATE_SUB(success_date, INTERVAL ROW_NUMBER() OVER(ORDER BY success_date ASC) DAY) AS grouping_option  
        FROM Succeeded
        WHERE YEAR(success_date) = 2019
    ) AS SubSucceded
    GROUP BY grouping_option
)

SELECT
    period_state,
    start_date,
    end_date
FROM FailTasks
UNION ALL
SELECT
    period_state,
    start_date,
    end_date
FROM SuccessTasks
ORDER BY start_date ASC;
