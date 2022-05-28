-- [ LeetCode ] 1988. Find Cutoff Score for Each School

SELECT
    school_id,
    IFNULL(MIN(score), -1) AS score
FROM (
    SELECT
        Schools.school_id,
        Exam.score,
        DENSE_RANK() OVER(PARTITION BY Schools.school_id ORDER BY Exam.student_count DESC) AS student_count_rank
    FROM Schools
    LEFT JOIN Exam
    ON Schools.capacity >= Exam.student_count
) AS ScoreRequirements
WHERE student_count_rank = 1
GROUP BY school_id;


/*
테이블에 대한 설명에서 Exam 테이블에 대해 논리적인 보장이 되어 있는 부분을 잘 읽으면 아래와 같이 쉽게 해결 가능하다.
Exam 테이블 내에서 score 필드의 값이 더 클 경우 student_count 필드의 값이 크거나 같다는 게 논리적으로 보장되어 있다.
따라서 단순히 LEFT JOIN 구를 실행한 이후 가장 작은 score 필드의 값만 반환하더라도 결국 student_count 필드의 값이 가장 크게 된다.
*/

SELECT
    Schools.school_id,
    MIN(IFNULL(score, -1)) AS score
FROM Schools
LEFT JOIN Exam
ON Schools.capacity >= Exam.student_count
GROUP BY Schools.school_id;
