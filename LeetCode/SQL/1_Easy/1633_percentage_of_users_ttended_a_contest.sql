-- [ LeetCode ] 1633. Percentage of Users Attended a Contest

/*
처음에 아래와 같은 해결책을 생각하기는 했으나
JOIN 구를 활용해도 문제를 풀 수 있을 것 같아서 시도하다가 안 된다는 것을 알고 시도하지 않았다.

LEFT JOIN 혹은 RIGHT JOIN 구를 사용해서 Register 테이블 내 contest_id 필드의 값 별로 user_id 필드의 값이 Users 테이블 내에는 존재하는데 Register 테이블 내에는 존재하지 않을 때로 생각하여 NULL 값이 반환될 것이라 여겼는데
결국 Register 테이블 내에 존재하는 user_id 필드의 값은 전부 Users 테이블에 존재하는 범위이기 때문에 NULL 값이 생성될 리가 없었다.

실제로 만약 이러한 문제를 받게 된다면 유실된 레코드 여부에 대한 질문 등을 하면 좋을 것 같다.
*/

SELECT
    contest_id,
    ROUND((COUNT(user_id) / (SELECT COUNT(user_id) FROM Users)) * 100, 2) AS percentage
FROM Register
GROUP BY contest_id
ORDER BY percentage DESC, contest_id ASC