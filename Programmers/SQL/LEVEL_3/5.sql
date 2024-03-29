-- [ 프로그래머스 ] 헤비 유저가 소유한 장소

SELECT ID, NAME, HOST_ID
FROM PLACES
WHERE HOST_ID IN (
    SELECT HOST_ID
    FROM PLACES
    GROUP BY HOST_ID
    HAVING COUNT(HOST_ID) >= 2
);


-- 아래와 같이 JOIN 자체에 서브쿼리를 사용하여 문제를 해결할 수도 있다.

SELECT PLACES.ID, PLACES.NAME, PLACEs.HOST_ID
FROM PLACES
JOIN (
    SELECT HOST_ID, COUNT(HOST_ID) AS "COUNT"
    FROM PLACES
    GROUP BY HOST_ID
) AS JOINED_PLACES
USING (HOST_ID)
WHERE COUNT >= 2