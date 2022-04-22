-- [ LeetCode ] 1978. Employees Whose Manager Left the Company

/*
제출해서 여러 번 틀렸다.
JOIN 구 실행 이전에 조건문을 실행해야 하는지 아니면 그 전에 실행해야 하는지 잘 고민해봐야 할 것 같다.
해당 문제의 경우 JOIN 구 실행 이전에 조건문을 통해 데이터가 어느 정도 걸러져야 문제가 해결된다.
JOIN 구의 조건에 해당하는 ON 구 및 JOIN 구를 실행한 뒤에 적용되는 WHERE 구에 문제에서 요구하는 조건을 실행했어서 계속 틀렸다.
따라서 서브쿼리를 활용하여 FROM 구에서 먼저 조건에 의해 걸러진 테이블을 조회할 수 있게 하였다.
*/

SELECT Selected_Employees.employee_id AS employee_id
FROM (
    SELECT employee_id, manager_id
    FROM Employees
    WHERE (
        manager_id IS NOT NULL
        AND
        salary < 30000
    )
) AS Selected_Employees
LEFT JOIN Employees AS Managers
ON Selected_Employees.manager_id = Managers.employee_id
WHERE Managers.employee_id IS NULL
ORDER BY employee_id;


/*
아래와 같이 문제를 해결할 수도 있다.
굳이 JOIN 구를 사용하지 않고 WHERE 구의 조건으로 서브쿼리만 사용했기 때문에 훨씬 빠르다.
*/

SELECT
    employee_id
FROM Employees
WHERE (
    salary < 30000
    AND
    manager_id IS NOT NULL
    AND
    manager_id NOT IN (SELECT employee_id FROM Employees)
)
ORDER BY employee_id;
