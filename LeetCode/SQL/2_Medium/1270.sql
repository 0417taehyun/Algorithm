-- [ LeetCode ] 1270. All People Report to the Given Manager

/*
처음에 문제를 해결하지 못해서 다른 사람의 풀이를 확인했다.
JOIN 구를 통해서 결합할 때 점점 결합의 깊이가 깊어질 수록 보스, 다시 말해 employee_id 필드의 값이 `1`인 경우에 가까워진다고 생각하면 된다.
문제에서 요구한 조건은 결국 3번을 초과하지 않고 보스와 연결되는 경우이기 때문에 JOIN 구를 두 번만 결합하고 마지막 결합되는 경우가 직접적으로 보스와 연결되는 경우면 된다.
*/

SELECT Employees.employee_id
FROM Employees
JOIN Employees AS FirstDepth
ON Employees.manager_id = FirstDepth.employee_id
JOIN Employees AS SecondDepth
ON FirstDepth.manager_id = SecondDepth.employee_id
WHERE (
    Employees.employee_id <> 1
    AND
    SecondDepth.manager_id = 1
);


/*
아래와 같이 WITH RECURSIVE 구를 통해 확장성 있게 문제를 해결할 수도 있다.
WITH RECURSIVE 구를 사용할 경우 레코드가 더이상 연산이 안 되면 자동으로 WITH RECUSRIVE 구를 빠져 나온다.

UNION ALL 키워드 -또는 UNION 키워드- 를 기준으로 수직 결합되는 밑부분이 재귀적으로 실행 부분이다.
예를 들어 주어진 테이블이 아래와 같다고 가정해보자.

+-------------+---------------+------------+
| employee_id | employee_name | manager_id |
+-------------+---------------+------------+
| 1           | Boss          | 1          |
| 3           | Alice         | 3          |
| 2           | Bob           | 1          |
| 4           | Daniel        | 2          |
| 7           | Luis          | 4          |
| 8           | Jhon          | 3          |
| 9           | Angela        | 8          |
| 77          | Robert        | 1          |
+-------------+---------------+------------+

처음 UNION ALL 키워드 윗부분에 실행된 결과 테이블은 아래와 같다.

+-------------+-------+
| employee_id | depth |
+-------------+-------+
| 2           | 1     |
| 77          | 1     |
+-------------+-------+

다음부터 UNION ALL 키워드 밑부분에 재귀적으로 실행되는 첫 번째 결과 테이블은 아래와 같다.
cte 테이블의 employee_id 필드의 값과 Employees 테이블의 manager_id 필드의 값이 같은 경우다.
다시 말해 직접적으로 employee_id 필드의 값이 `1`인 경우와 연결되어 있는 레코드와 연결되어 있는 레코드들이다.

+-------------+-------+
| employee_id | depth |
+-------------+-------+
| 2           | 1     |
| 77          | 1     |
| 4           | 2     |
+-------------+-------+

다음으로 다시 재귀적으로 반복되며 이때 depth 필드의 값이 하나 더 상승한다.
그리고 위 예시 데이터를 기준으로는 더이상 재귀적으로 수행해야 할 값이 없기 때문에 연산을 종료하고 최종적으로 아래 테이블을 반환한다.

+-------------+-------+
| employee_id | depth |
+-------------+-------+
| 2           | 1     |
| 77          | 1     |
| 4           | 2     |
| 7           | 3     |
+-------------+-------+

만약 manager_id 필드의 값이 `7`인 경우의 레코드가 추가로 존재할 경우 아래와 같이 해당 레코드가 추가된 테이블이 결과로 반환된다.

+-------------+-------+
| employee_id | depth |
+-------------+-------+
| 2           | 1     |
| 77          | 1     |
| 4           | 2     |
| 7           | 3     |
| 5           | 4     |
+-------------+-------+

결과적으로 연산은 계층에 의해 결국 종료되기 때문에 실제 이를 조회하는 부분에서 WHERE 구를 활용해 확장성 있는 쿼리를 작성할 수 있다.
만약 최대 3명이 아닌 5명일 경우 단순히 WHERE 구의 정수값을 `3`이 아닌 `5`로 바꿔주면 되기 때문이다.
*/

WITH RECURSIVE cte (employee_id, depth) AS (
	SELECT
		Employees.employee_id,
		1 AS depth
	FROM Employees
	WHERE (
		Employees.employee_id <> 1
		AND
		Employees.manager_id = 1
	)
	UNION ALL
	SELECT
		SubEmployees.employee_id,
		cte.depth + 1 AS depth
	FROM cte
	JOIN Employees AS SubEmployees
	ON cte.employee_id = SubEmployees.manager_id
)

SELECT employee_id
FROM cte
WHERE depth <= 3;
