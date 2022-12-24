-- [ LeetCode ] 2253. Dynamic Unpivoting of a Table

CREATE PROCEDURE UnpivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;

    SET @prepared_stmt = NULL;
    SELECT GROUP_CONCAT(CONCAT('SELECT product_id, "', column_name, '" AS store, ', column_name, ' AS price FROM Products WHERE ', column_name, ' IS NOT NULL') SEPARATOR ' UNION ') INTO @prepared_stmt
    FROM information_schema.columns
    WHERE (
        table_name = 'Products'
        AND
        column_name != 'product_id'
    );

    PREPARE stmt FROM @prepared_stmt;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END