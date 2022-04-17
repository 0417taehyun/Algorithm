-- [ LeetCode ] 1777. Product's Price for Each Store

/*
아래와 같이 WITH 구를 활용하여 문제를 풀었다.
CASE 구의 조건을 통해 조건을 만족하지 못할 경우 NULL 값이 반환되고 SUM 함수는 NULL 값을 따로 변환하지 않고 처리하기 때문에
NULL 값으로만 이루어진 값들을 합산할 경우 그 결괎값으로 NULL 값을 반환한다.
*/

WITH cte (product_id, store1, store2, store3) AS (
    SELECT
        product_id,
        SUM(CASE WHEN store = "store1" THEN price END) AS store1,
        SUM(CASE WHEN store = "store2" THEN price END) AS store2,
        SUM(CASE WHEN store = "store3" THEN price END) AS store3
    FROM Products
    GROUP BY product_id
)

SELECT *
FROM cte;

SELECT


/*
물론 WITH 구를 사용하지 않더라도 아래와 같이 문제를 해결할 수 있다.
CASE 구 대신 IF 구를 사용하여 만약 해당 조건에 알맞지 않으면 NULL 값을 반환하게 하였다.
*/

SELECT
    product_id,
    SUM(IF(store="store1", price, null)) AS store1,
    SUM(IF(store="store2", price, null)) AS store2,
    SUM(IF(store="store3", price, null)) AS store3
FROM Products
GROUP BY product_id;
