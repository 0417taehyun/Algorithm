-- [ LeetCode ] 1709. Biggest Window Between Visits

SELECT
    user_id,
    MAX(date_diff) AS biggest_window
FROM (
    SELECT
        user_id,
        DATEDIFF(IFNULL(LEAD(visit_date) OVER(PARTITION BY user_id ORDER BY visit_date ASC), '2021-1-1'), visit_date) AS date_diff
    FROM UserVisits
) AS UserVisitedDateDiff
GROUP BY user_id
ORDER BY user_id;


/*
LEAD 윈도우 함수(Window Function)의 경우 기본적으로 값이 없을 경우 `NULL`을 반환하게 되어있기 때문에 임의로 기본값을 설정할 수 있다.
따라서 위 풀이와 같이 IFNULL 함수를 사용하여 `NULL`값에 대한 처리를 따로 해주는 것이 아니라 아래처럼 기본값으로 지정해주면 된다.
이때 중간에 위치한 `1`이 의미하는 것은 간격이다. 따라서 만약 해당 값이 `2`일 경우 다음 값이 아닌 다다음 값을 반환한다.
*/

SELECT
    user_id,
    MAX(date_diff) AS biggest_window
FROM (
    SELECT
        user_id,
        DATEDIFF(LEAD(visit_date, 1, '2021-1-1') OVER(PARTITION BY user_id ORDER BY visit_date ASC), visit_date) AS date_diff
    FROM UserVisits
) AS UserVisitedDateDiff
GROUP BY user_id
ORDER BY user_id;
