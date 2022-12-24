-- [ LeetCode ] 1107. New Users Daily Count

-- MIN 함수는 `NULL` 값을 따로 처리하지 않고 넘긴다.

SELECT
    first_logged_in AS login_date,
    COUNT(user_id) AS user_count
FROM (
    SELECT
        user_id,
        MIN(IF(activity='login', activity_date, null)) AS first_logged_in
    FROM Traffic
    GROUP BY user_id
) AS UserFirstLoggedIn
WHERE DATEDIFF("2019-06-30", first_logged_in) BETWEEN 0 AND 90
GROUP BY first_logged_in;
