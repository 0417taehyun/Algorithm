-- [ LeetCode ] 1050. Actors and Directors Who Cooperated At Least Three Times

/*
다른 풀이 중에 COUNT(1)을 사용한 풀이가 존재했다.
COUNT(*) 표현과 COUNT(1) 표현은 둘 다 MySQL의 데이터베이스 엔진 중 하나인 InnoDB 내에서 동일하게 작동한다.
다만 COUNT(*) 표현의 경우 NULL 값을 포함하여 수를 세는데, `1`은 일종의 상수 역할을 하여 NULL 값이 아닌 모든 경우를 의미한다.

이때 InnoDB는 트랜잭션을 지원해서 트랜잭션 세이프 스토리지 엔진이라고도 부르며 MySQL에서 기본적으로 사용되고 있는 엔진이다.
다른 스토리지 엔진의 종류에는 MyISAM도 존재하는데 작성(Write)보다는 조회(Read)에 특화된 엔진이다.
*/

SELECT actor_id, director_id
FROM ActorDirector
GROUP BY actor_id, director_id
HAVING COUNT(director_id) >= 3;