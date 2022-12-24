-- [ LeetCode ] 1158. Market Analysis I

/*
처음에 회원가입은 진행을 해서 Users 테이블에 존재하는데 주문을 하지 않아 Orders 테이블에 존재하지 않는 사용자를 고려하지 않아 제출했을 때 틀린 값을 반환했다.
Users 테이블을 기준으로 Orders 테이블을 LEFT JOIN 구로 연걸해서 문제를 해결할 수 있다.
주문을 하지 않은 경우도 결론적으로는 `0` 값을 반환해야 하기 때문에 SUM 함수 및 IF 함수의 조건을 활용했다.
*/

SELECT
    Users.user_id AS buyer_id,
    Users.join_date AS join_date,
    SUM(IF(YEAR(Orders.order_date) = '2019', 1, 0)) AS orders_in_2019
FROM Users
LEFT JOIN Orders
ON Users.user_id = Orders.buyer_id
GROUP BY user_id;
