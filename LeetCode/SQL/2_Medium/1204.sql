-- [ LeetCode ] 1204. Last Person to Fit in the Bus

SELECT person_name
FROM (
    SELECT
        Queue.person_name AS person_name,
        SUM(PreviousPerson.weight) AS current_weight
    FROM Queue
    JOIN Queue AS PreviousPerson
    ON Queue.turn >= PreviousPerson.turn
    GROUP BY Queue.turn
) AS TotalWeigth
WHERE current_weight <= 1000
ORDER BY current_weight DESC
LIMIT 1;


-- 아래와 같이 SUM 윈도우 함수(Window Function)을 사용하여 축적된 합을 구할 수 있다.

SELECT person_name
FROM (
    SELECT
        person_name,
        SUM(weight) OVER(ORDER BY turn ASC) AS current_weight  
    FROM Queue
    ORDER BY current_weight DESC
) AS TotalWeigth
WHERE current_weight <= 1000
LIMIT 1;
