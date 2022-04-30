-- [ LeetCode ] 614. Second Degree Follower

-- MySQL의 경우 문자의 대소문자 상관 없이 해당 문자를 동일하게 취급해주지만 Oracle의 경우 대소문자에 따라 동일한 문자라도 다르게 취급한다.

SELECT
    Follow.followee AS follower,
    COUNT(DISTINCT Follow.follower) AS num
FROM Follow
JOIN Follow AS Followers
ON (Follow.followee = Followers.follower)
GROUP BY Follow.followee
ORDER BY follower;
