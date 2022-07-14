-- [ LeetCode ] 2339. All the Matches of the League

SELECT
    HomeTeams.team_name AS home_team,
    AwayTeams.team_name AS away_team
FROM Teams AS HomeTeams
JOIN Teams AS AwayTeams
ON HomeTeams.team_name <> AwayTeams.team_name;
