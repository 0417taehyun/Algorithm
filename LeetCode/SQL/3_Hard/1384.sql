-- [ LeetCode ] 1384. Total Sales Amount by Year

/*
CAST 함수, 그리고 YEAR 함수 대신 DATE_FORMAT 함수를 사용한 이유는 문제에서 해당 값들을 문자열로 받길 원했기 때문이다.
문제를 해결하는데 YearsPoints 테이블을 생각하는 게 조금 오래 걸렸다.

추가적으로 DATEDIFF 함수의 경우 두 날짜의 차이를 반환하는 함수이기 때문에 해당 두 날짜감 모두 포함된 결괏값을 원할 경우 따로 `1`을 더해줘야 한다는 걸 잊지 말아야겠다.
*/

SELECT
    CAST(Product.product_id AS CHAR) AS product_id,
    Product.product_name,
    DATE_FORMAT(start_date, "%Y") AS report_year,
    average_daily_sales * (DATEDIFF(
        IF(YearsPoints.end_date <= Sales.period_end, YearsPoints.end_date, Sales.period_end),
        IF(YearsPoints.start_date >= Sales.period_start, YearsPoints.start_date, Sales.period_start)
    ) + 1) AS total_amount
FROM Product
JOIN Sales
USING (product_id)
JOIN (
    SELECT '2018-01-01' AS start_date, '2018-12-31' AS end_date
    UNION ALL
    SELECT '2019-01-01', '2019-12-31'
    UNION ALL
    SELECT '2020-01-01', '2020-12-31'
) AS YearsPoints
ON YEAR(YearsPoints.start_date) BETWEEN YEAR(Sales.period_start) AND YEAR(Sales.period_end)
GROUP BY Product.product_id, YEAR(YearsPoints.start_date)
ORDER BY product_id ASC, report_year ASC;


/*
아래와 같이 WITH RECURSIVE 구에서 period_start 필드 및 period_end 사이에 있는 모든 sale_date 필드를 구하여 확장성 있는 쿼리를 만들 수 있다.
이렇게 할 경우 이전 풀이와 다르게 연도가 유동적으로 주어지더라도 해결 가능하기 때문이다.
*/

WITH RECURSIVE cte (product_id, sale_date) AS (
    SELECT
        product_id,
        period_start AS sale_date
    FROM Sales
    UNION ALL
    SELECT
        product_id,
        DATE_ADD(sale_date, INTERVAL 1 DAY) AS sale_date
    FROM cte
    WHERE sale_date < (SELECT period_end FROM Sales WHERE cte.product_id = Sales.product_id)
)

SELECT 
    CAST(Product.product_id AS CHAR) AS product_id,
    Product.product_name,
    DATE_FORMAT(cte.sale_date, "%Y") AS report_year,
    SUM(average_daily_sales) AS total_amount
FROM Product
JOIN Sales
USING (product_id)
JOIN cte
USING (product_id)
GROUP BY Product.product_id, report_year
ORDER BY product_id ASC, report_year ASC;
