-- [ LeetCode ] 1949. Strong Friendship

/*
처음에 아래와 같이 풀었는데 테스트 케이스는 통과하더라도 결국 시간이 초과되어 제출이 반려됐다.
JOIN 구에서 별다른 조건 없이 모든 경우의 수를 다 구한 다음에 이를 COUNT 함수를 활용해서 계산을 하기 때문에 발생한 시간 초과였다.

SELECT
    user1_id,
    user2_id,
    common_friend
FROM (
    SELECT
        Friendship.user1_id,
        Friendship.user2_id,
        COUNT(
            CASE
                WHEN Friendship.user1_id = X.user1_id THEN
                    CASE
                        WHEN Friendship.user2_id = Y.user1_id THEN IF(X.user2_id = Y.user2_id, 1, NULL)
                        ELSE IF(X.user2_id = Y.user1_id, 1, NULL)
                    END
                ELSE
                    CASE
                        WHEN Friendship.user2_id = Y.user1_id THEN IF(X.user1_id = Y.user2_id, 1, NULL)
                        ELSE IF(X.user1_id = Y.user1_id, 1, NULL)
                    END
            END 
        ) AS common_friend
    FROM Friendship
    JOIN Friendship AS X
    ON (
        Friendship.user1_id = X.user1_id
        OR
        Friendship.user1_id = X.user2_id
    )
    JOIN Friendship AS Y
    ON (
        Friendship.user2_id = Y.user1_id
        OR
        Friendship.user2_id = Y.user2_id
    )
    GROUP BY Friendship.user1_id, Friendship.user2_id
) AS CommonFriends
WHERE common_friend >= 3;

그래서 다른 사람이 제출한 답안을 보고 아래와 같이 문제를 해결했다.
JOIN 구에 따른 user1_id 필드 및 user2_id 필드 중 어느 곳에 일치하는 지에 따라 조건을 분기했던 지점을
WITH 구 및 UNION ALL 키워드와 user1_id 필드 및 user2_id 필드를 뒤집어서 정의하는 방법을 통해 간단하게 해결할 수 있었다.
*/

WITH cte (user1_id, user2_id) AS (
    SELECT
        user1_id,
        user2_id
    FROM Friendship
    UNION ALL
    SELECT
        user2_id AS user1_id,
        user1_id AS user2_id
    FROM Friendship
)

SELECT
    Friendship.user1_id,
    Friendship.user2_id,
    COUNT(XUser.user2_id) AS common_friend
FROM Friendship
JOIN cte AS XUser
USING (user1_id)
JOIN cte AS YUser
ON (
    Friendship.user2_id = YUser.user1_id
    AND
    XUser.user2_id = YUser.user2_id
)
GROUP BY Friendship.user1_id, Friendship.user2_id
HAVING COUNT(XUser.user2_id) >= 3;
