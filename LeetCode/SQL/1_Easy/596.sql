-- [ LeetCode ] 596. Classes More Than 5 Students

/*
한 수업을 여러번 듣는 학생이 존재할 수 있기 때문에 DISTINCT 함수를 사용해줘야 한다.
처음 풀이 때는 COUNT(class) >= 5와 같이 조건을 걸었는데 student 필드를 COUNT 해주는 것이 훨씬 직관적이다.
*/

SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;
