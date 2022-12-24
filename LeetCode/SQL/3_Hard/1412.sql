-- [ LeetCode ] 1412. Find the Quiet Students in All Exams

SELECT
    DISTINCT Student.student_id,
    Student.student_name
FROM Student
JOIN Exam
USING (student_id)
LEFT JOIN (
    SELECT DISTINCT student_id
    FROM (
        SELECT
            student_id,
            DENSE_RANK() OVER(PARTITION BY exam_id ORDER BY score DESC) AS highest_rank,
            DENSE_RANK() OVER(PARTITION BY exam_id ORDER BY score ASC) AS lowest_rank
        FROM Exam
    ) AS ExamRank
    WHERE (
        highest_rank = 1
        OR
        lowest_rank = 1
    )
) AS NotQuietStudent
USING (student_id)
WHERE NotQuietStudent.student_id IS NULL
ORDER BY student_id ASC;
