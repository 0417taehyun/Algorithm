-- [ LeetCode ] 2159. Order Two Columns Independently

SELECT
    FirstColumns.first_col,
    SecondColumns.second_col
FROM (
    SELECT
        first_col,
        ROW_NUMBER() OVER(ORDER BY first_col ASC) AS row_num
    FROM Data
) AS FirstColumns
JOIN (
    SELECT
        second_col,
        ROW_NUMBER() OVER(ORDER BY second_col DESC) AS row_num
    FROM Data
) AS SecondColumns
USING (row_num)
ORDER BY row_num ASC;


-- INNER JOIN 구를 통해서 이미 결과가 정렬이 되어있기 때문에 아래와 같이 ORDER BY 구를 굳이 사용하지 않아도 된다.

SELECT
    FirstColumns.first_col,
    SecondColumns.second_col
FROM (
    SELECT
        first_col,
        ROW_NUMBER() OVER(ORDER BY first_col ASC) AS row_num
    FROM Data
) AS FirstColumns
JOIN (
    SELECT
        second_col,
        ROW_NUMBER() OVER(ORDER BY second_col DESC) AS row_num
    FROM Data
) AS SecondColumns
USING (row_num)