-- [ LeetCode ] 178. Rank Scores

/*
아래와 같이 윈도우 함수(Window Function)의 종류 중 하나인 DENSE_RANK 함수를 사용하여 문제를 풀었다.
이때 RANK 함수와 DENSE_RANK 함수의 차이점은 RANK 함수의 경우 동일한 순위가 존재하면 그 다음 순위가 동일한 순위의 수만큼 건너 뛰어서 넘버링이 되는데
DENSE_RANK 함수는 이어져서 넘버링이 되어 공백이 생기지 않는다는 점이다.

추가적으로 `rank`라는 필드이름은 기본적으로 RANK 함수 때문에 사용이 안 되어 따옴표를 붙여줘야 한다.
*/

SELECT
    score,
    DENSE_RANK() OVER(ORDER BY score DESC) AS 'rank'
FROM Scores;


/*
DENSE_RANK 함수를 사용하지 않을 경우 아래와 같이 문제를 해결할 수 있다.
해당 점수를 포함하여 해당 점수보다 높은 점수의 갯수를 카운트하면 그것이 곧 순위가 된다.
*/

SELECT
    Scores.score AS score,
    COUNT(Unique_Scores.score) AS 'rank'
FROM Scores
JOIN (
    SELECT DISTINCT score
    FROM Scores
) AS Unique_Scores
ON Scores.score <= Unique_Scores.score
GROUP BY id
ORDER BY score DESC;
