-- [ LeetCode ] 619. Biggest Single Number

-- MAX 함수는 NULL 값을 자동으로 처리해서 만약 존재하지 않을 경우 NULL 값을 반환한다.

SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS Single_Numbers;