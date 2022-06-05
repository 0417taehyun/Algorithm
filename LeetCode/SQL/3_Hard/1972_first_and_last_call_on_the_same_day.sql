-- [ LeetCode ] 1972. First and Last Call On the Same Day

/*
처음에 아래와 같이 문제를 풀었는데 틀렸다.
날짜 별 첫 번째 통화와 마지막 통화의 사용자 쌍(Pair)이 같은 경우를 구하는 것으로 착각했기 때문이다.


WITH CallTimes (caller_id, recipient_id, call_date, recent_to_past, past_to_recent) AS (
    SELECT
        caller_id,
        recipient_id,
        DATE(call_time) AS call_date,
        DENSE_RANK() OVER(PARTITION BY DATE(call_time) ORDER BY call_time ASC) AS past_to_recent,
        DENSE_RANK() OVER(PARTITION BY DATE(call_time) ORDER BY call_time DESC) AS recent_to_past
    FROM Calls
), cte (caller_id, recipient_id) AS (
    SELECT
        FirstCalls.caller_id,
        FirstCalls.recipient_id
    FROM (
        SELECT
            caller_id,
            recipient_id,
            call_date
        FROM CallTimes
        WHERE past_to_recent = 1
    ) AS FirstCalls
    JOIN (
        SELECT
            caller_id,
            recipient_id,
            call_date
        FROM CallTimes
        WHERE recent_to_past = 1
    ) AS LastCalls
    ON (
        FirstCalls.call_date = LastCalls.call_date
        AND
        (
            (
                FirstCalls.caller_id = LastCalls.caller_id
                AND
                FirstCalls.recipient_id = LastCalls.recipient_id
            )
            OR
            (
                FirstCalls.caller_id = LastCalls.recipient_id
                AND
                FirstCalls.recipient_id = LastCalls.caller_id
            )
        )
    )
)

SELECT caller_id AS user_id
FROM cte
UNION
SELECT recipient_id AS user_id
FROM cte;


사용자의 날짜 별 첫 통화의 대상자가 마지막 통화 대상자랑 일치하는 사용자를 구하는 문제였기 때문에 아래와 같이 UNION ALL 키워드를 활용했다.
그리고 DENSE_RANK 윈도우 함수(Window Function)을 사용하여 첫 통화와 마지막 통화를 구해서 JOIN 구를 통해 일치하는 경우만 도출했다.

이때 유의할 점은 UNION 또는 UNION ALL 구를 사용할 때는 SELECT 구에서의 순서에 유의해야 한다는 것이다.
만약 아래 UNION ALL 키워드 다음에 오는 SELECT 구에서 첫 번째 필드를 `caller_id AS recipient_id`와 같이 정의할 경우
앞선 필드에서 첫 번째 필드가 caller_id 필드이기 때문에 이름에 따라 이것이 자동으로 매칭되어지는 게 아니라 순서대로 매칭이 되어
정의한 대로 recipient_id 필드가 아닌 caller_id 필드가 된다.
따라서 UNION 또는 UNION ALL 구를 사용할 때는 SELECT 구에서 필드를 정의할 때 그 순서에 유의해야 한다.
*/


WITH cte (caller_id, recipient_id, call_date, past_to_recent, recent_to_past) AS (
    SELECT
        caller_id,
        recipient_id,
        DATE(call_time) AS call_date,
        DENSE_RANK() OVER(PARTITION BY caller_id, DATE(call_time) ORDER BY call_time ASC) AS past_to_recent,
        DENSE_RANK() OVER(PARTITION BY caller_id, DATE(call_time) ORDER BY call_time DESC) AS recent_to_past
    FROM (
        SELECT
            caller_id,
            recipient_id,
            call_time
        FROM Calls
        UNION ALL
        SELECT
            recipient_id AS caller_id,
            caller_id AS recipient_id,
            call_time
        FROM Calls
    ) AS AllCallers
)

SELECT DISTINCT caller_id AS user_id
FROM (
    SELECT
        caller_id,
        recipient_id,
        call_date
    FROM cte
    WHERE past_to_recent = 1
) AS FirstCalls
JOIN (
    SELECT
        caller_id,
        recipient_id,
        call_date
    FROM cte
    WHERE recent_to_past = 1
) AS LastCalls
USING (caller_id, recipient_id, call_date);
