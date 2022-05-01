-- [ LeetCode ] 1070. Product Sales Analysis III

SELECT
    Sales.product_id AS product_id,
    GroupedSales.first_year AS first_year,
    Sales.quantity AS quantity,
    Sales.price AS price
FROM Sales
JOIN (
    SELECT
        product_id,
        MIN(year) AS first_year
    FROM Sales
    GROUP BY product_id
) As GroupedSales
ON (
    Sales.product_id = GroupedSales.product_id
    AND
    Sales.year = GroupedSales.first_year
);


-- 아래와 같이 WHERE 구에 서브쿼리를 활용하여 문제를 해결할 수도 있다.

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM Sales
WHERE (product_id, year) IN (
    SELECT
        product_id,
        MIN(year)
    From Sales
    GROUP BY product_id
);


-- 아래와 같이 윈도우 함수(Window Function) 중 RANK 함수를 사용해서 문제를 해결할 수도 있다.

SELECT
    product_id,
    year AS first_year,
    quantity,
    price
FROM (
    SELECT
        product_id,
        year,
        RANK() OVER(PARTITION BY product_id ORDER BY year ASC) AS year_rank,
        quantity,
        price
    FROM Sales
) AS ProductFirstYear
WHERE year_rank = 1;
