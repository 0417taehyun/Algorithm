-- [ LeetCode ] 1045. Customers Who Bought All Products

/*
product_key 필드가 Product 테이블과 연결 된 외래 키(Foregin Key)이기 때문에
굳이 Product 테이블에서는 삭제가 되었는데 Customer 테이블에는 남아있는 경우를 따지지 않아도 괜찮다.
따라서 아래와 같이 JOIN 구를 별도로 사용하지 않고 단순히 서브쿼리만 활용하여 문제를 해결할 수 있다.
*/

SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(product_key) FROM Product);