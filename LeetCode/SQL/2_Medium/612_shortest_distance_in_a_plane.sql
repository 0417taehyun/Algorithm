-- [ LeetCode ] 612. Shortest Distance in a Plane

SELECT
    ROUND(MIN(SQRT(
        POWER(GREATEST(Point2D.x, OtherPoints.x) - LEAST(Point2D.x, OtherPoints.x), 2)
        +
        POWER(GREATEST(Point2D.y, OtherPoints.y) - LEAST(Point2D.y, OtherPoints.y), 2)
    )), 2) AS shortest
FROM Point2D
JOIN Point2D AS OtherPoints
ON NOT (
    Point2D.x = OtherPoints.x
    AND
    Point2D.y = OtherPoints.y
);


/*
아래와 같이 ST_DISTANCE 및 POINT 함수를 사용하여 문제를 간단하게 해결할 수 있다.
예전에 Geo Location 관련된 연산을 위해 데이터베이스를 선택할 때 MySQL보다 PostgreSQL이 더 뛰어나다는 글을 읽은 적이 있는데
내부적으로 위치 계산을 위해 ST_DISTANCE 및 POINT 함수 같은 기능을 제공해주는 것 같다.
POINT 함수를 통해 x 및 y 필드를 하나의 좌표로 만들어주고 해당 두 좌표의 거리를 ST_DISTANCE 함수를 사용하여 간단하게 구할 수 있다.

FROM 구에 두 테이블을 사용하였는데 위 풀이처럼 JOIN 구를 써야하는 상황에
FROM 구에 단순히 두 테이블을 열거하는 게 더 성능이 좋지는 않을지 고민을 해보면 좋을 것 같다.
*/

SELECT ROUND(MIN(ST_DISTANCE(POINT(A.x, A.y), POINT(B.x, B.y))), 2) AS shortest
FROM (
    Point2D AS A,
    Point2D AS B
)
WHERE (
    A.x <> B.x
    OR
    A.y <> B.y
);