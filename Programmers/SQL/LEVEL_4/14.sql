-- [ 프로그래머스 ] 특정 기간동안 대여 가능한 자동차들의 대여비용 구하기


SELECT
    CAR_ID,
    CAR_TYPE,
    FEE
FROM (
    SELECT
        TARGET_CARS.CAR_ID,
        TARGET_CARS.CAR_TYPE,
        ROUND(TARGET_CARS.DAILY_FEE * ((100 - TARGET_DISCOUNT.DISCOUNT_RATE) / 100) * 30, 0) AS FEE
    FROM (
        SELECT
            TARGET_CARS.CAR_ID,
            TARGET_CARS.CAR_TYPE,
            TARGET_CARS.DAILY_FEE
        FROM (
            SELECT
                CAR_ID,
                CAR_TYPE,
                DAILY_FEE
            FROM CAR_RENTAL_COMPANY_CAR
            WHERE (
                CAR_TYPE = '세단'
                OR
                CAR_TYPE = 'SUV'
            )    
        ) AS TARGET_CARS
        LEFT JOIN (
            SELECT CAR_ID
            FROM CAR_RENTAL_COMPANY_RENTAL_HISTORY
            WHERE (
                (
                    START_DATE <= '2022-11-01'
                    AND
                    END_DATE >= '2022-11-01'
                )
                OR
                (
                    START_DATE >= '2022-11-01'
                    AND
                    END_DATE <= '2022-11-30'
                )
            )
        ) AS NONE_TARGET_CARS
        USING (CAR_ID)
        WHERE NONE_TARGET_CARS.CAR_ID IS NULL
    ) TARGET_CARS
    JOIN (
        SELECT
            CAR_TYPE,
            DISCOUNT_RATE
        FROM CAR_RENTAL_COMPANY_DISCOUNT_PLAN
        WHERE (
            (
                CAR_TYPE = '세단'
                OR
                CAR_TYPE = 'SUV'
            )
            AND
            DURATION_TYPE = '30일 이상'
        )
    ) AS TARGET_DISCOUNT
    USING (CAR_TYPE)
) AS RESULT
WHERE (
    FEE  >= 500000
    AND
    FEE < 2000000
)
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;


/*
아래와 같이 GROUP BY 구 및 HAVING 구, 그리고 MAX 집계 함수를 사용하여 문제를 풀 수도 있다.
IF 함수를 사용해 해당 기간 내에 빌리지 못하는 경우에 대해 값을 1로 치환하는 방식이다.
*/

SELECT
    CAR_ID,
    CAR_TYPE,
    FEE
FROM (
    SELECT
        CAR_RENTAL_COMPANY_CAR.CAR_ID,
        CAR_RENTAL_COMPANY_CAR.CAR_TYPE,
        ROUND(CAR_RENTAL_COMPANY_CAR.DAILY_FEE * ((100 - CAR_RENTAL_COMPANY_DISCOUNT_PLAN.DISCOUNT_RATE) / 100) * 30, 0) AS FEE
    FROM CAR_RENTAL_COMPANY_CAR
    JOIN CAR_RENTAL_COMPANY_RENTAL_HISTORY
    USING (CAR_ID)
    JOIN CAR_RENTAL_COMPANY_DISCOUNT_PLAN
    USING (CAR_TYPE)
    WHERE (
        (
            CAR_RENTAL_COMPANY_CAR.CAR_TYPE = '세단'
            OR
            CAR_RENTAL_COMPANY_CAR.CAR_TYPE = 'SUV'
        )
        AND
        CAR_RENTAL_COMPANY_DISCOUNT_PLAN.DURATION_TYPE = '30일 이상'
    )
    GROUP BY CAR_RENTAL_COMPANY_CAR.CAR_ID
    HAVING MAX(
        IF(
            (
                (
                    CAR_RENTAL_COMPANY_RENTAL_HISTORY.START_DATE <= '2022-11-01'
                    AND
                    CAR_RENTAL_COMPANY_RENTAL_HISTORY.END_DATE >= '2022-11-01'
                )
                OR
                (
                    CAR_RENTAL_COMPANY_RENTAL_HISTORY.START_DATE >= '2022-11-01'
                    AND
                    CAR_RENTAL_COMPANY_RENTAL_HISTORY.END_DATE <= '2022-11-30'
                )
            ),
            1,
            0
        )
    ) = 0
) AS TARGET_CARS
WHERE (
    FEE >= 500000
    AND
    FEE <= 2000000
)
ORDER BY FEE DESC, CAR_TYPE ASC, CAR_ID DESC;
