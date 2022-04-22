-- [ LeetCode ] 2082. The Number of Rich Customers

/*
GROUP BY 구는 내부적으로 정렬을 수행하지만 DISTINCT 키워드는 별다른 정렬을 수행하지 않는다.
따라서 GROUP BY 구보다 DISTINCT 키워드를 사용하는 게 훨씬 성능이 좋다.
*/

SELECT COUNT(DISTINCT customer_id) AS rich_count
FROM Store
WHERE amount > 500;