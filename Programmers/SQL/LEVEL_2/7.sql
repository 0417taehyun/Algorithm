-- [ 프로그래머스 ] 입양 시각 구하기(1)

/*
자료형을 변환할 수 있게 도와주는 `CAST` 함수,
DATETIME 자료형에서 원하는 형태의 문자열로 추출하게 해주는 `DATEFORMAT` 함수를 사용해서 문제를 풀었다.

이때 유의할 점은 `9`시부터 `19`시 사이의 시간만을 구해야하는 조건인데,
해당 조건을 `GROUP BY` 절이 사용된 이후에 `HAVING` 절을 사용해서 구할 경우
`DATETIME` 필드가 이미 존재하지 않기 때문에 유의해야 한다.

추가적으로 문자열을 DATETIME 자료형으로 바꿔주는 함수는 `STR_TO_DATE(string, format)`이다.
*/

SELECT
    CAST(DATE_FORMAT(DATETIME, "%H") AS SIGNED) AS "HOUR",
    COUNT("HOUR") AS "COUNT"
FROM ANIMAL_OUTS
WHERE (
    CAST(DATE_FORMAT(DATETIME, "%H") AS SIGNED) >= 9
    AND
    CAST(DATE_FORMAT(DATETIME, "%H") AS SIGNED) <= 19
)
GROUP BY DATE_FORMAT(DATETIME, "%H")
ORDER BY HOUR;


/*
MySQL에는 DATETIME 자료형에서 시간 값만 추출해 정수로 반환해주는 `HOUR` 함수가 존재한다.
따라서 아래와 같이 더 간단하게 문제를 풀 수 있다.

이외에도 추출을 도와주는 `DATE`, `YEAR`, `MONTH`, `DAY`, `MINUTE`, `SECOND` 함수도 존재한다.
이때 `DATE` 함수의 경우 그 반환값이 문자열임에 유의해야 한다.
*/

SELECT
    HOUR(DATETIME) AS "HOUR",
    COUNT("HOUR") AS "COUNT"
FROM ANIMAL_OUTS
WHERE (
    HOUR(DATETIME) >= 9
    AND
    HOUR(DATETIME) <= 19
)
GROUP BY HOUR(DATETIME)
ORDER BY HOUR;