-- [ LeetCode ] 627. Swap Salary

-- UPDATE 구의 SET 구 내부에서도 CASE 구를 사용하여 조건을 지정해서 변경할 수도 있다.

UPDATE Salary SET sex = CASE sex
    WHEN "m" THEN "f"
    ELSE "m"
    END;


-- 아래와 같이 IF 조건문을 사용하여 더 간단하게 풀이할 수도 있다.

UPDATE Salary SET sex = IF(sex = "m", "f", "m");