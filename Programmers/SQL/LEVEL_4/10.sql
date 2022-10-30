-- [ 프로그래머스 ] 오프라인/온라인 판매 데이터 통합하기

/*
UNION 구에 대해서는 WHERE 구가 전체에 대해 적용되지 않기 때문에 각각 사용해주거나
아래와 같이 서브쿼리를 통해 새로운 중간 테이블을 생성해야 한다.
*/

SELECT SALES_DATE, PRODUCT_ID, USER_ID, SALES_AMOUNT
FROM (
    SELECT
        DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
        PRODUCT_ID,
        USER_ID,
        SALES_AMOUNT
    FROM ONLINE_SALE
    UNION ALL
    SELECT
        DATE_FORMAT(SALES_DATE, "%Y-%m-%d") AS SALES_DATE,
        PRODUCT_ID,
        NULL AS USER_ID,
        SALES_AMOUNT
    FROM OFFLINE_SALE
) AS SALES
WHERE (
    YEAR(SALES_DATE) = 2022
    AND
    MONTH(SALES_DATE) = 3
)
ORDER BY SALES_DATE ASC, PRODUCT_ID ASC, USER_ID ASC;
