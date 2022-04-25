-- [ LeetCode ] 534. Game Play Analysis III

SELECT
    Activity.player_id AS player_id,
    Activity.event_date AS event_date,
    SUM(Played_Games.games_played) AS games_played_so_far
FROM Activity
JOIN Activity AS Played_Games
ON (
    Activity.player_id = Played_Games.player_id
    AND
    Activity.event_date >= Played_Games.event_date
)
GROUP BY player_id, event_date;
