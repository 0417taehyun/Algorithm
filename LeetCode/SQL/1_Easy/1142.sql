-- [ LeetCode ] 1142. User Activity for the Past 30 Days II

SELECT IFNULL(ROUND(SUM(sessions) / COUNT(user), 2), 0.00) AS average_sessions_per_user
FROM (
    SELECT
        users AS user,
        COUNT(DISTINCT session_id) AS sessions
        FROM Activity
        WHERE DATEDIFF("2019-07-27", 30) BETWEEN 0 AND 29
        GROUP BY user_id
) AS Counted_Activity;


/*
아래와 같이 DISTINCT 키워드를 사용하여 훨씬 간단하게 문제를 풀 수 있다.
DISTINCT 키워드의 경우 GROUP BY 구와 달리 내부적으로 정렬 연산을 수행하지 않기 때문에 훨씬 빠르다.

문제를 그룹화해서 푸는 걸로 초점을 맞출 때가 많은데 DISTINCT 키워드를 사용하는 방법은 불가능한지 우선적으로 먼저 생각해보는 연습을 해야겠다.
*/

SELECT IFNULL(ROUND(COUNT(DISTINCT session_id) / COUNT(DISTINCT user_id), 2), 0.00) AS average_sessions_per_user
FROM Activity
WHERE DATEDIFF("2019-07-27", activity_date) BETWEEN 0 AND 29;