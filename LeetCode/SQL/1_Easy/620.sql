-- [ LeetCode ] 620. Not Boring Movies

/*
MOD 함수는 말 그대로 나머지를 반환해주는 함수다.
MySQL 내부적으로는 % 연산자가 존재하지만 이는 Oracle에서는 존재하지 않는 연산자다.
따라서 표준에 더 가까운 MOD 함수를 사용해주는 게 더 좋다.
*/

SELECT id, movie, description, rating
FROM Cinema
WHERE (
    MOD(id, 2) = 1
    AND
    description NOT LIKE "%boring%"
)
ORDER BY rating DESC;