-- [ 프로그래머스 ] 경기도에 위치한 식품창고 목록 출력하기

SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IFNULL(FREEZER_YN, "N") AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;


SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    IF(FREEZER_YN IS NULL, "N", FREEZER_YN) AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;


SELECT
    WAREHOUSE_ID,
    WAREHOUSE_NAME,
    ADDRESS,
    CASE
        WHEN FREEZER_YN IS NULL THEN "N"
        ELSE FREEZER_YN
    END AS FREEZER_YN
FROM FOOD_WAREHOUSE
WHERE ADDRESS LIKE "경기도%"
ORDER BY WAREHOUSE_ID ASC;