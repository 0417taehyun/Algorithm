-- [ LeetCode ] 1811. Find Interview Candidates

-- HAVING 구 부분을 통해 확장성 있게 쿼리를 사용할 수 있다.

SELECT
    DISTINCT name,
    mail
FROM (
    SELECT
        user_id,
        mail,
        name,
        contest_id,
        contest_id - ROW_NUMBER() OVER(PARTITION BY user_id ORDER BY contest_id ASC) AS diff,
        COUNT(CASE user_id WHEN gold_medal THEN TRUE END) OVER(PARTITION BY user_id ORDER BY contest_id ASC) AS gold_medal_counts
    FROM Users
    JOIN Contests
    ON (
        user_id = gold_medal
        OR
        user_id = silver_medal
        OR
        user_id = bronze_medal
    )
) AS UserContestResults
GROUP BY user_id, diff
HAVING (
    COUNT(contest_id) >= 3
    OR
    MAX(gold_medal_counts) >= 3
);
