-- [ LeetCode ] 1308. Running Total for Different Genders

SELECT
    Scores.gender AS gender,
    Scores.day AS day,
    SUM(PreviousGames.score_points) AS total
FROM Scores
JOIN Scores AS PreviousGames
ON (
    Scores.gender = PreviousGames.gender
    AND
    Scores.day >= PreviousGames.day
)
GROUP BY gender, day
ORDER BY gender, day;


/*
아래와 같이 SUM 윈도우 함수(Window Function)를 사용하는 게 훨씬 빠르고 좋다.
gender 및 day 필드가 기본 키(Primary Key)이기 때문에 gender 기준으로 PARTITION BY 키워드를 통해 그룹화해줘도 문제를 해결할 수 있다.
*/

SELECT
    gender,
    day,
    SUM(score_points) OVER(PARTITION BY gender ORDER BY day) AS total
FROM Scores
ORDER BY gender, day;
