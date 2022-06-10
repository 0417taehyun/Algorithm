-- [ LeetCode ] 1194. Tournament Winners

/*
처음에 WITH 구에 작성된 LEFT JOIN 구를 fist_player 필드와 일치한 경우와 second_player 필드와 일치한 경우로 나누어 작성했는데
이럴 경우 first_player 필드가 일치한 행이 second_player 필드가 일치하는 경우가 복수 존재할 경우 그 개수 만큼 중복되어 반복되기 때문에 정상적으로 원하는 합계에 따른 순위를 구할 수 없었다.
따라서 이를 해결하기 위해서 단순히 LEFT JOIN 구를 한번만 사용하는 대신 ON 구에 그 조건으로 OR 키워드를 사용해야 한다.

JOIN 구를 여러 번 사용할 경우 행이 반복되는 경우에 대해 유의할 필요가 있다.
*/

WITH MatchesResults (group_id, player_id, player_rank) AS (
    SELECT
        Players.group_id,
        Players.player_id,
        RANK() OVER(
            PARTITION BY group_id
            ORDER BY IFNULL(SUM(IF(Players.player_id = Matches.first_player, Matches.first_score, Matches.second_score)), 0) DESC, Players.player_id ASC
        ) AS player_rank
    FROM Players
    LEFT JOIN Matches
    ON (
        Players.player_id = Matches.first_player
        OR
        Players.player_id = Matches.second_player
    )
    GROUP BY Players.player_id
)

SELECT
    group_id,
    player_id
FROM MatchesResults
WHERE player_rank = 1;
