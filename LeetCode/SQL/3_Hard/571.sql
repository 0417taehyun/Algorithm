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


/*
아래와 같이 수학적인 접근을 통해 문제를 해결할 수 있다.
어떤 수 N의 이전 수들의 개수와 다음 수들의 개수가 같다면 해당 N은 중간에 있는 값이며 만약 다르다면 그 다른 범위를 N의 개수로 채울 수 있다.
따라서 여기서 개수를 의미하는 frequency 필드를 활용하여 이전 수들의 개수와 다음 수들의 개수의 차이가 만약 현재 수의 개수보다 작거나 같다면 해당 수는 중간값이다.
*/

SELECT AVG(Numbers.num) AS median
FROM Numbers
WHERE Numbers.frequency >= ABS(
    (SELECT SUM(Subnumbers.frequency) FROM Numbers AS Subnumbers WHERE Numbers.num >= Subnumbers.num)
    -
    (SELECT SUM(Subnumbers.frequency) FROM Numbers AS Subnumbers WHERE Numbers.num <= Subnumbers.num)
);


-- 아래와 같이 WITH 구를 통해 위 방법을 조금 더 깔금하게 바꾸어 해결할 수 있다.

WITH PreviousNumbers (num, previous_counts) AS (
    SELECT
        Numbers.num,
        SUM(Subnumbers.frequency) AS previous_counts
    FROM Numbers
    JOIN Numbers AS Subnumbers
    ON Numbers.num <= Subnumbers.num
    GROUP BY Numbers.num
), NextNumbers (num, next_counts) AS (
    SELECT
        Numbers.num,
        SUM(Subnumbers.frequency) AS next_counts
    FROM Numbers
    JOIN Numbers AS Subnumbers
    ON Numbers.num >= Subnumbers.num
    GROUP BY Numbers.num
)

SELECT AVG(Numbers.num) AS median
FROM Numbers
JOIN PreviousNumbers
USING (num)
JOIN NextNumbers
USING (num)
WHERE Numbers.frequency >= ABS(PreviousNumbers.previous_counts - NextNumbers.next_counts);