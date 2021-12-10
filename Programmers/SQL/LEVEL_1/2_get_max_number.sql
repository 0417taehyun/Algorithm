-- [ 프로그래머스 ] 최댓값 구하기

SELECT MAX(DATETIME) AS '시간' FROM ANIMAL_INS;


-- 아래와 같이 DATETIME 열을 기준으로 오름차순 정렬한 다음 제일 처음 행만 반봔하는 방법도 있다.

SELECT DATETIME AS '시간'
FROM ANIMAL_INS
ORDER BY DATETIME DESC
LIMIT 1;