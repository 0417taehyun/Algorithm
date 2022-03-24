-- [ LeetCode ] 197. Rising Temperature

/*
SUBDATE를 사용하여 주어진 날짜를 연산할 수 있다.
첫 번째 인자로 DATE 두 번째 인자로 DAY를 받아서 DATE로부터 DAY만큼의 값을 뺀 새로운 DATE를 반환한다.

비슷한 문법으로 DATE_ADD(DATE, INTERVAL -1 DAY)와 같은 문법을 사용하거나,
DATE_SUB(DATE, INTERVAL 1 DAY)와 같은 문법을 사용해도 똑같은 결괏값을 얻을 수 있다.
이때 INTERVAL 뒤에는 얼마만큼의 격차를 벌릴 것인지 숫자를 입력하고 그 뒤에는 HOUR, DAY, MONTH 등의 시간 종류를 입력한다.
*/

SELECT Weather.id AS id
FROM Weather
JOIN Weather AS Joined_Table
ON SUBDATE(Weather.recordDate, 1) = Joined_Table.recordDate
WHERE Weather.temperature > Joined_Table.temperature;


/*
아래와 같이 JOIN 구문의 조건인 ON 구에 복수의 조건을 설정할 수도 있다.
이때 DATEDIFF 함수를 사용하여 Weather.recordDate 필드의 값에서 Joined_Table.recordDate 필드의 값을 뺀 결과가 1인 경우만 JOIN을 실행하게 한다.
이는 다시 말해 Weather.recordDate 필드의 값이 하루 더 늦는다는, 더 최신의 날짜라는 걸 의미한다.
*/

SELECT Weather.id AS id
FROM Weather
JOIN Weather AS Joined_Table
ON (
    DATEDIFF(Weather.recordDate, Joined_Table.recordDate) = 1
    AND
    Weather.temperature > Joined_Table.temperature
);

