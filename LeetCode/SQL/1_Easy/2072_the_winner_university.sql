-- [ LeetCode ] 2072. The Winner University

SELECT
    CASE
        WHEN (SELECT SUM(score >= 90) AS cnt FROM NewYork ) > (SELECT SUM(score >= 90) AS cnt FROM California)
        THEN "New York University"
        
        WHEN (SELECT SUM(score >= 90) AS cnt FROM NewYork ) < (SELECT SUM(score >= 90) AS cnt FROM California)
        THEN "California University"
        
        ELSE "No Winner"
    END AS winner;


-- 아래와 같이 WITH 구를 사용하는 게 보기에도 훨씬 좋고 깔끔하다.

WITH Counts AS (
    SELECT
        (SELECT SUM(score >= 90) FROM NewYork) AS Ny,
        (SELECT SUM(score >= 90) FROM California) AS Cali
)

SELECT
    CASE
        WHEN Ny > Cali THEN "New York University"
        WHEN Ny < Cali THEN "California University"
        ELSE "No Winner"
    END AS winner
FROM Counts;