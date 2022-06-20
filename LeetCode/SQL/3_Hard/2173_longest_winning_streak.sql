-- [ LeetCode ] 2173. Longest Winning Streak

SELECT
    player_id,
    IFNULL(longest_streak, 0) AS longest_streak
FROM (
    SELECT DISTINCT player_id
    FROM Matches
) AS Players
LEFT JOIN (
    SELECT
        DISTINCT player_id,
        MAX(COUNT(match_day)) OVER(PARTITION BY player_id) AS longest_streak
    FROM (
        SELECT
            player_id,
            match_day,
            result,
            (
                CAST(ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY match_day ASC) AS UNSIGNED)
                -
                CAST(COUNT(IF(result = 'Win', 1, NULL)) OVER(PARTITION BY player_id ORDER BY match_day ASC) AS UNSIGNED)
            ) AS diff
        FROM Matches
    ) AS ConsecutiveWinnings
    WHERE result = 'Win'
    GROUP BY player_id, diff
) AS LongestStreaks
USING (player_id);
