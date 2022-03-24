-- [ LeetCode ] 511. Game Play Analysis I

/*
LEFT JOIN을 사용하여 아래와 같이 문제를 해결했다.
event_date 필드의 값이 큰 경우에 JOIN을 하게 되면,
한번만 접속한 사용자는 물론 다중 접속한 사용자 또한 Joined_Table 테이블의 player_id 필드 값이 NULL인 경우를 통해 최초의 로그인 시점을 구할 수 있다.
event_date 필드의 값이 작은 경우로 JOIN을 하게 되면 한번만 접속한 사용자는 제외되기 때문에 주의해야 한다.
*/

SELECT
    Activity.player_id AS player_id,
    Activity.event_date AS first_login
FROM Activity
LEFT JOIN Activity AS Joined_Table
ON (
    Activity.player_id = Joined_Table.player_id
    AND
    Activity.event_date > Joined_Table.event_date
)
WHERE Joined_Table.player_id IS NULL;


/*
아래와 같이 훨씬 간단하게 GROUP BY 및 MIN을 사용하여 문제를 해결할 수 있다.
기존 집계함수의 경우 가장 작은 값만을 반환하는 것으로 헷갈렸었는데 해당 경우는 COUNT 함수이다.

추가적으로 MIN 및 MAX는 GROUP BY를 사용하지 않더라도 사용 가능하다.
*/

SELECT
    player_id,
    MIN(event_date) AS first_login
FROM Activity
GROUP BY player_id;