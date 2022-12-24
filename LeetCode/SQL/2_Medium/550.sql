-- [ LeetCode ] 550. Game Play Analysis IV

/*
확장성을 고려한 쿼리를 생각해봤다.
처음 로그인한 날짜를 기준으로 연속해서 하루 이상만 접속해도 되는 경우가 아닌 마지막 로그인한 날짜를 기준으로 할 수도 있고, 아예 로그인 기준 없이 그저 연속되는 날짜를 구해야 할 수도 있다.
물론 이때도 연속의 횟수가 3회, 4회 이상일 수도 있으며 추가적으로 이틀에 한번 접속한 경우에 대해 답을 구하고 싶을 수도 있다.
이러한 확장성을 고려했을 때 ROW_NUMBER 및 LEAD 윈도우 함수(Window Function), 그리고 DATEDIFF 함수를 사용하였다.
*/

SELECT ROUND(SUM(row_num = 1 AND date_diff = 1) / COUNT(DISTINCT player_id), 2) AS fraction
FROM (
    SELECT
        ROW_NUMBER() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS row_num,
        player_id,
        device_id,
        games_played,
        DATEDIFF(LEAD(event_date) OVER(PARTITION BY player_id ORDER BY event_date ASC), event_date) AS date_diff
    FROM Activity
) AS Activity_With_Next_Event_Date;


/*
아래와 같이 문제를 간단하게 해결할 수 있었다.

먼저 FROM 구에 사용되는 서브쿼리 문법에서 MIN 부분을 변형하여 해결할 수 있다.
이때 MIN 함수를 사용한 이유는 가장 처음 로그인한 날짜를 기준으로 답을 구하기 위해서다.

다음으로 LEFT JOIN 구를 사용하여 player_id 필드의 값이 동일하고,
처음 로그인한 날짜 기준으로 DATEDIFF 함수를 사용해 그 간격이 `1`인 경우를 합쳐준다.
이때 해당 값이 없을 경우 `NULL` 값으로 처리가 되는데 Grouped_Activity 테이블에 존재하는 중복이 제거된 전체 사용자 수를 계산하기 위해 INNER JOIN 구가 아닌 LEFT JOIN 구를 사용한 것이다.

마지막으로 LEFT JOIN 구를 통해 player_id 필드의 값이 `NULL`이 아닐 경우 처음 로그인한 날짜 기준으로 연속해서 로그인한 사용자이기 때문에 이를 COUNT 함수를 통해 세고,
Grouped_Activity 테이블에 존재하는 player_id 필드의 수가 곧 -player_id 필드를 기준으로 그룹핑되었기 때문에- 중복되지 않은 모든 사용자 수를 의미하기 때문에 이를 COUNT 함수를 통해 세어
두 결괏값을 나눠주고 이를 ROUND 함수를 사용하여 반올림처리 한다. 만약 올림처리를 하길 원했다면 CEIL 함수를, 내림처리를 하길 원했다면 FLOOR 함수를 사용하면 된다.
*/

SELECT ROUND(COUNT(Activity.player_id) / COUNT(Grouped_Activity.player_id), 2) AS fraction
FROM (
    SELECT
        player_id,
        MIN(event_date) AS first_logged_in
    FROM Activity
    GROUP BY player_id
) AS Grouped_Activity
LEFT JOIN Activity
ON (
    Grouped_Activity.player_id = Activity.player_id
    AND
    DATEDIFF(Activity.event_date, Grouped_Activity.first_logged_in) = 1
);
