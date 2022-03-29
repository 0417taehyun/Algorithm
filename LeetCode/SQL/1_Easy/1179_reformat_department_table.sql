-- [ LeetCode ] 1179. Reformat Department Table

/*
`month` 필드가 primary key이기 때문에 SUM 함수 대신 MAX 함수를 써도 해결 가능하다.

처음에 새로운 컬럼을 어떻게 생성해서 만들 수 있을지 고민했는데,
만약에 결괏값이 없을 경우 자동으로 NULL 값이 대입되기 때문에 SELECT 구에서 차례로 나열해서 생성할 수 있다.
*/

SELECT
    id,
    SUM(IF(month="Jan", revenue, null)) AS Jan_Revenue,
    SUM(IF(month="Feb", revenue, null)) AS Feb_Revenue,
    SUM(IF(month="Mar", revenue, null)) AS Mar_Revenue,
    SUM(IF(month="Apr", revenue, null)) AS Apr_Revenue,
    SUM(IF(month="May", revenue, null)) AS May_Revenue,
    SUM(IF(month="Jun", revenue, null)) AS Jun_Revenue,
    SUM(IF(month="Jul", revenue, null)) AS Jul_Revenue,
    SUM(IF(month="Aug", revenue, null)) AS Aug_Revenue,
    SUM(IF(month="Sep", revenue, null)) AS Sep_Revenue,
    SUM(IF(month="Oct", revenue, null)) AS Oct_Revenue,
    SUM(IF(month="Nov", revenue, null)) AS Nov_Revenue,
    SUM(IF(month="Dec", revenue, null)) AS Dec_Revenue
FROM Department
GROUP BY id;