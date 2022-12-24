-- [ LeetCode ] 1212. Team Scores in Football Tournament

/*
처음에 단순히 Teams 테이블에 대해 두 번의 INNER JOIN 구를 사용한 뒤에 SUM 함수를 사용하면 될 것 같다고 생각했는데
그랬을 경우 중복된 데이터 값이 생길 뿐만 아니라 SUM 함수 자체도 사용할 수 없다.
따라서 정상적으로 문제를 해결하기 위해 조금 복잡하지만 호스트로 경기를 진행한 경우와 게스트로 경기를 진행한 경우를 나누어 각각 Teams 테이블에 LEFT JOIN 구를 사용하고
그 결괏값인 두 테이블을 INNER JOIN 구로 결합하여 문제를 해결했다.
*/

SELECT
    HostMatches.team_id AS team_id,
    HostMatches.team_name AS team_name,
    HostMatches.num_points + GuestMatches.num_points AS num_points
FROM (
    SELECT
        team_id,
        team_name,
        SUM(
            CASE
                WHEN Matches.host_goals > Matches.guest_goals THEN 3
                WHEN Matches.host_goals = Matches.guest_goals THEN 1
                ELSE 0
            END
        ) AS num_points
    FROM Teams
    LEFT JOIN Matches
    ON Teams.team_id = Matches.host_team
    GROUP BY team_id
) AS HostMatches
JOIN (
    SELECT
        team_id,
        SUM(
            CASE
                WHEN Matches.guest_goals > Matches.host_goals THEN 3
                WHEN Matches.guest_goals = Matches.host_goals THEN 1
                ELSE 0
            END
        ) AS num_points
    FROM Teams
    LEFT JOIN Matches
    ON Teams.team_id = Matches.guest_team
    GROUP BY team_id
) AS GuestMatches
USING (team_id)
ORDER BY num_points DESC, team_id ASC;


/*
아래와 같이 훨씬 간단하게 LEFT JOIN 구의 조건으로 ON 구 부분에 OR 키워드를 활용하는 방법으로 문제를 해결할 수 있다.
이때 SUM 함수에 대한 조건으로 CASE 구를 사용하는데 아래는 가독성을 위해 호스트일 경우와 게스트일 경우를 나누고 내부적으로 중첩된 CASE 구를 재사용했지만
단순히 하나의 케이스 구에 각각 호스트인지 또는 게스트인지를 따지는 조건문을 매번 AND 키워드를 활용해 넣어서 문제를 풀 수도 있다.

JOIN 구를 사용할 때 그 조건을 다양하게 활용할 수 있다는 걸 잊지 말아야겠다.
*/

SELECT
    team_id,
    team_name,
    SUM(
        CASE
            WHEN Teams.team_id = Matches.host_team THEN (
                CASE
                    WHEN Matches.host_goals > Matches.guest_goals THEN 3
                    WHEN Matches.host_goals = Matches.guest_goals THEN 1
                    ELSE 0
                END
            )
            ELSE (
                CASE
                    WHEN Matches.guest_goals > Matches.host_goals THEN 3
                    WHEN Matches.guest_goals = Matches.host_goals THEN 1
                    ELSE 0
                END
            )
        END
    ) AS num_points
FROM Teams
LEFT JOIN Matches
ON (
    Teams.team_id = Matches.host_team
    OR
    Teams.team_id = Matches.guest_team
)
GROUP BY team_id
ORDER BY num_points DESC, team_id ASC;
