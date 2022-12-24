-- [ LeetCode ] 1532. The Most Recent Three Orders

/*
DENSE_RANK 윈도우 함수(Window Function)를 사용해서 문제를 풀었다. 이때 RANK 함수가 아닌 DENSE_RANK 함수를 사용한 이유는 확장성 때문이다.
문제에서는 하루에 단 한번의 주문한 한 것이 보증되지만 이후에 확장성을 고려했을 때 사용자가 동일한 날짜에 여러 번의 주문을 할 수 있기 때문이다.
*/

SELECT
    Customers.name AS customer_name,
    Customers.customer_id AS customer_id,
    OrdersRank.order_id AS order_id,
    OrdersRank.order_date AS order_date
FROM Customers
JOIN (
    SELECT
        order_id,
        customer_id,
        order_date,
        DENSE_RANK() OVER(PARTITION BY customer_id ORDER BY order_date DESC) AS order_rank
    FROM Orders
) AS OrdersRank
ON (
    OrdersRank.order_rank <= 3
    AND
    Customers.customer_id = OrdersRank.customer_id
)
ORDER BY customer_name ASC, customer_id ASC, order_date DESC;


/*
굳이 윈도우 함수를 사용하지 않더라도 아래와 같이 두 번의 JOIN 구를 통해 문제를 해결할 수 있다.
COUNT 함수를 활용해서 기준이 되는 날짜 이후의 날짜의 갯수가 3개 이하면 위에서부터 가장 최신인 날짜가 되기 때문이다.
*/

SELECT
    Customers.name AS customer_name,
    Customers.customer_id,
    Orders.order_id,
    Orders.order_date
FROM Customers
JOIN Orders
USING (customer_id)
JOIN Orders AS NextOrderDate
ON (
    Customers.customer_id = NextOrderDate.customer_id
    AND
    Orders.order_date <= NextOrderDAte.order_date
)
GROUP BY Customers.customer_id, Orders.order_date
HAVING COUNT(NextOrderDate.order_id) <= 3
ORDER BY customer_name ASC, customer_id ASC, order_date DESC;
