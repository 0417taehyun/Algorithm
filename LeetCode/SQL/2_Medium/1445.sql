-- [ LeetCode ] 1445. Apples & Oranges

/*
예시를 확인해 보면 따로 동일한 날에 대해 과일이 아예 판매되지 않아 레코드가 누락된 경우 또한 `0`이라는 값으로 저장되기 때문에
여러 까다로운 제약조건들을 고민하지 않아도 된다는 걸 알 수 있다. 하지만 확장성을 고려했을 때 두 가지 고민을 해보면 좋다.

1. 레코드가 오류로 인해서 누락되는 경우도 존재할 수 있다.
2. 각 날에 대한 사과 및 오린제 판매량의 차이이기 때문에 테이블 내에 첫 시작하는 날을 기준으로 중간에 공백 기간 없이 오늘까지의 연속된 날짜로 계산해야 할 수도 있다.
*/

SELECT
    sale_date,
    SUM(IF(fruit="apples", sold_num, -sold_num)) AS diff
FROM Sales
GROUP BY sale_date
ORDER BY sale_date ASC;
