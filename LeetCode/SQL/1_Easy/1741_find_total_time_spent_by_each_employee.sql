-- [ LeetCode ] 1741. Find Total Time Spent by Each Employee

SELECT
    event_day AS day,
    emp_id,
    SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day;


/*
아래와 같이 GROUP BY 구를 사용하지 않더라도 윈도우 함수(Window Function)를 활용하여 문제를 해결할 수도 있다.
이때 OVER 표현식 내부에 PARTITION BY 부분에 해당 함수가 어떤 필드를 토대로 그룹핑 되어야 하는지 지정해줄 수 있다.
*/
SELECT
    DISTINCT event_day AS day,
    emp_id,
    SUM(out_time - in_time) OVER(PARTITION BY emp_id, event_day) AS total_time
FROM Employees;