-- [ 프로그래머스 ] 입양 시각 구하기 (2)

-- 아래와 같이 `UNION`을 사용하여 임시 테이블을 만들어서 문제를 해결했다.

SELECT
    HOUR_TABLE.HOUR AS HOUR,
    COUNT(ORIGIN.HOUR) AS COUNT
FROM (
        SELECT 0
        UNION
        SELECT 1
        UNION
        SELECT 2
        UNION
        SELECT 3
        UNION
        SELECT 4
        UNION
        SELECT 5
        UNION
        SELECT 6
        UNION
        SELECT 7
        UNION
        SELECT 8
        UNION
        SELECT 9
        UNION
        SELECT 10
        UNION
        SELECT 11
        UNION
        SELECT 12
        UNION
        SELECT 13
        UNION
        SELECT 14
        UNION
        SELECT 15
        UNION
        SELECT 16
        UNION
        SELECT 17
        UNION
        SELECT 18
        UNION
        SELECT 19
        UNION
        SELECT 20
        UNION
        SELECT 21
        UNION
        SELECT 22
        UNION
        SELECT 23                               
    ) AS HOUR_TABLE
LEFT JOIN (
    SELECT HOUR(DATETIME) AS HOUR
    FROM ANIMAL_OUTS
) AS ORIGIN
USING (HOUR)
GROUP BY HOUR
ORDER BY HOUR;


/*
아래와 같이 WITH RECURSIVE 문법을 통해 재귀쿼리를 사용할 수 있다.
이때 UNION ALL 문법은 중복 여부와 상관 없이 모든 데이터를 수평으로 결합하여 출력한다.

JOIN 구문이나 다른 구문에 서브쿼리를 사용할 경우 AS를 반드시 사용해줘야 한다.
추가적으로 IFNULL의 경우 만약 NULL일 경우 두 번째 매개변수 값을 반환하고 그렇지 않을 경우 원래의 값인 첫 번째 매개변수를 반환한다.
*/

WITH RECURSIVE HOUR_TABLE (HOUR) AS (
    SELECT 0
    UNION ALL
    SELECT HOUR + 1
    FROM HOUR_TABLE
    WHERE HOUR
    BETWEEN 0 AND 22
)

SELECT
    HOUR_TABLE.HOUR AS HOUR,
    IFNULL(ORIGIN.COUNT, 0) AS COUNT
FROM HOUR_TABLE
LEFT JOIN (
    SELECT
        HOUR(DATETIME) AS HOUR,
        COUNT(HOUR(DATETIME)) AS COUNT
    FROM ANIMAL_OUTS
    GROUP BY HOUR(DATETIME)
) AS ORIGIN
USING (HOUR)
ORDER BY HOUR;