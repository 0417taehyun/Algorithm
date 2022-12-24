-- [ LeetCode ] 1809. Ad-Free Sessions

SELECT session_id
FROM Playback
WHERE session_id NOT IN (
    SELECT
        DISTINCT session_id
    FROM Playback
    JOIN Ads
    ON (
        Playback.customer_id = Ads.customer_id
        AND
        Ads.timestamp BETWEEN Playback.start_time AND Playback.end_time
    )
);

/*
처음에는 위와 같이 문제를 풀었는데 생각해보니 LEFT JOIN 구를 사용했기 때문에
조건에 맞지 않으면 결합된 Ads 테이블 쪽 값이 `NULL`이 되기 때문에
굳이 서브쿼리로 따로 빼지 않아도 쉽게 문제가 해결되는 것이었다.

따라서 아래와 같이 WHERE 구를 통해 Ads 테이블 쪽 필드의 값이 `NULL`인 경우만 조회하면 된다.
*/

SELECT session_id
FROM Playback
LEFT JOIN Ads
ON (
    Playback.customer_id = Ads.customer_id
    AND
    Ads.timestamp BETWEEN Playback.start_time AND Playback.end_time
)
WHERE Ads.ad_id IS NULL;