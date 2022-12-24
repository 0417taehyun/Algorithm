-- [ LeetCode ] 1285. Find the Start and End Number of Continuous Ranges

/*
연속되는 숫자 관련 문제가 나올 경우 ROW_NUMBER 윈도우 함수(Window Function)를 사용하여
필드와 해당 행 번호의 차이가 동일한 경우를GROUP BY 구를 사용해 그룹화하는 방법을 떠올려보자.
*/

SELECT
    MIN(log_id) AS start_id,
    MAX(log_id) AS end_id
FROM (
    SELECT
        log_id,
        log_id - ROW_NUMBER() OVER(ORDER BY log_id) AS diff
    FROM Logs
) AS LogsDiff
GROUP BY diff
ORDER BY start_id;
