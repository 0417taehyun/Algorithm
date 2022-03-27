-- [ LeetCode ] 1083. Sales Analysis II

SELECT DISTINCT buyer_id
FROM Sales
JOIN Product
ON (
    Sales.product_id = Product.product_id
    AND
    Product.product_name = "S8"
)
WHERE buyer_id NOT IN (
    SELECT buyer_id
    FROM Sales
    JOIN Product
    USING (product_id)
    WHERE product_name = "iPhone"
);


/*
아래와 같이 훨씬 간단하게 SUM 함수 내에 CASE 구를 사용하여 문제를 해결할 수도 있다.

GROUP BY 구를 통해 그룹화 되어있기 때문에 만약에 product_name 필드의 값이 `S8`일 경우 `1`로 취급하여 더하고 그렇지 않으면 `0`으로 취급하여,
그렇게 얻은 값들을 더해서 `S8`을 1회 이상 구매한 경우, 다시 말해 합산의 값이 `0`을 초과하는 경우만을 조건으로 한다.

마찬가지로 `iPhone`인 경우 `1`로 취급하여 더하고 그렇지 않으면 `0`으로 취급하여,
그렇게 얻은 값들을 더해서`iPhone`을 구매한 경우가 없는 경우, 다시 말해 합산의 값이 `0`인 경우만을 조건으로 한다.
*/

SELECT buyer_id
FROM Sales
JOIN Product
USING (product_id)
GROUP BY buyer_id
HAVING (
    SUM(CASE product_name WHEN "S8" THEN 1 ELSE 0 END) > 0
    AND
    SUM(CASE product_name WHEN "iPhone" THEN 1 ELSE 0 END) = 0
);