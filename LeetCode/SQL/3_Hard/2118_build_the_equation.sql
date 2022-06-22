-- [ LeetCode ] 2118. Build the Equation

/*
GROUP_CONCAT 함수 내부에 컬럼이 아닌 것을 사용할 수 없다.
예를 들어 CASE 구를 사용할 경우 그 결괏값들에 대해 GROUP_CONCAT 함수가 작동하는 것이 아닌 CASE 구문 자체가 GROUP_CONCAT 함수의 대상이 된다.
*/

SELECT CONCAT(GROUP_CONCAT(LHS ORDER BY power DESC SEPARATOR ''), '=0') AS equation
FROM (
    SELECT
        power,
        CASE power
            WHEN 1 THEN IF(factor > 0, CONCAT('+', factor, 'X'), CONCAT(factor, 'X'))
            WHEN 0 THEN IF(factor > 0, CONCAT('+', factor), CONCAT(factor))
            ELSE IF(factor > 0, CONCAT('+', factor, 'X', '^', power), CONCAT(factor, 'X', '^', power))
        END AS LHS
    FROM Terms
) AS LHSTemrs;
