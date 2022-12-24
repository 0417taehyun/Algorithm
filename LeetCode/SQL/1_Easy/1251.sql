-- [ LeetCode ] 1251. Average Selling Price

SELECT
    Prices.product_id AS product_id,
    ROUND(SUM(price * units) / SUM(units), 2) AS average_price
FROM Prices
JOIN UnitsSold
ON (
    Prices.product_id = UnitsSold.product_id
    AND
    UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
)
GROUP BY product_id;


/*
위와 같이 INNER JOIN을 사용해서 문제를 해결해도 모든 테스트 케이스를 통과하기는 한다.
하지만 누군가 Prices 테이블에는 존재하는 product_id 값이 있는데 아직 팔라지 않아서 UnitsSold 테이블에는 존재하지 않는 경우의 수에 관해 질문했다.

테스트 케이스를 생각할 때, 특히 JOIN 구를 활용하여 문제를 해결할 때는 INNER JOIN을 사용할 것인지 LEFT JOIN을 사용할 것인지 신중해야 할 것 같다.
만약 질문처럼 아직 팔리지 않는 제품이 존재할 경우 SELECT 구에 IF 조건문과 더불어 JOIN 또한 INNER JOIN이 아닌 LEFT JOIN을 사용해여 아래와 같이 문제를 해결할 수 있다.
*/

SELECT
    Prices.product_id AS product_id,
    IF(
        SUM(units) IS NOT NULL,
        ROUND(SUM(price * units) / SUM(units), 2),
        0
    ) AS average_price
FROM Prices
LEFT JOIN UnitsSold
ON (
    Prices.product_id = UnitsSold.product_id
    AND
    UnitsSold.purchase_date BETWEEN Prices.start_date AND Prices.end_date
)
GROUP BY product_id;