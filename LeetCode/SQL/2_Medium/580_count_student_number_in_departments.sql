-- [ LeetCode ] 580. Count Student Number in Departments

SELECT
    dept_name,
    COUNT(student_id) AS student_number
FROM Department
LEFT JOIN Student
USING (dept_id)
GROUP BY dept_id
ORDER BY student_number DESC, dept_name ASC;
