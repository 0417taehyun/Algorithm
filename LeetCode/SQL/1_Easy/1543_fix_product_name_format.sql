-- [ LeetCode ] 1543. Fix Product Name Format

/*
아래와 같이 문자를 전부 소문자로 만들어주는 LOWER 함수, 앞뒤 공백을 전부 없애주는 TRIM 함수,
그리고 날짜 형식을 변경할 수 있는 DATE_FORMAT 함수를 사용하여 문제를 풀었다.

이때 유의해야 할 점은 우선 날짜 포맷에 있어 '%Y'와 '%y'는 다른 값을 반환하는데,
대문자 Y의 경우 `2020`과 같이 네 자리 수를 반환하며 소문자 y의 경우 `20`과 같이 앞의 두 자리 수를 반환한다.

또한 GROUP BY 구에서 `AS` 키워드를 사용한 별칭을 사용할 수 없기 때문에
실제 실행되는 함수인 LOWER(TRIM(product_name)) 및 DATE_FORMAT(sale_date, "%Y-%m") 표현을 직접 사용해줘야 한다.
*/

SELECT
    LOWER(TRIM(product_name)) AS product_name,
    DATE_FORMAT(sale_date, "%Y-%m") AS sale_date,
    COUNT(sale_id) AS total
FROM Sales
GROUP BY LOWER(TRIM(product_name)), DATE_FORMAT(sale_date, "%Y-%m")
ORDER BY product_name ASC, sale_date ASC;