-- [ LeetCode ] 1241. Number of Comments per Post

SELECT
    Post_Submissions.sub_id AS post_id,
    COUNT(DISTINCT Submissions.sub_id) AS number_of_comments
FROM Submissions AS Post_Submissions
LEFT JOIN Submissions AS Comment_Submissions
ON Post_Submissions.sub_id = Comment_Submissions.parent_id
WHERE Post_Submissions.parent_id IS NULL
GROUP BY Post_Submissions.sub_id
ORDER BY post_id ASC;


-- 아래와 같이 DISTINCT 및 서브쿼리를 활용하여 문제를 해결할 수도 있다.

SELECT
    DISTINCT sub_id AS post_id,
    (
        SELECT (COUNT DISTINCT sub_id)
        FROM Submissions AS Comment_Submissions
        WHERE Comment_Submissions.parent_id = Submissions.sub_id
    ) AS number_of_comments
FROM Submissions
WHERE parent_id IS NULL
ORDER BY post_id ASC;