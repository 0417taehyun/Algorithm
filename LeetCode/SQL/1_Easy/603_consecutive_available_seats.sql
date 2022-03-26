-- [ LeetCode ] 603. Consecutive Available Seats

-- MySQL에서 1은 true, 0은 false와 같다.

SELECT Cinema.seat_id AS seat_id
FROM Cinema
LEFT JOIN Cinema AS Previous_Cinema
ON Cinema.seat_id - 1 = Previous_Cinema.seat_id
LEFT JOIN Cinema AS Next_Cinema
ON Cinema.seat_id + 1 = Next_Cinema.seat_id
WHERE (
    (
        Cinema.free = 1
        AND
        Previous_Cinema.free = 1
    )
    OR
    (
        Cinema.free = 1
        AND
        Next_Cinema.free = 1
    )    
)
ORDER BY seat_id ASC;


-- 아래와 같이 JOIN을 사용하지 않더라도 WHERE 구 내에서 서브쿼리를 활용해 문제를 해결할 수도 있다.

SELECT DISTINCT seat_id
FROM Cinema
WHERE (
    free = true
    AND (
        seat_id - 1 IN (
            SELECT seat_id
            FROM Cinema
            WHERE free = true
        )
        OR
        seat_id + 1 IN (
            SELECT seat_id
            FROM Cinema
            WHERE free = true
        )
    )
)
ORDER BY seat_id ASC;