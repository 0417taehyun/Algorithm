-- [ LeetCode ] 1917. Leetcodify Friends Recommendations

/*
NOT IN 구를 사용하지 않고 문제릃 해결하려 하다보니 쉽지 않았다.
JOIN 구의 방향성과 그 결괏값에 따라 어떻게 NULL 값이 생성되는지 유의 해야겠다.
직접 접근법을 생각할 때 테이블을 대략적으로 그려본 게 도움이 되었다. 실제 문제 풀 때도 헷갈리는 경우 이렇게 해봐야겠다.
*/

WITH Users (user_id, friend_id) AS (
    SELECT user1_id AS user_id, user2_id AS friend_id
    FROM Friendship
    UNION ALL
    SELECT user2_id AS user_id, user1_id AS friend_id
    FROM Friendship
), Recommendations (user_id, recommended_id) AS (
    SELECT
        DISTINCT Listens.user_id AS user_id,
        SubListens.user_id AS recommended_id
    FROM Listens
    JOIN Listens AS SubListens
    ON (
        Listens.user_id <> SubListens.user_id
        AND
        Listens.song_id = SubListens.song_id
        ANd
        Listens.day = SubListens.day
    )
    LEFT JOIN Users
    ON (
        Listens.user_id = Users.user_id
        AND
        SubListens.user_id = Users.friend_id
    )
    WHERE Users.user_id IS NULL
    GROUP BY Listens.user_id, SubListens.user_id, Listens.day
    HAVING COUNT(DISTINCT Listens.song_id) >= 3
)

SELECT user_id, recommended_id
FROM Recommendations;
