-- [ LeetCode ] 1459. Rectangles Area

SELECT
    Points.id AS p1,
    SubPoints.id AS p2,
    ABS(Points.x_value - SubPoints.x_value) * ABS(Points.y_value - SubPoints.y_value) AS area
FROM Points
JOIN Points AS SubPoints
ON (
    Points.id < SubPoints.id
    AND
    Points.x_value <> SubPoints.x_value
    AND
    Points.y_value <> SubPoints.y_value
)
ORDER BY area DESC, p1 ASC, p2 ASC;