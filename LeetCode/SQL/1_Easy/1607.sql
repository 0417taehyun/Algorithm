-- [ LeetCode ] 1607. Sellers With No Sales

/*
결론적으로 `sale_date` 필드의 값이 `2020`이 없는 경우를 구하는 문제였는데
한번도 판매가 된 적이 없어 Orders 테이블에서 NULL 값인 seller_id 값을 고려를 해주지 않아 틀렸었다.
앞으로 문제를 풀 때는 제약 조건을 한번 더 꼼꼼히 따져봐야겠다.

추가적으로 YEAR 함수 및 SUM 함수의 경우 NULL 값을 따로 처리하지 않기 때문에 유의해야한다.
이를 해결하기 위해서 IFNULL 함수를 땨로 사용했다.
*/

SELECT
    seller_name
FROM Orders
RIGHT JOIN Seller
USING (seller_id)
GROUP BY seller_id
HAVING SUM(IFNULL(YEAR(sale_date) = "2020", 0)) = 0
ORDER BY seller_name ASC;