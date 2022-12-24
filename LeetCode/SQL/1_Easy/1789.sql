-- [ LeetCode ] 1789. Primary Department for Each Employee

SELECT
    employee_id,
    IF(COUNT(department_id) > 1, MAX(IF(primary_flag='Y', department_id, 0)), department_id) AS department_id
FROM Employee
GROUP BY employee_id;


-- 아래와 같이 서브쿼리를 활용하여 문제를 해결할 수도 있다.

SELECT
    employee_id,
    department_id
FROM Employee
WHERE (
    primary_flag = 'Y'
    OR
    employee_id IN (SELECT employee_id FROM Employee GROUP BY employee_id HAVING COUNT(department_id) = 1)
);