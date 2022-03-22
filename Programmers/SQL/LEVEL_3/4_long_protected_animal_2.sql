-- [ 프로그래머스 ] 오랜 기간 보호한 동물(2)

/*
INNER JOIN 대신 JOIN을 사용해도 된다. MySQL에서 JOIN은 INNER JOIN으로 취급하기 때문이다.
내부결합이기 때문에 정확히 ANIMAL_INS 값이 일치하는 경우, 다시 말해 ANIMAL_OUTS에 존재하는 ANIMAL_INS 값만 추출이 된다.

추가적으로 ORDER BY의 기본값은 오름차순으로 ASC 키워드가 붙어져 있고, 만약 내림차순을 원할 경우 끝에 DESC를 붙여주면 된다.
*/

SELECT ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
FROM ANIMAL_OUTS
INNER JOIN ANIMAL_INS
USING (ANIMAL_ID)
ORDER BY (ANIMAL_OUTS.DATETIME - ANIMAL_INS.DATETIME) DESC
LIMIT 2;