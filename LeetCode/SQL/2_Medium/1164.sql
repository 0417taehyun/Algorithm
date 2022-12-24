-- [ LeetCode ] 1164. Product Price at a Given Date

/*
change_date 필드의 값이 `2019-08-16` 값보다 이전인 경우가 없는 예외처리를 하는 부분 때문에 좀 시간이 걸렸다.
다른 정답을 보니 UNION 키워드를 활용하여 푸는 경우도 있었는데 아래와 같이 IFNULL 및 SUM 함수를 사용하는 것도 괜찮은 풀이 같다.
SUM 함수의 경우 NULL 값을 그대로 `NULL`로 두기 때문에 만약 모든 값이 `NULL`인 경우 그 합은 `NULL`이다.
만약 하나라도 숫자가 존재할 경우, 예를 들어 `10`, `NULL`, `20`, `NULL`과 같이 값이 존재할 경우 이에 대해 SUM 함수를 사용하면 결과는 `30`이다.

DISTINCT 키워드 및 MAX 윈도우 함수(Window Function)를 사용하는 경우와 GROUP BY 구 및 MAX 함수를 사용하는 경우 중 무엇이 더 빠르고 좋은지, 언제 각각을 사용해야 하는지는 추후에 살펴보고자 한다.
DISTINCT 키워드 때문에 아무래도 윈도우 함수가 더 빠를 것으로 예상했는데 관련해서는 더 자세히 알아보야겠다.
*/

SELECT
    Products.product_id AS product_id,
    IFNULL(
        SUM(
            CASE
                WHEN Products.change_date = ChangedProducts.change_date THEN new_price
                ELSE NULL
            END
        ), 10
    ) AS price
FROM Products
LEFT JOIN (
    SELECT
        DISTINCT product_id,
        MAX(change_date) OVER(PARTITION BY product_id) AS change_date
    FROM Products
    WHERE change_date <= '2019-08-16'
) AS ChangedProducts
USING (product_id, change_date)
GROUP BY Products.product_id;
