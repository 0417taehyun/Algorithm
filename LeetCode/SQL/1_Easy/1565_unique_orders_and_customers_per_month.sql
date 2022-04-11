-- [ LeetCode ] 1565. Unique Orders and Customers Per Month

/*
GROUP BY 구 관련해서 헷갈렸던 의문이 이 문제를 풀면서 해결됐다.
GROUP BY 구가 SELECT 구보다 먼저 실행됨에도 불구하고 AS 키워드를 활용한 별칭을 사용할 수 있는 경우와 그렇지 않은 경우가 존재했었다.
아래의 경우 `month`라는 이름의 필드가 원래 테이블 내에 존재하지 않는다. 따라서 별칭을 통해서 얻게 된 `month` 필드를 GROUP BY 구에서 사용할 수 있다.
만약 DATE_FORMAT 함수를 사용한 필드의 이름을 기존 필드와 동일한 `order_date`라고 명명했을 경우, 다시 말해 `DATE_FORMAT(order_date, "%Y-%m") AS order_date`와 같이 사용했을 경우
`GROUP BY order_date`와 같이 사용했을 경우 DATE_FORMAT 함수를 통해 포맷팅된 order_date 필드 값을 그룹핑하는 것이 아닌 기존 order_date 필드 값을 그룹핑한다.
결국 SELECT 구보다 GROUP BY 구가 먼저 실행되고 만약 그룹핑하려는 필드가 별칭이라 존재하지 않을 경우 SELECT 구에서 가져오는 식으로 작동하는 것이다.
*/

SELECT
    DATE_FORMAT(order_date, "%Y-%m") AS month,
    COUNT(order_id) AS order_count,
    COUNT(DISTINCT customer_id) AS customer_count
FROM Orders
WHERE invoice > 20
GROUP BY month;