-- [ LeetCode ] 1126. Active Businesses

SELECT business_id
FROM Events
JOIN (
    SELECT
        event_type,
        AVG(occurences) AS event_average
    FROM Events
    GROUP BY event_type
) AS EventAverage
ON (
    Events.event_type = EventAverage.event_type
    AND
    Events.occurences > EventAverage.event_average
)
GROUP BY business_id
HAVING COUNT(Events.event_type) > 1;


/*
아래처럼 WITH 구를 사용하여 문제를 간단하게 해결할 수도 있다.
IF 함수 및 AVG 윈도우 함수(Window Function)를 사용하여 평균보다 큰 경우 TRUE 값을, 그렇지 않은 경우 FALSE 값을 부여한 flag 필드를 생성하고
해당 flag 필드를 합산했을 때 TRUE 값의 경우 `1`, FALSE 값의 경우 `0`으로 치환되기 때문에 `1`보다 큰 경우만 골라준다.
*/

WITH cte (business_id, flag) AS (
    SELECT
        business_id,
        IF(occurences > AVG(occurences) OVER(PARTITION BY event_type), TRUE, FALSE) AS flag
    FROM Events
)


SELECT business_id
FROM cte
GROUP BY business_id
HAVING SUM(flag) > 1;
