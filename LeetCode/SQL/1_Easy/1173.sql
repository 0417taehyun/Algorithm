-- [ LeetCode ] 1173. Immediate Food Delivery I

SELECT
    ROUND(((SELECT COUNT(delivery_id) FROM Delivery WHERE order_date = customer_pref_delivery_date) / COUNT(delivery_id)) * 100, 2)
    AS immediate_percentage
FROM Delivery;


/*
아래 두 풀이와 같이 서브쿼리를 사용하지 않더라도 SUM 및 AVG 함수 내부에 조건식을 대입하여 문제를 해결할 수 있다.
*/

SELECT ROUND(SUM(order_date = customer_pref_delivery_date) / COUNT(delivery_id) * 100, 2) AS immediate_percentage
FROM Delivery;


SELECT ROUND(AVG(order_date = customer_pref_delivery_date) * 100, 2) AS immediate_percentage
FROM Delivery;