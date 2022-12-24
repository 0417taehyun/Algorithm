-- [ LeetCode ] 1159. Market Analysis II

SELECT
    Users.user_id AS seller_id,
    IF(OrdersReports.user_id IS NULL, 'no', 'yes') AS 2nd_item_fav_brand
FROM Users
LEFT JOIN (
    SELECT
        Orders.seller_id AS user_id,
        Items.item_brand AS favorite_brand
    FROM Orders
    JOIN Orders AS SubOrders
    ON (
        Orders.seller_id = SubOrders.seller_id
        AND
        Orders.order_date >= SubOrders.order_date
    )
    JOIN Items
    ON Orders.item_id = Items.item_id
    GROUP BY Orders.seller_id, Orders.order_date
    HAVING COUNT(SubOrders.order_id) = 2
) As OrdersReports
USING (user_id, favorite_brand);


/*
아래와 같이 CASE 구를 사용하여 서브쿼리로 user_id 필드의 값과 seller_id 필드의 값이 같은 Orders 테이블 중
order_date 필드를 기준으로 오름차순 정렬하고 LIMIT 및 OFFSET 키워드를 통해 두 번째 행만 조회하여
해당 행의 item_brand 필드의 값이 favorite_brand 필드의 값과 같은 경우면 'yes'를, 그렇지 않으면 'no'를 반환하게 해서 문제를 풀 수도 있다.
*/

SELECT
    user_id AS seller_id,
    CASE favorite_brand
        WHEN (
            SELECT item_brand
            FROM Orders
            JOIN Items
            USING (item_id)
            WHERE user_id = seller_id
            ORDER BY order_date ASC
            LIMIT 1 OFFSET 1
        ) THEN 'yes'
        ELSE 'no'
    END AS 2nd_item_fav_brand
FROM Users;
