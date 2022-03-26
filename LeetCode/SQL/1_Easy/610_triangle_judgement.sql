-- [ LeetCode ] 610. Triangle Judgement

SELECT
    x, y, z,
    CASE
        WHEN (x >= y) AND (x >= z) THEN (
            CASE
                WHEN (y + z) > x THEN "Yes"
                ELSE "No"
            END
        )
        WHEN (y >= x) AND (y >= z) THEN (
            CASE
                WHEN (x + z) > y THEN "Yes"
                ELSE "No"
            END
        )
        WHEN (z >= x) AND (z >= y) THEN (
            CASE
                WHEN (x + y) > z THEN "Yes"
                ELSE "No"
            END
        )
    END AS "triangle"
FROM Triangle;


/*
GREATEST 함수를 사용하여 문제를 풀 수도 있다.
해당 함수는 인자를 받아서 해당 인자 중에 가장 큰 값을 반환해준다.

또한 IF 함수를 통해 만약 첫 번째 인자인 조건의 결과가 true일 경우 두 번째 인자의 값을,
false일 경우 세 번째 인자의 값을 반환하여 문제를 해결할 수 있다.
*/

SELECT
    x, y, z,
    CASE
        WHEN GREATEST(x, y, z) = x THEN IF(y+z > x, "Yes", "No")
        WHEN GREATEST(x, y, z) = y THEN IF(x+z > y, "Yes", "No")
        ELSE IF(x+y > z, "Yes", "No")
    END AS "triangle"
FROM Triangle;