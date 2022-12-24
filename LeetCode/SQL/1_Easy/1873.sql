-- [ LeetCode ] 1873. Calculate Special Bonus

/*
LEFT 함수를 사용하여 좌측을 기준으로 어떤 문자열의 특정 인덱스에 위치한 값을 추출할 수 있다.
이때 유의할 점은 인덱스가 `1`부터 시작한다는 것이다.
*/

SELECT
    employee_id,
    IF (
        (
            MOD(employee_id, 2) = 1
            AND
            LEFT(name, 1) <> 'M'
        ),
        salary,
        0
    ) AS bonus
FROM Employees
ORDER BY employee_id;