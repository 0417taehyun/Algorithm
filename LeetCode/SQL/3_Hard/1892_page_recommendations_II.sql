-- [ LeetCode ] 1892. Page Recommendations II

SELECT
    Users.user_id,
    FriendsLikes.page_id,
    COUNT(FriendsLikes.user_id) AS friends_likes
FROM (
    SELECT
        user1_id AS user_id,
        user2_id AS friend_id
    FROM Friendship
    UNION ALL
    SELECT
        user2_id AS user_id,
        user1_id AS friend_id
    FROM Friendship
) AS Users
JOIN Likes AS FriendsLikes
ON Users.friend_id = FriendsLikes.user_id
LEFT JOIN Likes AS MyLikes
ON (
    Users.user_id = MyLikes.user_id
    AND
    FriendsLikes.page_id = MyLikes.page_id
)
WHERE MyLikes.user_id IS NULL
GROUP BY Users.user_id, FriendsLikes.page_id;
