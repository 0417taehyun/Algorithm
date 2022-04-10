-- [ LeetCode ] 1511. Customer Order Frequency

/*
문제를 해결한 방법 중에 WHERE 구에 작성한 YEAR 함수를 통해 2020년인 경우를 확인하지 않는 풀이법이 있었다.
저장된 데이터의 범위가 따로 한정되어 있다는 이야기는 문제에 없었기 때문에 이 부분도 조건을 고려해주는 게 옳다.

한 가지 궁금한 점은 HAVING 구 내부 SUM 함수의 조건절에 연도에 대한 조건을 추가하는 것이 훨씬 효율적인지 아니면 WHERE 구에 조건을 거는 것이 효율적인지 궁금했다.
생각했을 때는 처음 YEAR 함수 및 MONTH 함수가 한번씩 order_date 필드를 조회하기 때문에 WHERE 구에 한번 써주는 게 훨씬 효율적이라 생각했다.

먼저 아래는 SUM 함수의 내부 조건에 MONTH 함수만 사용했을 때의 실행계획이다.
-> Filter: ((sum(if((month(orders.order_date) = 6),(product.price * orders.quantity),0)) >= 100) and (sum(if((month(orders.order_date) = 7),(product.price * orders.quantity),0)) >= 100)) (actual time=0.081..0.082 rows=1 loops=1)

댜음으로 아래는 SUM 함수의 내부 조건에 MONTH 함수와 동시에 YEAR 함수까지 함께 사용했을 때의 실행계획이다.
-> Filter: ((sum(if(((month(orders.order_date) = 6) and (year(orders.order_date) = 2020)),(product.price * orders.quantity),0)) >= 100) and (sum(if(((month(orders.order_date) = 7) and (year(orders.order_date) = 2020)),(product.price * orders.quantity),0)) >= 100))  (actual time=0.099..0.100 rows=1 loops=1)

SUM 함수 내부 조건에 MONTH 함수를 사용하고 이후 마지막 즈음에 WHERE 구에 대한 쿼리 실행을 하게 되는데 사실 단순 SUM 함수 부분만 살펴보더라도 그렇게 극명한 차이가 발생하지 않는 것을 알 수 있다.
관련해서 최적화하는 방안에 대해서는 나중에 한번 더 찾아봐야겠다.
*/

SELECT
    Orders.customer_id AS customer_id,
    name
FROM Orders
JOIN Customers
USING (customer_id)
JOIN Product
USING (product_id)
WHERE YEAR(order_date) = 2020
GROUP BY customer_id
HAVING (
    SUM(IF(MONTH(order_date) = 6, price*quantity, 0)) >= 100
    AND
    SUM(IF(MONTH(order_date) = 7, price*quantity, 0)) >= 100
);