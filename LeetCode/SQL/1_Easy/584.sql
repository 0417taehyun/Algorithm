-- [ LeetCode ] 584. Find Customer Referee

-- 아래와 같이 WHERE 구에 서브쿼리를 활용한 풀이가 속도가 빨랐다.

SELECT name
FROM Customer
WHERE NOT id IN (
    SELECT id
    FROM Customer
    WHERE referee_id = 2
);


-- 아래와 같이 IFNULL 함수를 사용하여 문제를 해결할 수도 있다.

SELECT name
FROM Customer
WHERE IFNULL(referee_id, 0) <> 2;