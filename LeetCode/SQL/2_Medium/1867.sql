-- [ LeetCode ] 1867. Orders With Maximum Quantity Above Average

WITH cte AS (
    SELECT
        order_id,
        MAX(quantity) AS max_quantity,
        AVG(quantity) AS average_quantity
    FROM OrdersDetails
    GROUP BY order_id
)

SELECT order_id
FROM cte
WHERE max_quantity > (SELECT MAX(average_quantity) FROM cte);


/*
처음에 위와 같이 풀었는데 아래와 같이 더 간단하게 풀 수 있다.
결과부터 이야기하자면 MAX 함수 부분이 위와 달리 반복되지 않기 때문에 훨씬 성능이 좋다.

AVG 함수를 사용하여 GROUP BY 구를 통해 그룹핑된 필드 내의 quantity 필드의 평균을 구한 뒤 그 평균들 중에서 가장 큰 값을 MAX 윈도우 함수(Window Function)를 통해 찾는다.
결국 윈도우 함수는 GROUP BY 등의 모든 레코드 조작이 거친 뒤의 필드를 대상으로 하기 때문에 정상적으로 작동한다.
그리고 MAX 윈도우 함수는 결국 동일한 값을 모든 order_id 필드에 대해 주기 때문에 WHERE 구에서 이를 max_quantity 필드의 값과 비교하면 된다.
*/

WITH cte AS (
    SELECT
        order_id,
        MAX(AVG(quantity)) OVER() AS max_average_quantity,
        MAX(quantity) AS max_quantity
    FROM OrdersDetails
    GROUP BY order_id
)

SELECT order_id
FROM cte
WHERE max_quantity > max_average_quantity;
