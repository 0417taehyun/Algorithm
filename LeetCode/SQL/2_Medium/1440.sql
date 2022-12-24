-- [ LeetCode ] 1440. Evaluate Boolean Expression

/*
유의할 점은 MySQL에서 비교 연산자에 대한 반환값으로 참(`TRUE`)일 경우 `1`, 거짓(`FALSE`)일 경우 `0`을 반환하기 때문에
IF 함수를 사용하여 문자열로 `"true"` 및 `"false"`로 변환해서 값을 출력해야 한다.
*/

SELECT
    left_operand,
    operator,
    right_operand,
    CASE operator
        WHEN '>' THEN IF(LeftVariables.value > RightVariables.value, "true", "false")
        WHEN '<' THEN IF(LeftVariables.value < RightVariables.value, "true", "false")
        ELSE IF(LeftVariables.value = RightVariables.value, "true", "false")
    END AS value
FROM Expressions
JOIN Variables AS LeftVariables
ON left_operand = LeftVariables.name
JOIN Variables AS RightVariables
ON right_operand = RightVariables.name;
