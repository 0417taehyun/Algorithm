-- [ LeetCode ] 1112. Highest Grade For Each Student

SELECT
    student_id,
    MIN(course_id) AS course_id,
    grade
FROM Enrollments
WHERE (student_id, grade) IN (
    SELECT
        student_id,
        MAX(grade)
    FROM Enrollments
    GROUP BY student_id
)
GROUP BY student_id
ORDER BY student_id ASC;


/*
아래와 같이 윈도우 함수(Window Function) 중 RANK 함수를 사용하여 문제를 해결할 수도 있었다.
외부에 GROUP BY 함수를 따로 더 안 써도 되기 때문에 훨씬 효율적일 것으로 판단된다.
*/

SELECT
    student_id,
    course_id,
    grade
FROM (
    SELECT
        student_id,
        course_id,
        grade,
        RANK() OVER(PARTITION BY student_id ORDER BY grade DESC, course_id ASC) AS rnk
    FROM Enrollments
) AS Ordered_Enrollments
WHERE rnk = 1
ORDER BY student_id ASC;