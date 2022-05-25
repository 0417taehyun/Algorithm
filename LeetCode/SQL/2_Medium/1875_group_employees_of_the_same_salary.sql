-- [ LeetCode ] 1875. Group Employees of the Same Salary

SELECT
    employee_id,
    name,
    Employees.salary,
    DENSE_RANK() OVER(ORDER BY Employees.salary ASC) AS team_id
FROM Employees
JOIN (
    SELECT salary
    FROM Employees
    GROUP BY salary
    HAVING COUNT(employee_id) >= 2
) AS GroupedEmployees
USING (salary)
ORDER BY team_id ASC, employee_id ASC;


/*
처음에 위와 같이 문제를 풀었는데 JOIN 구 때문에 성능이 그리 좋지 않았다.
아래와 같이 JOIN 구가 아닌 서브쿼리를 활용하여 내부에 COUNT 윈도우 함수(Window Function)를 써서 문제를 해결할 수 있다.

COUNT 윈도우 함수의 경우 누적인 줄 알고 수가 점점 커지는 개념으로 생각했는데
윈도우 함수가 결국 모든 조작이 끝난 테이블에 대해 실행하는 함수이기 때문에 PARTITION BY 구를 통해 묶인 행에서의 개수를 센다.
그래서 그 결괏값은 동일한 PARTITION BY 구에 대해서는 전부 값이 같다.
*/

SELECT
    employee_id,
    name,
    salary,
    DENSE_RANK() OVER(ORDER BY salary ASC) AS team_id
FROM (
    SELECT
        employee_id,
        name,
        salary,
        COUNT(employee_id) OVER(PARTITION BY salary) AS member_count
    FROM Employees
) AS MemberCounts
WHERE member_count >= 2
ORDER BY team_id ASC, employee_id ASC;
