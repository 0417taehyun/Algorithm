-- [ LeetCode ] 1729. Find Followers Count

-- 본인이 본인을 팔로우하는 경우 횟수에서 제외해야 할 것 같아서 WHERE 구를 추가했다.

SELECT
    user_id,
    COUNT(follower_id) AS followers_count
FROM Followers
WHERE user_id <> follower_id
GROUP BY user_id
ORDER BY user_id;