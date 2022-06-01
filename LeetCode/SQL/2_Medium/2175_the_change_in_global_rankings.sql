-- [ LeetCode ] 2175. The Change in Global Rankings

/*
RANK 윈도우 함수(Window Function)가 반환하는 값은 자연수이기 때문에 BIGINT UNSIGNED 자료형이다.
따라서 CAST 함수를 사용하여 그 결괏값의 자료형을 SIGNED 자료형으로 바꿔줘야 정수값을 얻을 수 있게 사칙연산이 가능하다.

RANK 윈도우 함수 외에도 ROW_NUMBER 등 어떤 특정 함수의 결괏값이 자연수만 반환하는 경우 자료형에 의해 사칙연산이 되지 않는 상황을 항상 고려해야겠다.
*/

SELECT
    TeamPoints.team_id,
    TeamPoints.name,
    (
        CAST(RANK() OVER(ORDER BY TeamPoints.points DESC, TeamPoints.name ASC) AS SIGNED)
        -
        CAST(RANK() OVER(ORDER BY (TeamPoints.points + PointsChange.points_change) DESC, TeamPoints.name ASC) AS SIGNED)
    ) AS rank_diff
FROM TeamPoints
JOIN PointsChange 
USING (team_id);
