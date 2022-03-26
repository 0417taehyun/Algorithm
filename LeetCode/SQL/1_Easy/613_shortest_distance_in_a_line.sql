-- [ LeetCode ] 613. Shortest Distance in a Line

/*
비집계함수의 종류 중 하나인 ROW_NUMBER 함수를 활용하여 문제를 풀 수 있다.
이전 512. Game Play Analysis II 문제를 풀었을 때 사용했던 RANK 함수와 사용법은 똑같다.
ROW_NUMBER 함수를 사용해 두 테이블을 INNER JOIN 한 뒤 ABS 함수를 사용해 두 거리의 절댓값을 구하고 가장 작은 값을 반환하여 선택하였다.
*/

SELECT MIN(ABS(Point_With_Row.x - Joined_Table.x)) AS "shortest"
FROM (
    SELECT
        x,
        ROW_NUMBER() OVER (ORDER BY x) AS row_num
    FROM Point
) AS Point_With_Row
JOIN (
    SELECT
        x,
        ROW_NUMBER() OVER (ORDER BY x) AS row_num
    FROM Point
) AS Joined_Table
ON Point_With_Row.row_num = Joined_Table.row_num + 1


/*
또한 아래와 같이 LEAD 함수, 또는 LEG 함수를 사용하여 다음행의 값을 구하여 문제를 해결할 수도 있다.

두 함수 모두 각각의 행에 대한 결괏값을 반환하기 때문에 윈도우 함수다.
(앞서 언급했던 ROW_NUMBER 및 RANK 함수 모두 비집계함수, 분석함수라 불렀지만 동시에 윈도우 함수이기도 하다.)

LEAD 함수를 사용하는 방법은 아래와 같다.

LEAD(column_name, offset, default_value) OVER (PARTITION BY column_name ORDER BY column_name) AS result_name;

LEAD 함수가 다음행을 의미했다면, LAG 함수는 이전행을 의미한다. 이때 사용법은 LEAD 함수와 동일하다.
모두 offset의 기본값으로 `1`을 의미해서 아래 해결 쿼리에서 `1`을 생략해도 된다.
default_value의 경우 만약 값이 NULL일 경우에 대한 기본값을 설정해주게 된다.
*/

SELECT MIN(length) AS shortest
FROM (
    SELECT ABS(x - LEAD(x, 1) OVER (ORDER BY x)) AS length
    FROM Point
) AS Point_Length


/*
아래와 같이 굳이 행의 번호가 존재하지 않더라도 x 값이 다른 경우를 전부 INNER JOIN하여 계산한 결괏값이 가장 작은 경우를 반환해도 된다.

ROW_NUMBER 함수를 사용하여 x 값을 기준으로 행을 정렬해서 번호를 매긴 이후 INNER JOIN을 사용한 이유는,
거리를 일차원에서의 거리를 계산하기 때문에 본인을 기준으로 바로 다음 값과의 결과만 계산하면 되기 때문이다.

아래와 같이 문제를 해결할 경우 JOIN에 따라 필드 수가 배로 들기 때문에 연산 속도가 훨씬 느려진다.
더욱이 x 값이 동일한 경우, 다시 말해 거리가 0인 경우에 대한 부분이 JOIN의 조건에서 문제가 될 수 있다.

이러한 제약 조건을 인터뷰 때 물어보는 것도 좋은 접근이라 생각된다.
*/

SELECT MIN(ABS(Point.x - Joined_Table.x)) AS shortest
FROM Point
JOIN Point AS Joined_Table
ON (Point.x <> Joined_Table.x);