-- [ LeetCode ] 1571. Warehouse Manager

SELECT
    name AS warehouse_name,
    SUM(volume * units) AS volume
FROM Warehouse
LEFT JOIN (
    SELECT
        product_id,
        Width * Length * Height AS volume
    FROM Products
) AS Products_Volume
USING (product_id)
GROUP BY name;


/*
아래와 같이 문제를 해결할 수도 있다.
문제에 "Inventory Occupies"라고 작성되어 있었기 때문에 LEFT JOIN 구를 사용할 필요 없이 INNER JOIN 구를 사용해도 된다.
LEFT JOIN 구를 사용할 경우 NULL 값이 반환되기 때문에 이를 한번 더 처리하는 과정에서 조금 더 느릴 수밖에 없다.
*/

SELECT
    name AS warehouse_name,
    SUM(units * Width * Length * Height) AS volume
FROM Warehouse
JOIN Products
USING (product_id)
GROUP BY name;
