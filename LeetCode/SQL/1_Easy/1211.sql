-- [ LeetCode ] 1211. Queries Quality and Percentage

SELECT
    query_name,
    ROUND(SUM((rating / position)) / COUNT(query_name), 2) AS quality,
    ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;


-- 아래와 같이 quality 필드 또한 SUM 함수가 아닌 AVG 함수를 사용할 수 있다.

SELECT
    query_name,
    ROUND(AVG(rating / position), 2) AS quality,
    ROUND(AVG(rating < 3) * 100, 2) AS poor_query_percentage
FROM Queries
GROUP BY query_name;