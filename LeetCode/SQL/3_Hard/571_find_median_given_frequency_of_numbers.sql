-- [ LeetCode ] 571. Find Median Given Frequency of Numbers

/*
처음에는 아래와 같이 복잡하게 문제를 풀었다.
WITH RECURSIVE 구에서 WHERE 구를 통해 제약을 걸어 전체 개수가 홀수인 경우와 짝수인 경우를 나눠서 중간값을 구했다.

이때 유의할 점은 UNION ALL 키워드 다음에 오는 SELECT 구가 결국 WHERE 구보다 이전에 실행된다는 것이다. 
추가적으로 SUM 윈도우 함수(Window Function)의 경우 OVER 부분에 아무런 조건을 서술하지 않으면 누적합이 아닌 전체 합을 구한다.
*/

WITH RECURSIVE MedianPositions (mid_number, flag) AS (
    SELECT
        ROUND(SUM(frequency) / 2) AS mid_number,
        MOD(SUM(frequency), 2) AS flag
    FROM Numbers
    UNION ALL
    SELECT
        mid_number + 1 as mid_number,
        flag + 1 AS flag
    FROM MedianPositions
    WHERE flag = 0
)

SELECT ROUND(AVG(NumberRanges.num), 1) AS median
FROM (
    SELECT
        num,
        LAG(end_num, 1, 0) OVER(ORDER BY num ASC) AS start_num,
        end_num
    FROM (
        SELECT
            num,
            SUM(frequency) OVER(ORDER BY num ASC) AS end_num
        FROM Numbers
    ) AS EndNumbers
) AS NumberRanges
JOIN MedianPositions
ON MedianPositions.mid_number BETWEEN NumberRanges.start_num + 1 AND NumberRanges.end_num;


