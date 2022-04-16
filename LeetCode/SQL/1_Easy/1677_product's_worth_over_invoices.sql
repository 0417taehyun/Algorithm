-- [ LeetCode ] 1677. Product's Worth Over Invoices

/*
문제를 처음 풀 때 Product 테이블에는 존재하는 제품이 Invoice 테이블에 존재하지 않는 경우를 고려해야 한다고 생각해서
단순히 SUM 함수만 사용하는 게 아니라 IFNULL 함수를 함께 사용하였고 JOIN 구 또한 INNER JOIN 구가 아닌 OUTER JOIN 구를 떠올렸다.
그러나 JOIN 구의 기준이 되는 대상을 Invoice 테이블이 아닌 Product 테이블로 했어야 Product 테이블에 존재하지만 Invoice 테이블에 존재하지 않는 제품에 대해 NULL 값 처리를 해줄 수 있었는데,
RIGHT JOIN 구가 아닌 LEFT JOIN 구를 사용하여 처음에 문제를 틀렸었다.

문제의 제약 조건 등에 대해서 고민을 해본 것은 무척 좋았지만 앞으로 JOIN 구를 사용할 때는 그 방향에 대해 잘 생각해봐야갰다.
NULL 값을 얻고 싶은 곳으로 향해서 JOIN 구를 사용해야 한다.
*/

SELECT
    name,
    SUM(IFNULL(rest, 0)) AS rest,
    SUM(IFNULL(paid, 0)) AS paid,
    SUM(IFNULL(canceled, 0)) AS canceled,
    SUM(IFNULL(refunded, 0)) AS refunded
FROM Invoice
RIGHT JOIN Product
USING (product_id)
GROUP BY product_id
ORDER BY name;