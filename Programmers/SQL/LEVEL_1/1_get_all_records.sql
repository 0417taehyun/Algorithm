-- [ 프로그래머스 ] 모든 레코드 조회하기

SELECT * FROM ANIMAL_INS ORDER BY ANIMAL_ID;


-- 아래와 같이 GROUP BY를 사용할 수도 있다. 그러나 성능을 위해 ORDER BY 명령이 자동으로 삭제될 수 있다.

SELECT animal.*
FROM (
    SELECT *
    FROM ANIMAL_INS
    ORDER BY ANIMAL_INS.ANIMAL_ID
) AS animal
GROUP BY animal.ANIMAL_ID;

-- 따라서 서브쿼리 내의 ORDER BY 명령이 정상적으로 작동하게 하기 위해 아래와 같이 LIMIT 키워드를 사용하여 LIMIT 키워드의 최댓값으로 제한해준다.

SELECT animal.*
FROM (
    SELECT *
    FROM ANIMAL_INS
    ORDER BY ANIMAL_INS.ANIMAL_ID
    LIMIT 18446744073709551615
) AS animal
GROUP BY animal.ANIMAL_ID;