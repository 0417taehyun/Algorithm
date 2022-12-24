-- [ LeetCode ] 1097. Game Play Analysis V

/*
문제를 풀 때 유의했어야 했던 점은 AVG 함수가 NULL 값은 무시한다는 것과
player_id 필드의 평균 값이 아닌 개수의 평균을 구해야 하는 개념이기 때문에 IF 함수를 써서 NULL 값이 아닌 경우 `1`로 변환해줘야 하는 것이었다.
*/

SELECT
    InstallDates.install_dt,
    COUNT(InstallDates.player_id) AS installs,
    ROUND(AVG(IF(Activity.player_id IS NULL, 0, 1)), 2) AS Day1_retention
FROM (
    SELECT
        player_id,
        MIN(event_date) AS install_dt
    FROM Activity
    GROUP BY player_id
) AS InstallDates
LEFT JOIN Activity
ON (
    InstallDates.player_id = Activity.player_id
    AND
    DATEDIFF(Activity.event_date, InstallDates.install_dt) = 1
)
GROUP BY InstallDates.install_dt;
