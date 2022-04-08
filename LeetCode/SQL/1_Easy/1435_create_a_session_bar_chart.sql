-- [ LeetCode ] 1435. Create a Session Bar Chart

SELECT
    Bins.bin AS bin,
    COUNT(Visiting_Time.bin) AS total
FROM (
    SELECT
        CASE
            WHEN (duration DIV 60) BETWEEN 0 AND 4 THEN "[0-5>"
            WHEN (duration DIV 60) BETWEEN 5 AND 9 THEN "[5-10>"
            WHEN (duration DIV 60) BETWEEN 10 AND 14 THEN "[10-15>"
            ELSE "15 or more"
        END AS bin
    FROM Sessions
) AS Visiting_Time
RIGHT JOIN (
    SELECT "[0-5>" AS bin
    UNION
    SELECT "[5-10>"
    UNION
    SELECT "[10-15>"
    UNION
    SELECT "15 or more"
) AS Bins
USING (bin)
GROUP BY (Bins.bin)


/*
아래와 같이 WITH 구문을 사용하여 해결 가능하다.
이떄 duration 필드의 자료형이 `INT`이기 때문에 그 최댓값이 2^31 - 1인 것을 알 수 있다.

문제를 해결할 때 해당 필드의 자료형도 꼼꼼하게 살펴보는 게 좋을 것 같다.
*/

WITH cte AS (
    SELECT "[0-5>" AS bin, 0 AS min_duration, 5*60 AS max_duration
    UNION ALL
    SELECT "[5-10>" AS bin, 5*60 AS min_duration, 10*60 AS max_duration
    UNION ALL
    SELECT "[10-15>", 10*60 AS min_duration, 15*60 AS max_duration
    UNION ALL
    SELECT "15 or more", 15*60 AS min_duration, POWER(2, 31) AS max_duration
)

SELECT
    bin,
    COUNT(session_id) AS total
FROM cte
LEFT JOIN Sessions
ON duration BETWEEN min_duration AND (max_duration - 1)
GROUP BY bin



-- 기타

/*
LeetCode 환경에서는 GROUP BY 구에 SELECT 구에서 사용한 별칭(Alias)을 사용할 수 있었다.
기본적으로 SQL 쿼리를 실행할 때 결정되어 있는 구의 순서가 GROUP BY가 SELECT보다 우선인데 이것이 가능한 이유가 궁금했다.

더욱이 문제는 아래 세 쿼리문에서 첫 번째와 두 번째 경우는 정상적으로 CASE 별 COUNT 함수가 적용이 되었고,
아래는 적용되지 않고 전체를 COUNT 했다.

집계(Aggregation) 관련하여 따옴포(Quotation) 관련된 문제가 있는 것인지 궁금했다.
*/

SELECT
    CASE
        WHEN (duration DIV 60) BETWEEN 0 AND 4 THEN "[0-5>"
        WHEN (duration DIV 60) BETWEEN 5 AND 9 THEN "[5-10>"
        WHEN (duration DIV 60) BETWEEN 10 AND 14 THEN "[10-15>"
        ELSE "15 or more"
    END AS bin,
    COUNT(session_id) AS total
FROM Sessions
GROUP BY bin

SELECT
    CASE
        WHEN (duration DIV 60) BETWEEN 0 AND 4 THEN "[0-5>"
        WHEN (duration DIV 60) BETWEEN 5 AND 9 THEN "[5-10>"
        WHEN (duration DIV 60) BETWEEN 10 AND 14 THEN "[10-15>"
        ELSE "15 or more"
    END AS bin,
    COUNT(session_id) AS total
FROM Sessions
GROUP BY `bin`

SELECT
    CASE
        WHEN (duration DIV 60) BETWEEN 0 AND 4 THEN "[0-5>"
        WHEN (duration DIV 60) BETWEEN 5 AND 9 THEN "[5-10>"
        WHEN (duration DIV 60) BETWEEN 10 AND 14 THEN "[10-15>"
        ELSE "15 or more"
    END AS bin,
    COUNT(session_id) AS total
FROM Sessions
GROUP BY "bin"

/*
우선 앞서 말했듯 SQL에서는 기본적으로 GROUP BY 구의 순서가 SELECT 구보다 우선된다.
모든 구에 대한 실행 순서는 아래와 같다.

1. FROM
2. ON
3. JOIN
4. WHERE
5. GROUP BY
6. WITH CUBE or WITH ROLLUP
7. HAVING
8. SELECT
9. DISTINCT
10. ORDER BY
11. TOP


위 두 쿼리에 각각 EXPLAIN ANALYZE 구를 활용해 실행계획을 출력해보면 아래와 같았다.

먼저 `GROUP BY bin`과 같은 형태는 아래와 같이 임시 테이블(Temporary Table)을 스캔(Scan)하는 것을 볼 수 있다.

-> Table scan on <temporary>  (actual time=0.000..0.001 rows=3 loops=1)
-> Aggregate using temporary table  (actual time=0.046..0.047 rows=3 loops=1)
-> Table scan on Sessions  (cost=0.75 rows=5) (actual time=0.011..0.015 rows=5 loops=1)

그러나 `GROUP BY "bin"` 과 같은 형태는 곧바로 `GROUP aggregate`를 실행하는 것을 볼 수 있다.

-> Group aggregate: count(sessions.session_id)  (actual time=0.017..0.017 rows=1 loops=1)
-> Table scan on Sessions  (cost=0.75 rows=5) (actual time=0.009..0.012 rows=5 loops=1)


그렇다면 이와 같은 차이가 발생하는 이유는 무엇일까?

관련해서 우선 MySQL 공식 문서에 아래와 같이 두 글을 봐보자.

- [B.3.4.4 Problems with Column Aliases](https://dev.mysql.com/doc/refman/8.0/en/problems-with-alias.html),
- [12.20.3 MySQL Handling of GROUP BY](https://dev.mysql.com/doc/refman/8.0/en/group-by-handling.html)

위에서 발생하는 이유에 대해 설명해준 문서인데 요약하자면,
표준 SQL(Standard SQL)은 컬럼 별칭(Column Alias)이 결정되기 이전에 참조하는 것을 허용하지 않지만 GROUP BY 구문에서는 가능하다는 것이다. 
이때 유의할 점은 GROUP BY 구에 참조하려는 별칭의 값을 식별자 따옴표(Indentifier Quoting)인 백틱(``)을 사용해주지 않을 경우 문자열 리터럴(Literal String)로 인지해서 오류가 발생한다.


*/