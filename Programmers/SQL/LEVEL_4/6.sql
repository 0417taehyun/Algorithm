-- [ 프로그래머스 ] 주문량이 많은 아이스크림들 조회하기

SELECT FLAVOR
FROM (
    SELECT
        FLAVOR
        SUM(FIRST_HALF.TOTAL_ORDER + JULY.TOTAL_ORDER) AS TOTAL_ORDER
    FROM FIRST_HALF
    JOIN (
        SELECT
            FLAVOR,
            SUM(TOTAL_ORDER) AS TOTAL_ORDER
        FROM JULY
        GROUP BY FLAVOR
    ) AS JULY
    USING (FLAVOR)
    GROUP BY FLAVOR
    ORDER BY TOTAL_ORDER DESC
    LIMIT 3;
) AS ICE_CREAM
LIMIT 3;


/*
ORDER BY 구의 경우 SELECT 구에서 선택된 필드에 한해서만 사용할 수 있는 줄 알았는데 아래와 같이 ORDER BY 구 자체에도 함수를 사용해서 정렬할 수 있었다.
*/

SELECT FLAVOR
FROM FIRST_HALF
JOIN (
    SELECT
        FLAVOR,
        SUM(TOTAL_ORDER) AS TOTAL_ORDER
    FROM JULY
    GROUP BY FLAVOR
) AS JULY
USING (FLAVOR)
GROUP BY FLAVOR
ORDER BY SUM(FIRST_HALF.TOTAL_ORDER + JULY.TOTAL_ORDER) DESC
LIMIT 3;
