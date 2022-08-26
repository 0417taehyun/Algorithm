-- [ LeetCode ] 2388. Change Null Values in a Table to the Previous Value

SELECT
    id,
    IFNULL(drink, SubTable_drink) AS drink
FROM (
    SELECT
        WithRowNum.id,
        WithRowNum.drink,
        MAX(SubTable.row_num) AS latest_one,
        SubTable.drink AS SubTable_drink
    FROM (
        SELECT
            ROW_NUMBER() OVER() AS row_num,
            id,
            drink
        FROM CoffeeShop
    ) AS WithRowNum
    LEFT JOIN (
        SELECT
            ROW_NUMBER() OVER() AS row_num,
            id,
            drink
        FROM CoffeeShop
    ) AS SubTable
    ON (
        WithRowNum.drink IS NULL
        AND
        WithRowNum.row_num > SubTable.row_num
        AND
        SubTable.drink IS NOT NULL
    )
    GROUP BY WithRowNum.id
) AS Result;


-- 아래와 같이 WITH 구를 사용하여 임시 테이블을 생성해 반복되는 서브쿼리에 대한 최적화가 가능하다.

WITH WithRowNum (row_num, id, drink) AS (
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        id,
        drink
    FROM CoffeeShop
)

SELECT
    id,
    IFNULL(drink, SubTable_drink) AS drink
FROM (
    SELECT
        WithRowNum.id,
        WithRowNum.drink,
        MAX(SubTable.row_num) AS latest_one,
        SubTable.drink AS SubTable_drink
    FROM WithRowNum
    LEFT JOIN WithRowNum AS SubTable
    ON (
        WithRowNum.drink IS NULL
        AND
        WithRowNum.row_num > SubTable.row_num
        AND
        SubTable.drink IS NOT NULL
    )
    GROUP BY WithRowNum.id
) AS Result;


-- 최종적으로 WITH RECURSIVE 구를 활용해 최적화가 가능하다.

WITH RECURSIVE WithRowNum (row_num, id, drink) AS (
    SELECT
        ROW_NUMBER() OVER() AS row_num,
        id,
        drink
    FROM CoffeeShop
), Result (row_num, id, drink) AS (
    SELECT
        row_num,
        id,
        drink
    FROM WithRowNum
    WHERE row_num = 1
    UNION ALL
    SELECT
        WithRowNum.row_num,
        WithRowNum.id,
        IFNULL(WithRowNum.drink, Result.drink) AS drink
    FROM Result
    JOIN WithRowNum
    ON Result.row_num = WithRowNum.row_num - 1
)

SELECT id, drink
FROM Result;