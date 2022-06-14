-- [ LeetCode ] 2298. Tasks Count in the Weekend

/*
처음에 GROUP BY IF(DAYNAME(submit_date) IN ('Saturday', 'Sunday'), 'weekend', 'working days') 같은 표현을 통해
주말과 평일을 나누어 묶은 다음 계산하려 했는데 생각해보니 하나의 행만 반환해야 하기 때문에 GROUP BY 구를 사용하면 안 된다.
GROUP BY 구는 결국 'weekend' 값과 'working days' 값 두 가지의 경우에 대해 나누어 SELECT 구를 실행하여 두 개의 행을 반환하기 때문이다.
따라서 아래와 같이 문제를 해결할 수 있다.

한 가지 궁금한 점은 submit_date 필드의 값에 NULL 값이 올 수 있는 지에 대한 여부였는데 관련해서는 이번 문제에서 따로 다루지 않는 것 같았다.
작업 처리에 대한 요청이 들어갔지만 정상적으로 제출되지 않은 경우에 대해서도 고민한 것이다.
그런데 이를 위해서는 task_date 필드도 따로 추가가 되어 있어야 좀 더 재미있는 문제가 만들어질 것 같다.
*/

SELECT
    COUNT(IF(DAYNAME(submit_date) IN ('Saturday', 'Sunday'), submit_date, NULL)) AS weekend_cnt,
    COUNT(IF(DAYNAME(submit_date) NOT IN ('Saturday', 'Sunday'), submit_date, NULL)) AS working_cnt
FROM Tasks;
