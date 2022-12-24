-- [ LeetCode ] 579. Find Cumulative Salary of an Employee

/*
문제를 풀 때 유의해야 할 점은 JOIN 구 다음에 WHERE 구를 사용해야 한다는 것이다.
그리고 GROUP BY 구는 WHERE 구 다음에 위치한다.
*/

SELECT
    RecentMonths.id,
    RecentMonths.month,
    SUM(Employee.salary) AS Salary
FROM (
    SELECT
        id,
        month,
        salary,
        MAX(month) OVER(PARTITION BY id) AS recent_month
    FROM Employee
) AS RecentMonths
JOIN Employee
ON (
    RecentMonths.id = Employee.id
    AND
    (RecentMonths.month - Employee.month) BETWEEN 0 AND 2
)
WHERE RecentMonths.month <> RecentMonths.recent_month
GROUP BY RecentMonths.id, RecentMonths.month
ORDER BY id ASC, month DESC;
