-- [ LeetCode ] 1398. Customers Who Bought Products A and B but Not C

/*
먼저 한 명의 사용자가 동일한 제품을 여러 번 구매할 수 있기 때문에 DISTINCT 키워드를 활용하여 각 사용자 별로 구매한 중복되지 않은 제품을 반환 받았다.
이는 결국 문제에서 product_name 필드의 값이 `A` 및 `B`인 경우가 존재하면서 `C`인 경우가 아니면 되기 때문이다.

이후 GROUP BY 구를 통해 각 사용자 별로 주문한 내역을 그룹화하고 HAVING 구에서 실제 원하는 레코드를 얻기 위해 조건을 걸었다.
WHERE 구 및 NOT IN 등을 활용한 방법도 있지만 기본적으로 NOT IN 조건은 해당 조건에 해당하는지, 그렇지 않은지 계속해서 값을 처음부터 끝까지 조회해야 하기 때문에 성능이 좋지 못하다.
따라서 `A` 및 `B`인 경우를 `1`로, `C`인 경우를 `-1`로 두어 SUM 함수를 실행하였다. 이때 굳이 SUM 함수가 아닌 COUNT 함수여도 무관하다.

기본 키(Primary Key)에 대한 부분이 주어졌을 때 기본 키가 아닌 값의 경우 중복될 수 있다는 점을 항상 떠올려야겠다.
*/

SELECT
    Customers.customer_id,
    Customers.customer_name
FROM Customers
JOIN (
    SELECT
        DISTINCT product_name,
        customer_id
    FROM Orders
) AS UniqueProductOrders
USING (customer_id)
GROUP BY Customers.customer_id
HAVING SUM(CASE WHEN product_name = 'A' OR product_name ='B' THEN 1 WHEN product_name = 'C' THEN -1 END) = 2
ORDER BY customer_id;
