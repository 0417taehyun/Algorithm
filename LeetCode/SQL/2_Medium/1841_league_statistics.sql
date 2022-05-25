-- [ LeetCode ] 1841. League Statistics

SELECT
    team_name,
    COUNT(team_id) AS matches_played,
    SUM(CASE team_id
        WHEN home_team_id THEN
            CASE
                WHEN home_team_goals > away_team_goals THEN 3
                WHEN home_team_goals = away_team_goals THEN 1
                ELSE 0
            END
        WHEN away_team_id THEN
            CASE
                WHEN away_team_goals > home_team_goals THEN 3
                WHEN away_team_goals = home_team_goals THEN 1
                ELSE 0
            END
    END) AS points,
    SUM(IF(team_id = home_team_id, home_team_goals, away_team_goals)) AS goal_for,
    SUM(IF(team_id = home_team_id, away_team_goals, home_team_goals)) AS goal_against,
    SUM(IF(team_id = home_team_id, (home_team_goals - away_team_goals), (away_team_goals - home_team_goals))) AS goal_diff
FROM Teams
JOIN Matches
ON (
    team_id = home_team_id
    OR
    team_id = away_team_id
)
GROUP BY team_id, team_name
ORDER BY points DESC, goal_diff DESC, team_name ASC;
