-- [ LeetCode ] 1853. Convert Date Format

/*
CONCAT_WS 함수의 경우 맨 첫 번째 매개변수를 통해 어떤 것을 구분으로 하여 문자를 합쳐줄 것인지 정해줄 수 있다.
DAYNAME 함수와 MONTHNAME 함수는 각각 요일의 이름과 월의 이름을 반환해준다.
*/

SELECT
    CONCAT_WS(', ', DAYNAME(day), CONCAT_WS(' ', MONTHNAME(Day), DAY(day)), YEAR(day)) AS day
FROM Days;


/*
물론 아래와 같이 DATE_FORMAT 함수를 사용하여 문제를 간단하게 해결할 수도 있다.
이때 유의할 점은 일(Day)을 나타낼 때 `%d`를 사용할 경우 `09`와 같이 2자리 수로 표현되며 `%e`를 사용할 경우 `9`와 같이 정수형으로 표현이 된다는 것이다.
*/

SELECT
    DATE_FORMAT(day, "%W, %M %e, %Y") AS day
FROM Days;