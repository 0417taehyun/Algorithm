-- [ LeetCode ] 577. Employee Bonus


/*
Bonus 테이블에 한 명의 empId가 중복해서 여러 값을 받을 수 있을 것이라 생각하여

SELECT
    empId,
    SUM(bonus)
FROM Bonus
GROUP BY empId

형태로 묶어서 합산된 bonus 필드를 반환하는 서브쿼리도 작성했었다.
인터뷰 때 질문을 받는다면 이러한 조건들, 다시 말해 정규화 여부 등에 관해서도 물어보는 게 좋아보인다.
*/

SELECT
    name,
    bonus
FROM Employee
LEFT JOIN Bonus
USING (empId)
WHERE (
    bonus IS NULL
    OR
    bonus < 1000
);