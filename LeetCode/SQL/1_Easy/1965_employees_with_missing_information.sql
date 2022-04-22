-- [ LeetCode ] 1965. Employees With Missing Information

/*
아래와 같이 UNION 키워드를 사용하여 문제를 해결할 수 있다.
이때 중요한 건 ORDER BY 키워드의 경우 결국 SELECT 구가 끝난 다음에 실행이 되기 때문에 가장 마지막에 작성해줘야 한다는 것이다.
추가적으로 중복을 관리해줘야 하기 때문에 UNION ALL 키워드가 아닌 UNION 키워드를 사용하였다.
*/

SELECT
    employee_id
FROM Employees
LEFT JOIN Salaries
USING (employee_id)
WHERE Salaries.employee_id IS NULL
UNION
SELECT
    employee_id
FROM Salaries
LEFT JOIN Employees
USING (employee_id)
WHERE Employees.employee_id IS NULL
ORDER BY employee_id;


-- 아래와 같이 서브쿼리에 UNION 키워드를 사용하여 해결할 수도 있다.

SELECT
    Integrations.employee_id AS employee_id
FROM (
    SELECT *
    FROM Employees
    LEFT JOIN Salaries
    USING (employee_id)
    UNION
    SELECT *
    FROM Employees
    RIGHT JOIN Salaries
    USING (employee_id)
) AS Integrations
WHERE (
    Integrations.name IS NULL
    OR
    Integrations.salary IS NULL
)
ORDER BY employee_id;


/*
물론 훨씬 간단하게는 굳이 JOIN 구를 사용하지 않더라도 WHERE 구에 서브쿼리 및 NOT IN 구를 사용하여 문제를 해결할 수 있다.
그러나 테이블 내에서 employee_id 필드가 기본 키(Primary Key)이기 때문에 인덱스가 저장되어 있을 것이고
WHERE ... NOT IN ... 구를 사용할 경우 결국 WHERE 구에서 서브쿼리에 대한 결괏값에 하나씩 대응하여 결과를 반환해야 하기 때문에
JOIN 구를 사용한 방법과 비교했을 때 훨씬 느릴 것으로 예상했다.
*/

SELECT
    employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT
    employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;
