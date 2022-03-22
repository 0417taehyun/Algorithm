-- [ 프로그래머스 ] 없어진 기록 찾기

-- 아래와 같이 서브쿼리 및 `NOT EXISTS` 조건을 활용하여 문제를 풀 수 있다.

SELECT ANIMAL_ID, NAME
FROM ANIMAL_OUTS
WHERE NOT EXISTS (
    SELECT ANIMAL_ID
    FROM ANIMAL_INS
    WHERE ANIMAL_INS.ANIMAL_ID = ANIMAL_OUTS.ANIMAL_ID
)
ORDER BY ANIMAL_ID;


/*
아래와 같이 LEFT JOIN 이후에 ANIMAL_INS 테이블에서의 ANIMAL_ID 필드 값이 `NULL`인 경우를 찾아줘도 된다.
한 가지 유의할 점은 MySQL의 경우 단순 JOIN은 INNER JOIN으로 인지한다는 것이다.
*/

SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
LEFT JOIN ANIMAL_INS
ON ANIMAL_OUTS.ANIMAL_ID = ANIMAL_INS.ANIMAL_ID
WHERE ANIMAL_INS.ANIMAL_ID IS NULL
ORDER BY ANIMAL_ID;