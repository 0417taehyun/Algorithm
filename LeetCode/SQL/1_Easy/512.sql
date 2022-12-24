-- [ LeetCode ] 512. Game Play Analysis II

SELECT
    Activity.player_id AS player_id,
    Activity.device_id AS device_id
FROM Activity
LEFT JOIN Activity AS Joined_Table
ON (
    Activity.player_id = Joined_Table.player_id
    AND
    Activity.event_date > Joined_Table.event_date
)
WHERE Joined_Table.player_id IS NULL;


/*
아래와 같이 RANK 함수를 사용해서 해결할 수도 있다.
집계함수가 아닌 비집계함수 중 순위를 매기는 함수로 '분석함수'라 부른다.
그 종류에는 RANK 외에도 NTILE, DENSE_RANK, ROW_NUMBER 등이 있다.

RANK 함수는 선택사항으로 PARTION BY 구를, 필수적으로 OVER 및 ORDER BY 구를 함께 작성해야 한다.

OVER(...) AS rank_column_name과 같은 표현식으로 rank_column_name에 OVER() 구문을 통해 매겨진 순위를 반환한다.
PARTITION BY 구는 선택사항으로 동일 그룹으로 묶어줄 필드 명을 결정한다.
OVER 내에 사용된 ORDER BY 구를 통해서 랭킹을 매길 수 있게 어떤 컬럼을 어떤 기준으로 정렬할 것인지 결정한다.

아래 RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS rnk 구를 분석해보면 아래와 같다.
plyaer_id 필드를 기준으로 그룹화하여 순위를 매기는데 그 기준은 event_date 필드를 오름차순 정렬하고 이를 rnk라는 이름의 필드로 반환한다. 
*/

SELECT
    player_id,
    device_id
FROM (
    SELECT
        player_id,
        device_id
        RANK() OVER(PARTITION BY player_id ORDER BY event_date ASC) AS rnk
    FROM Activity
) AS Orderd_Table
WHERE rnk = 1;


/*
아래와 같이 WHERE 구의 조건으로 복수 필드를 설정하고 서브쿼리를 활용하여 문제를 해결할 수도 있다.
*/

SELECT
    player_id,
    device_id
FROM Activity
WHERE (player_id, event_date) IN (
    SELECT
        player_id,
        MIN(event_date)
    FROM Activity
    GROUP BY plyer_id
);