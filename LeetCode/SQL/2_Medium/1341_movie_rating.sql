-- [ LeetCode ] 1341. Movie Rating

/*
UNION 혹은 UNION ALL 키워드를 사용하기 이전에 ORDER BY 및 LIMIT 키워드, 다시 말해 SELECT 구 다음에 실행되는 것들을 사용하지 못한다.
왜냐하면 MySQL에서 쿼리 실행 순서가 다음과 같기 때문이다.

... SELECT > DISTINCT > UNION > ORDER BY > LIMIT

그래서 아래와 같이 서브쿼리를 사용하여 문제를 해결했다. 실행 순서를 잊지 말아야겠다.
*/

SELECT results
FROM (
    SELECT Users.name AS results
    FROM MovieRating
    JOIN Users
    USING (user_id)
    GROUP BY MovieRating.user_id
    ORDER BY COUNT(movie_id) DESC, Users.name ASC
    LIMIT 1
) AS GreatestUser
UNION
SELECT results
FROM (
    SELECT Movies.title AS results
    FROM MovieRating
    JOIN Movies
    USING (movie_id)
    GROUP BY MovieRating.movie_id
    ORDER BY AVG(IF(YEAR(created_at) = 2020 AND MONTH(created_at) = 2, rating, NULL)) DESC, Movies.title ASC
    LIMIT 1
) AS HighestRatingMovie;
