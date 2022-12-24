-- [ LeetCode ] 1767. Find the Subtasks That Did Not Execute

/*
결과적으로 아래와 같이 문제를 풀었지만 INNER JOIN 구가 작동하지 않을 것 같았다.
WITH RECURSIVE 구를 통해 만든 Subtasks 테이블의 subtask_id 필드 기준이 될 Tasks 테이블의 subtasks_count 필드를 어떤 것과 비교해야 할 지 모를 것 같았기 때문이다.
그런데 생각해보면 일반적인 JOIN 구의 문법 또한 결국 기준이 되는 테이블을 전부 순회하며 조건에 맞을 경우 수평 결합을 하는 형태기 때문에 문제 없었다.
*/

WITH RECURSIVE Subtasks (subtask_id) AS (
    SELECT 1 AS subtask_id
    UNION ALL
    SELECT subtask_id + 1
    FROM Subtasks
    WHERE subtask_id BETWEEN 1 AND 19
)

SELECT
    Tasks.task_id,
    Subtasks.subtask_id
FROM Tasks
JOIN Subtasks
ON Tasks.subtasks_count >= Subtasks.subtask_id
LEFT JOIN Executed
ON (
    Tasks.task_id = Executed.task_id
    AND
    Subtasks.subtask_id = Executed.subtask_id
)
WHERE Executed.subtask_id IS NULL;
