-- [ LeetCode ] 1783. Grand Slam Titles

SELECT
    player_id,
    player_name,
    SUM(
        IF(player_id = Wimbledon, 1, 0)
        +
        IF(player_id = Fr_open, 1, 0)
        +
        IF(player_id = US_open, 1, 0)
        +
        IF(player_id = Au_open, 1, 0)
    ) AS grand_slams_count
FROM Players
JOIN Championships
ON (
    player_id = Wimbledon
    OR
    player_id = Fr_open
    OR
    player_id = US_open
    OR
    player_id = Au_open
)
GROUP BY player_id, player_name;
