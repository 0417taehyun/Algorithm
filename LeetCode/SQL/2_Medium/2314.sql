-- [ LeetCode ] 2314. The First Day of the Maximum Recorded Degree in Each City

SELECT
    city_id,
    day,
    degree
FROM (
    SELECT
        city_id,
        day,
        degree,
        RANK() OVER(PARTITION BY city_id ORDER BY degree DESC, day ASC) AS weather_rank
    FROM Weather
) AS WeatherRanks
WHERE weather_rank = 1
ORDER BY city_id ASC;
