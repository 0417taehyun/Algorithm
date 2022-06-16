-- [ LeetCode ] 2308. Arrange Table by Gender

-- ORDER BY 순서에 따른 행의 정렬 방식을 헷갈리지 말자.

SELECT
    user_id,
    gender
FROM (
    SELECT
        user_id,
        gender,
        ROW_NUMBER() OVER(PARTITION BY gender ORDER BY user_id ASC) AS id_order,
        CASE gender
            WHEN 'female' THEN 1
            WHEN 'other' THEN 2
            ELSE 3
        END AS gender_order
    FROM Genders
) AS OrderedGenders
ORDER BY id_order ASC, gender_order ASC;
