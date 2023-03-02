-- [ 프로그래머스 ] 대여 횟수가 많은 자동차들의 월별 대여 횟수 구하기

SELECT
    MONTH,
    CAR_ID,
    RECORDS
FROM (
    SELECT
        MONTH(START_DATE) AS 'MONTH',
        CAR_ID,
        COUNT(HISTORY_ID) AS RECORDS,
        SUM(COUNT(HISTORY_ID)) OVER(PARTITION BY CAR_ID) AS TOTAL_RECORDS
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
    WHERE (
        YEAR(START_DATE) = 2022
        AND
        MONTH(START_DATE) >= 8
        AND
        MONTH(START_DATE) <= 10
    )
    GROUP BY MONTH(START_DATE), CAR_ID
) AS TARGET_CARS
WHERE TOTAL_RECORDS >= 5
ORDER BY MONTH ASC, CAR_ID DESC;
