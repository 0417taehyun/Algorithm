-- [ LeetCode ] 1350. Students With Invalid Departments

SELECT
    Students.id AS id,
    Students.name AS name
FROM Students
LEFT JOIN Departments
ON (Students.department_id = Departments.id)
WHERE Departments.name IS NULL
ORDER BY id;


/*
아래와 같이 문제를 해결할 수도 있지만 데이터가 많을 수록 훨씬 느릴 수밖에 없다.
SELECT 구를 통해서 얻게 된 `id` 값들에 대해 연속적으로 비교를 해야 하기 때문이다.
*/

SELECT id, name
FROM Students
WHERE department_id NOT IN (SELECT id FROM Departments)
ORDER BY id;