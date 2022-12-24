-- [ LeetCode ] 1919. Leetcodify Similar Friends

SELECT DISTINCT user1_id, user2_id
FROM Friendship
JOIN Listens AS MyListens
ON Friendship.user1_id = MyListens.user_id
JOIN Listens AS FriendListens
ON (
    Friendship.user2_id = FriendListens.user_id
    AND
    MyListens.song_id = FriendListens.song_id
    AND
    MyListens.day = FriendListens.day
)
GROUP BY Friendship.user1_id, Friendship.user2_id, MyListens.day
HAVING COUNT(DISTINCT MyListens.song_id) >= 3;
