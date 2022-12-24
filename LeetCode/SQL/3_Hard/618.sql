-- [ LeetCode ] 618. Students Report By Geography

/*
수평결합이 핵심이기 때문에 LEFT JOIN 구를 사용했다.
이때 name 필드를 알파벳 순으로 정렬해서 수평결합을 해야하기 때문에 ROW_NUMBER 윈도우 함수(Window Function)를 사용해서 LEFT JOIN 구의 결합 조건으로 사용했다.
*/

WITH Students (row_num, name, continent) AS (
    SELECT
        ROW_NUMBER() OVER(PARTITION BY continent ORDER BY name ASC) AS row_num,
        name,
        continent
    FROM Student
)

SELECT
    AmericaStudents.name AS America,
    AsiaStudents.name AS Asia,
    EuropeStudents.name AS Europe
FROM (
    SELECT
        row_num,
        name
    FROM Students
    WHERE continent = 'America'
) AS AmericaStudents
LEFT JOIN (
    SELECT
        row_num,
        name
    FROM Students
    WHERE continent = 'Asia'
) AS AsiaStudents
USING (row_num)
LEFT JOIN (
    SELECT
        row_num,
        name
    FROM Students
    WHERE continent = 'Europe'
) AS EuropeStudents
USING (row_num);


-- 아래와 같이 서브쿼리 부분 자체를 WITH 구로 대체할 수 있다.

WITH AmericaStudents (row_num, name) AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY name ASC) AS row_num,
        name
    FROM Student
    WHERE continent = 'America'
), AsiaStudents (row_num, name) AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY name ASC) AS row_num,
        name
    FROM Student
    WHERE continent = 'Asia'
), EuropeStudents (row_num, name) AS (
    SELECT
        ROW_NUMBER() OVER(ORDER BY name ASC) AS row_num,
        name
    FROM Student
    WHERE continent = 'Europe'
)

SELECT
    AmericaStudents.name AS America,
    AsiaStudents.name AS Asia,
    EuropeStudents.name AS Europe
FROM AmericaStudents
LEFT JOIN AsiaStudents
USING (row_num)
LEFT JOIN EuropeStudents
USING (row_num);
