-- [ LeetCode ] 1280. Students and Examinations

/*
시간 내에 문제를 해결하지 못해서 다른 사람의 풀이를 참고했다.

MySQL에서 CROSS JOIN 구를 통해 합집합을 표현할 수 있다.
보통 합집합하면 UNION 키워드를 활용하여 두 개의 SELECT 구를 잇는 방법을 생각하기 마련인데,
UNION 키워드를 사용할 경우 수직 병합이 되기 때문에 컬럼의 수가 같아야 한다. 더욱이 UNION ALL이 아닌 UNION을 사용할 경우 중복값은 자동으로 제외된다.
반면에 CROSS JOIN 구를 사용할 경우 수평 병합이 되기 때문에 컬럼의 수가 같지 않아도 된다.

해당 문제에서는 학생이 시험을 보지 않은 과목에 대하여 `0`을 카운트해줘야 하는 것이 해결의 핵심 부분이었다.
이를 위해서 Students 테이블 및 Subjects 테이블을 CROSS JOIN 구를 통해 집합으로 만들고 이에 대해 Exminations 테이블을 LEFT JOIN 구를 활용해 통합하여,
학생 별로 모든 과목을 가진 테이블에 Examinations 테이블이 LEFT JOIN 되기 때문에 수강하지 않은 경우 COUNT 함수를 썼을 때 자동으로 `NULL` 값이 `0`으로 처리 된다.

추가적으로 INNER JOIN 구에 별다른 USING 또는 ON 키워드를 사용한 조건을 제시하지 않을 경우 CROSS JOIN 구를 사용한 것과 동일한 결괏값을 반환한다.
*/

SELECT
    Students.student_id AS student_id,
    student_name,
    Subjects.subject_name AS subject_name,
    COUNT(Examinations.subject_name) AS attended_exams
FROM Students
CROSS JOIN Subjects
LEFT JOIN Examinations
USING (student_id, subject_name)
GROUP BY student_id, subject_name
ORDER BY student_id, subject_name;