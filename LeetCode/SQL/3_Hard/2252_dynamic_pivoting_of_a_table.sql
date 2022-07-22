-- [ LeetCode ] 2252. Dynamic Pivoting of a Table

/*
프로시저(Procedure)는 여러 쿼리를 한번에 사용할 수 있게 한다.

GROUP_CONCATE 함수를 활용해서 동적으로 모든 store 필드에 대한 피벗 구를 문자열로 만든다.
이때 DISTINCT 키워드를 사용한 이유는 동일한 store 필드에 대해 여러 구가 중복되어 생성되지 않게 하기 위함이다.

이후 GROUP_CONCAT 함수를 사용한 구를 변수에 할당한 뒤 이를 다시 CONCAT 함수를 사용하여 해당 변수와 함께 문자열로 피벗 테이블 생성 구를 만든다.
끝으로 해당 구를 저장한 변수를 PREPARE 구를 활용하여 작동시키면 된다.

PREPARE 구는 문자열로 작성된 구를 받은 뒤에 이를 EXECUTE 구를 활용해 실질적으로 실행시키고 DEALLOCATE 구를 통해 해제한다.

한 가지 유의할 점은 GROUP_CONCAT 함수의 기본적인 문자열 수 제한 값은 1024이기 때문에 SET SESSION 구를 활용해 제한을 늘려주는 부분이다.
*/

CREATE PROCEDURE PivotProducts()
BEGIN
    SET SESSION group_concat_max_len = 1000000;

    SET @store_stmt = NULL;

    SELECT GROUP_CONCAT(DISTINCT CONCAT('SUM(IF(store = "', store, '", price, NULL)) AS ', store)) INTO @store_stmt
    FROM Products;

    SET @prepared_stmt = CONCAT('SELECT product_id, ', @store_stmt, ' FROM Products GROUP BY product_id');

    PREPARE stmt FROM @prepared_stmt;
    EXECUTE stmt;
    DEALLOCATE PREPARE stmt;
END
