-- [ LeetCode ] 571. Find Median Given Frequency of Numbers

WITH RECURSIVE MedianPositions (mid_number, flag) AS (
    SELECT
        ROUND(SUM(frequency) / 2) AS mid_number,
        MOD(SUM(frequency), 2) AS flag
    FROM Numbers
    UNION ALL
    SELECT
        mid_number + 1 as mid_number,
        flag + 1 AS flag
    FROM MedianPositions
    WHERE flag = 0
)

SELECT ROUND(AVG(NumberRanges.num), 1) AS median
FROM (
    SELECT
        num,
        LAG(end_num, 1, 0) OVER(ORDER BY num ASC) AS start_num,
        end_num
    FROM (
        SELECT
            num,
            SUM(frequency) OVER(ORDER BY num ASC) AS end_num
        FROM Numbers
    ) AS EndNumbers
) AS NumberRanges
JOIN MedianPositions
ON MedianPositions.mid_number BETWEEN NumberRanges.start_num + 1 AND NumberRanges.end_num;


