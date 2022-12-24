-- [ LeetCode ] 1795. Rearrange Products Table

-- 아래와 같이 WITH 구를 사용하여 문제를 풀었다.

WITH cte (product_id, store, price) AS (
    SELECT
        product_id,
        'store1' AS store,
        store1 AS price
    FROM Products
    UNION
    SELECT
        product_id,
        'store2' AS store,
        store2 AS price
    FROM Products
    UNION
    SELECT
        product_id,
        'store3' AS store,
        store3 AS price
    FROM Products    
)

SELECT *
FROM cte
WHERE price IS NOT NULL
ORDER BY product_id;


/*
아래와 같이 굳이 WITH 구를 사용하지 않더라도 문제를 해결할 수 있다.
MySQL에는 UNPIVOT 구가 따로 존재하지 않아서 이를 해결하기 위해 UNION ALL 키워드를 사용해야 한다.
UNION 키워드와 UNION ALL 키워드의 차이점은 UNION 키워드의 경우 중복을 제거하고 UNION ALL 키워드의 경우 중복을 제거하지 않는다는 점이다.
따라서 해당 문제는 중복에 대한 부분을 딱히 걱정할 필요가 없기 때문에 퍼포먼스를 위해 UNION ALL 키워드를 사용해주는 게 좋다.
*/

SELECT
    product_id,
    'store1' AS store,
    store1 AS price
FROM Products
WHERE store1 IS NOT NULL
UNION ALL
SELECT
    product_id,
    'store2' AS store,
    store2 AS price
FROM Products
WHERE store2 IS NOT NULL
UNION ALL
SELECT
    product_id,
    'store3' AS store,
    store3 AS price
FROM Products
WHERE store3 IS NOT NULL
ORDER BY product_id;