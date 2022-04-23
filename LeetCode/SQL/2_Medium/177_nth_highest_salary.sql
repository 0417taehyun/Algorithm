-- [ LeetCode ] 177. Nth Highest Salary

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      SELECT IF(COUNT(salary) <> N, null, MIN(salary))
      FROM (
          SELECT DISTINCT salary
          FROM Employee
          ORDER BY salary DESC
          LIMIT N
      ) AS Salaries
  );
END


/*
아래와 같이 DECLARE 및 SET 키워드를 활용하여 변수를 선언한 뒤 LIMIT 및 OFFSET 키워드를 이용해 레코드를 제한해서 문제를 해결할 수 있다.
이때 변수를 따로 선언한 이유는 LIMIT 및 OFFSET 키워드에서 사칙연산 표현을 사용할 수 없기 때문이다. 유의할 점은 OFFSET 키워드의 시작 값은 `0`이다.

추가적으로 함수의 경우 아무 것도 반환하지 않을 때 자동으로 NULL 값 처리가 되기 때문에 LIMIT 및 OFFSET 키워드를 활용할 수 있다.
빈 컬럼을 반환해도 자동적으로 NULL 값이 반환되기 때문이다.
*/

CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  DECLARE M INT;
  SET M = N - 1;
  
  RETURN (
      SELECT DISTINCT salary
      FROM Employee
      ORDER BY salary DESC
      LIMIT 1 OFFSET M
  );
END
