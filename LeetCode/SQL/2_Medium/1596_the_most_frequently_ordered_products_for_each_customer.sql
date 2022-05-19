-- [ LeetCode ] 1596. The Most Frequently Ordered Products for Each Customer

SELECT
    Orders.customer_id,
    Orders.product_id,
    Products.product_name
FROM Orders
JOIN (
    SELECT
        customer_id,
        product_id,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_amount DESC) AS order_amount_rank
    FROM (
        SELECT
            customer_id,
            product_id,
            COUNT(order_date) AS order_amount
        FROM Orders
        GROUP BY customer_id, product_id
    ) AS OrderAmount
) AS OrderAmountRank
ON (
    OrderAmountRank.order_amount_rank = 1
    AND
    Orders.customer_id = OrderAmountRank.customer_id
    AND
    Orders.product_id = OrderAmountRank.product_id
)
JOIN Products
ON Orders.product_id = Products.product_id
GROUP BY Orders.customer_id, Orders.product_id;


/*
윈도우 함수(Window Function)를 GROUP BY 구와 같이 못 쓰는 줄 알았다.
그런데 보니까 GROUP BY 구가 결론적으로 윈도우 함수보다는 먼저 실행되며 따라서 먼저 customer_id 및 product_id 필드를 기준으로 그룹핑이 되었고,
PARTITION BY 구의 대상인 customer_id 필드가 이를 위배하지 않기 때문에 사용 가능하다.

추가적으로 MySQL이 표준 SQL 문법을 확장하여 GROUP BY 구에 별칭(Alias) 및 함수와 같이 컬럼이 아닌 것(Noncolumn)을 사용할 수 있는 것처럼
윈도우 함수 내부의 ORDER BY 구의 기준으로도 함수를 사용할 수 있어서 COUNT 함수를 사용해 그 결괏값을 기준으로 정렬하였다.

이때 PARTITION BY 구가 필요한 이유는 customer_id 필드를 기준으로 하지 않을 경우 GROUP BY 구로 묶인 뒤의 전체 레코드에 대한 순위를 매기기 때문이다.
GROUP BY 구로 묶인 두의 레코드들 중 각 customer_id 필드에 대한 순위를 개별적으로 구해야 하기 때문에 customer_id 필드를 PARTITION BY 구의 기준으로 설정해야 한다.
*/

SELECT
    customer_id,
    product_id,
    product_name
FROM (
    SELECT
        Orders.customer_id,
        Orders.product_id,
        Products.product_name,
        DENSE_RANK() OVER(PARTITION BY Orders.customer_id ORDER BY COUNT(Orders.order_date) DESC) AS order_amount_rank
    FROM Orders
    JOIN Products
    USING (product_id)
    GROUP BY Orders.customer_id, Orders.product_id
) AS OrderAmountRank
WHERE order_amount_rank = 1;
