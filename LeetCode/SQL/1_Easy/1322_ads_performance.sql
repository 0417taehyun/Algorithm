-- [ LeetCode ] 1322. Ads Performance

/*
IFNULL 함수의 경우 두 개의 인자만 받게 되어 만약 첫 번째 인자의 값이 `NULL`이 아닐 경우 그대로 반환하고 `NULL`일 경우 두 번째 인자의 값을 반환한다.
COALESCE 함수의 경우 여러 인자를 받아서 가장 먼저 마주하게 되는 `NULL`이 아닌 값을 반환하게 된다.
따라서 아래 답변에서는 ROUND 함수로 묶인 구가 `NULL` 값을 반환할 경우 자동으로 그 다음 값이 `NULL`이 아닌 `0.00`이기 때문에 `0.00`을 반환한다.

이때 SUM 함수는 COUNT 함수와 달리 내부 조건에 따라서 합산하는 로우(Row)를 결정할 수 있기 때문에 SUM 함수를 사용하였고,
action="Clicked"과 같은 조건을 통해서 해당 BOOL 형태의 값은 TRUE일 경우 1, FALSE일 경우 0을 반환하기 때문에 이를 바탕으로 계산할 수 있다.
추가적으로 0을 분모로 해서 나눌 경우 자동으로 `NULL` 값을 반환하기 때문에 따로 DIVISION ERROR와 같은 예외 사항은 생각하지 않아도 된다.

** 추가
ERROR_FOR_DIVISON_BY_ZEOR의 경우 SQL 모드에 관한 사항이다.
자세한 내용은 1435. Create A Session Bar Chart 문제를 확인하면 된다.
*/

SELECT
    ad_id,
    COALESCE(ROUND(SUM(action="Clicked") / SUM(action <> "Ignored") * 100, 2), 0.00) AS ctr
FROM Ads
GROUP BY ad_id
ORDER BY ctr DESC, ad_id ASC;