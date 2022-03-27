-- [ LeetCode ] 1113. Reported Posts

-- 아래와 같이 GROUP BY 구 전에 WHERE 구를 사용할 수 있다.

SELECT
    extra AS report_reason,
    COUNT(extra) AS report_count
FROM (
    SELECT DISTINCT post_id, extra
    FROM Actions
    WHERE (
        action = "report"
        AND
        DATEDIFF("2019-07-05", action_date) = 1
    )
) AS Unique_Actions
GROUP BY extra;


-- 아래와 같이 extra 필드를 기준으로 그룹화하고 중복을 제거한 post_id 필드에 COUNT 함수를 사용하여 문제를 훨씬 더 간단하게 해결할 수 있다.

SELECT
    extra AS report_reason,
    COUNT(DISTINCT post_id) AS report_count
FROM Actions
WHERE (
    DATEDIFF("2019-07-05", action_date) = 1
    AND
    action = "report"
)
GROUP BY extra;