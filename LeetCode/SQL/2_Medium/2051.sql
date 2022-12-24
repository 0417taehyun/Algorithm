-- [ LeetCode ] 2051. The Category of Each Member in the Store

/*
COUNT 함수의 경우 NULL 값에 대한 처리를 별도로 하지 않기 때문에 NULL 값만 있는 경우 결국 NULL 값을 반환한다.
또한 어떤 수와 NULL 값을 연산하는 경우 그 결과는 해당 수를 무시하고 `NULL`이된다.
*/

WITH cte (member_id, name, conversion_rate) AS (
    SELECT
        Members.member_id,
        Members.name,
        (100 * COUNT(Purchases.visit_id)) / COUNT(Visits.visit_id) AS conversion_rate
    FROM Members
    LEFT JOIN Visits
    USING (member_id)
    LEFT JOIN Purchases
    USING (visit_id)
    GROUP BY Members.member_id
)

SELECT
    member_id,
    name,
    CASE
        WHEN conversion_rate IS NULL THEN 'Bronze'
        WHEN conversion_rate >= 80 THEN 'Diamond'
        WHEN conversion_rate >= 50 THEN 'Gold'
        ELSE 'Silver'
    END AS category
FROM cte;
