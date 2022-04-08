-- [ LeetCode ] 1484. Group Sold Products By The Date

/*
GROUP_CONCAT 함수를 처음 알게 되었다. CONCAT 함수와 달리 그룹핑 된 필드를 수평으로 CONCAT 할 수 있게 해준다.
내부적으로 어떤 필드를 합칠 것인지, 그리고 정렬 기준과 SEPARATOR 키워드를 통해 구분점을 지정해줄 수 있다.

문제를 풀면서 유의한 점은 테이블에 대한 설명에서 기본 키(Primary Key)에 대한 언급이 없었기 때문에
동일한 sell_date 필드 값 내에 동일한 product 필드 값이 존재할 수 있어서 DISTINCT 키워드를 사용해준 것이다.
문제를 앞으로도 꼼꼼하게 읽고 이러한 부분을 잘 고려해야겠다.
*/

SELECT
    sell_date,
    COUNT(DISTINCT product) AS num_sold,
    GROUP_CONCAT(
        DISTINCT product
        ORDER BY product ASC
        SEPARATOR ','
    ) AS products
FROM Activities
GROUP BY sell_date
ORDER BY sell_date;