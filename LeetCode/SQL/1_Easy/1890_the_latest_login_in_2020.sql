-- [ LeetCode ] 1890. The Latest Login in 2020

-- MAX 함수는 날짜 형식의 포맷에 대해서도 원활하게 작동한다.

SELECT
    user_id,
    MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;


/*
아래와 같이 Window Function을 활용해서 문제를 해결할 수도 있다.
FIRST_VALUE 함수는 가장 첫 번째 값을 반환하는데 user_id 필드를 기준으로 묶고,
time_stamp 필드를 기준으로 내림차순 정렬하면 결국 가장 큰 값을 얻을 수 있다.
*/

SELECT
    DISTINCT user_id,
    FIRST_VALUE(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp DESC) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = '2020';