-- [ LeetCode ] 2153. The Number of Passengers in Each Bus II

/*
누적된 차이를 계속해서 비교해가야 하기 때문에 WITH RECURSIVE 공통 테이블 표현식을 활용해서 문제를 풀 수 있다.
이때 arrival_time 필드를 기준으로 오름차순 정렬한 ROW_NUMBER 윈도우 함수(Window Function)를 사용해서 재귀의 기준이 되는 JOIN 구의 조건을 성사시킬 수 있다.
*/

WITH RECURSIVE cte1 (row_num, bus_id, capacity, waited_passengers_cnt) AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY Periods.arrival_time ASC) AS row_num,
        Periods.bus_id,
        Periods.capacity,
        COUNT(Passengers.passenger_id) AS waited_passengers_cnt
    FROM (
        SELECT
            bus_id,
            capacity,            
            arrival_time,
            LAG(arrival_time, 1, -1) OVER(ORDER BY arrival_time ASC) AS previous_time
        FROM Buses
    ) AS Periods
    LEFT JOIN Passengers
    ON (
        Periods.arrival_time >= Passengers.arrival_time
        AND
        Periods.previous_time < Passengers.arrival_time
    )
    GROUP BY Periods.bus_id
), cte2 (row_num, bus_id, diff, passengers_cnt) AS (
    SELECT
        row_num,
        bus_id,
        IF(capacity < waited_passengers_cnt, waited_passengers_cnt - capacity, 0) AS diff,
        IF(capacity < waited_passengers_cnt, capacity, waited_passengers_cnt) AS passengers_cnt
    FROM cte1
    WHERE row_num = 1
    UNION ALL
    SELECT
        cte1.row_num,
        cte1.bus_id,
        IF(cte1.capacity < cte1.waited_passengers_cnt + cte2.diff, cte1.waited_passengers_cnt + cte2.diff - cte1.capacity, 0) AS diff,
        IF(cte1.capacity < cte1.waited_passengers_cnt + cte2.diff, cte1.capacity, cte1.waited_passengers_cnt + cte2.diff) AS passengers_cnt
    FROM cte1
    JOIN cte2
    ON cte1.row_num = cte2.row_num + 1
)

SELECT bus_id, passengers_cnt
FROM cte2
ORDER BY bus_id ASC;
