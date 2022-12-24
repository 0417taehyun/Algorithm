-- [ LeetCode ] 1084. Sales Analysis III

SELECT
    product_id,
    product_name
FROM Product
WHERE product_id NOT IN (
    SELECT Product.product_id
    FROM Sales
    JOIN Product
    USING (product_id)
    WHERE sale_date NOT BETWEEN "2019-01-01" AND "2019-03-31"
);


/*
아래와 같이 GROUP BY를 사용하여 문제를 해결할 수도 있다.
`product_id` 필드를 기준으로 그룹화하여 여러 `sale_date` 필드의 값들 중 최소 값과 최대 값 모두 2019년 봄 내에 있어야 유효한 값이다.
*/

SELECT product_id, product_name
FROM Sales
JOIN Product
USING (product_id)
GROUP BY product_id
HAVING (
    MIN(sale_date) >= "2019-01-01"
    AND
    MAX(sale_date) <= "2019-03-31"
);