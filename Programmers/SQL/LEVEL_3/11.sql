-- [ 프로그래머스 ] 자동차 대여 기록에서 대여중 / 대여 가능 여부 구분하기

SELECT
    CAR_ID,
    IF(MAX(AVAILABILITY) = 1, '대여중', '대여 가능') AS AVAILABILITY
FROM (
    SELECT
        CAR_ID,
        IF(START_DATE <= '2022-10-16' AND END_DATE >= '2022-10-16', 1, 0) AS AVAILABILITY
    FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
) AS CAR_AVAILABILITY
GROUP BY CAR_ID
ORDER BY CAR_ID DESC;
