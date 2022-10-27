-- [ 프로그래머스 ] 가격이 제일 비싼 식품의 정보 출력하기

-- PRICE 컬럼의 값이 고유한지 물어보면 좋을 것 같다.

SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
FROM FOOD_PRODUCT
WHERE PRICE = (SELECT MAX(PRICE) FROM FOOD_PRODUCT);


/*
아래와 같이 ORDER BY 구 및 LIMIT 구를 활용해서 문제를 풀 수도 있다.
위 WHERE 구에 서브 쿼리를 사용한 예시의 경우 서브 쿼리가 PRICE 컬럼의 값을 비교할 때마다 수행이 되기 때문에 최적화의 어려움이 있다.
*/

SELECT
    PRODUCT_ID,
    PRODUCT_NAME,
    PRODUCT_CD,
    CATEGORY,
    PRICE
FROM FOOD_PRODUCT
ORDER BY PRICE DESC
LIMIT 1;
