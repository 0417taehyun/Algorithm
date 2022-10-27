-- [ 프로그래머스 ] 우유와 요거트가 담긴 장바구니

-- INNER JOIN 내부에 WHERE 구와 바깥 WHERE 구를 통해 조건을 걸어 문제를 풀었다.

SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
JOIN (
    SELECT CART_ID
    FROM CART_PRODUCTS
    WHERE NAME = "Yogurt"
) AS JOINED_TABLE
USING (CART_ID)
WHERE NAME = "Milk";


-- WHERE 구 내부에 서브쿼리를 사용하여 문제를 풀 수도 있다.

SELECT DISTINCT CART_ID
FROM CART_PRODUCTS
WHERE (
    CART_ID IN (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = "Milk"
    )
    AND
    CART_ID IN (
        SELECT CART_ID
        FROM CART_PRODUCTS
        WHERE NAME = "Yogurt"
    )
);