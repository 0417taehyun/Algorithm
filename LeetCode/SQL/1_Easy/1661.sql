-- [ LeetCode ] 1661. Average Time of Process per Machine

/*
처음에 문제를 풀 때 activity_type 필드의 값이 `start`인 경우만 있고 `end`인 경우가 없는 process_id 필드의 레코드,
다시 말해 프로세스를 시작했는데 아직 종료되지 않은 경우를 제외하고 평균 값을 계산해야 할 것 같아서 아래와 같이 HAVING 구에 조건을 걸었다.
machine_id 필드 및 process_id 필드는 기본 키(Primary Key)이기 때문에 만약 process_id 필드에 대해 COUNT 함수를 실행했을 때 `2`가 아니라면 프로세스가 종료되지 않은 경우기 때문이다.
물론 문제에 해당 제약 조건을 어떻게 처리해야 하는지 따로 작성되지 않았기 때문에 무조건 종료까지 된 프로세스에 대한 것만 테이블에 기록되는 것 같았다.
하지만 실제 인터뷰 등에서는 해당 제약조건에 대해 고민하고 묻는 것이 좋을 것 같다.

추가적으로 SUM 함수 부분의 경우 아래와 같이 더 간단하게 표현할 수 있다.

SUM(IF(activity_type="end", timestamp, -timestamp))
*/
SELECT
    machine_id,
    ROUND(AVG(timestamp), 3) AS processing_time
FROM (
    SELECT
        machine_id,
        SUM(IF(activity_type="end", timestamp, 0)) - SUM(IF(activity_type="start", timestamp, 0)) AS timestamp
    FROM Activity
    GROUP BY machine_id, process_id
    HAVING COUNT(process_id) = 2
) AS Activity_Time
GROUP BY machine_id;


/*
다른 사람의 풀이를 참조했는데 굳이 서브쿼리를 사용하지 않더라도 아래와 같이 INNER JOIN 구를 통해 문제를 해결할 수 있었다.
process_id 필드의 값이 동일하고 각 테이블의 acitivity_type 필드의 값이 `"end"` 및 `"start"`인 경우를 INNER JOIN 구의 조건으로 한다면
자동으로 종료가 되지 않은 프로세스, 다시 말해 activity_type 필드의 값에 `"end"`가 존재하지 않는 레코드는 `NULL` 값이라 대상에서 제외되기 때문이다.
아래와 같은 방식이 속도도 훨씬 빨랐다.
*/

SELECT
    Activity_End.machine_id AS machine_id,
    ROUND(AVG(Activity_End.timestamp - Activity_Start.timestamp), 3) AS processing_time
FROM Activity AS Activity_End
JOIN Activity AS Activity_Start
ON (
    Activity_End.machine_id = Activity_Start.machine_id
    AND
    Activity_End.process_id = Activity_Start.process_id
    AND
    Activity_End.activity_type = "end"
    AND
    Activity_Start.activity_type = "start"
)
GROUP BY Activity_End.machine_id;