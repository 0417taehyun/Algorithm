-- [ 프로그래머스 ] 동명 동물 수 찾기

/*
쿼리 실행 순서는 WHERE > GROUP BY > HAVING > SELECT > ORDER BY 순서이다.

또한 COUNT 횟수가 2회 이상인 결괏값을 얻기 위해서는 HAVING 절에서 사용해야 하는데
COUNT, SUM 등의 집계함수는 GROUP BY 이후에 사용이 가능하기 때문에 WHERE 절에서 사용 불가능하기 때문이다.

추가적으로 COUNT 집계함수는 자동으로 NULL 값을 제외하여 연산하기 때문에 NULL 값이 아닌 경우에 대한 별도의 조건을 지정해주지 않아도 된다.
*/

SELECT NAME, COUNT(NAME) AS "COUNT"
FROM ANIMAL_INS
GROUP BY NAME
HAVING COUNT(NAME) >= 2
ORDER BY NAME;