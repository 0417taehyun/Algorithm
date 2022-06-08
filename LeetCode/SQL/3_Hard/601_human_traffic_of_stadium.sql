-- [ LeetCode ] 601. Human Traffic of Stadium

SELECT
    id,
    visit_date,
    people
FROM (
    SELECT
        id,
        visit_date,
        people,
        COUNT(id) OVER(PARTITION BY diff) AS consecutive_counts
    FROM (
        SELECT
            id,
            visit_date,
            people,
            (id - ROW_NUMBER() OVER(ORDER BY id ASC)) AS diff
        FROM Stadium
        WHERE people >= 100
    ) AS ConsecutiveIds
) AS ConsecutiveCounts
WHERE consecutive_counts >= 3
ORDER BY visit_date ASC;
