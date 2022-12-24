-- [ LeetCode ] 1294. Weather Type in Each Country

SELECT
    country_name,
    CASE
        WHEN average_weather <= 15 THEN "Cold"
        WHEN average_weather >= 25 THEN "Hot"
        ELSE "Warm"
    END AS weather_type
FROM Countries
JOIN (
    SELECT
        country_id,
        AVG(weather_state) AS average_weather
    FROM Weather
    WHERE day BETWEEN "2019-11-01" AND "2019-11-30"
    GROUP BY country_id
) AS Grouped_Weater
USING (country_id);


/*
아래와 같이 YEAR, MONTH 함수를 활용하여 조건식을 작성할 수도 있다.
11월의 첫 시작이 1일인 것은 알지만 마지막 일이 30일인지 헷갈릴 수도 있기 때문에 조금 더 직관적이고 정확한 풀이라 생각된다.
*/

SELECT
    country_name,
    CASE
        WHEN average_weather <= 15 THEN "Cold"
        WHEN average_weather >= 25 THEN "Hot"
        ELSE "Warm"
    END AS weather_type
FROM Countries
JOIN (
    SELECT
        country_id,
        AVG(weather_state) AS average_weather
    FROM Weather
    WHERE (
        YEAR(day) = "2019"
        AND
        MONTH(day) = "11"
    )
    GROUP BY country_id
) AS Grouped_Weater
USING (country_id);
