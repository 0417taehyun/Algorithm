-- [ LeetCode ] 595. Big Countries

/*
실제 정답에서는 UNION을 사용한 방법이 훨씬 빨랐는데 이는 테이블 및 필드의 크기에 따라서 달라지기 때문이다.
UNION의 경우 UNION ALL과 달리 내부적으로 DISTINCT 문법을 실행하기 때문에 때에 따라서 느릴 수 있다.
*/

SELECT
    name,
    population,
    area
FROM World
WHERE (
    area >= 3000000
    OR
    population >= 25000000
);