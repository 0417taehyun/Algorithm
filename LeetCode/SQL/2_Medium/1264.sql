-- [ LeetCode ] 1264. Page Recommendations

/*
아래와 같이 문제를 풀었는데 나와 똑같이 푼 사람의 풀이에 단 댓글을 보게 되었다.

1. NOT IN 구는 JOIN 구와 비교했을 때 훨씬 성능이 안 좋다. 기본 키(Primary Key)가 담긴 인덱스 테이블을 활용하지 않고 모든 데이터를 하나씩 비교해야 하기 때문이다.
2. OR 키워드가 UNION 키워드와 동일하게 작동하기 때문에 UNION 키워드를 사용하는 게 훨씬 좋다.
*/

SELECT DISTINCT page_id AS recommended_page
FROM Likes
WHERE (
    page_id NOT IN (
        SELECT page_id
        FROM Likes
        WHERE user_id = 1
    )
    AND
    user_id IN (
        SELECT IF(user1_id = 1, user2_id, user1_id) AS user_id
        FROM Friendship
        WHERE (
            user1_id = 1
            OR
            user2_id = 1
        )
    )
);


/*
전체적인 제출 결과는 NOT IN 문법을 사용하는 것보다 아래와 같이 JOIN 구를 사용하는 게 훨씬 빨랐다.
대신 MySQL에서는 DISTINCT 키워드가 결국 정렬을 행하지 않고 GROUP BY 구는 정렬을 행하기 때문에 이 부분에 있어 결론적으로는 비슷한 성능을 보이는 것 같다.
다시 말해 JOIN 구를 사용하여 NOT IN 문법을 사용하는 경우보다 성능상의 이점을 가져간다 하더라도 DISTINCT 키워드 대신에 GROUP BY 구를 사용해야 하기 때문에 성능은 비슷해지는 것이다.
*/

SELECT page_id AS recommended_page
FROM Likes
JOIN (
    SELECT user2_id AS user_id
    FROM Friendship
    WHERE user1_id = 1
    UNION
    SELECT user1_id AS user_id
    FROM Friendship
    WHERE user2_id = 1
) AS SpecificUser
USING (user_id)
JOIN Likes AS SubLikes
USING (page_id)
GROUP BY page_id
HAVING SUM(IF(SubLikes.user_id = 1, TRUE, FALSE)) = FALSE;
