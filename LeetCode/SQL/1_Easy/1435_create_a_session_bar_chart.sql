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

집계(Aggregation) 관련하여 따옴표(Quotation) 관련된 문제가 있는 것인지 궁금했다.
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
이때 유의할 점은 GROUP BY 구에 참조하려는 별칭의 값을 식별자 따옴표(Indentifier Quoting)인 백틱(``)을 사용해주지 않을 경우 문자열 리터럴(String Literals)로 인지해서 오류가 발생한다.

그렇다면 GROUP BY 구에서 결국 컬럼 별칭을 사용할 수 있는데 어째서 `GROUP BY "bin"`과 같은 형태로 문자열 리터럴을 사용한 경우에도 문법적 오류 없이 쿼리 자체가 실행(Execution)은 된 것일까?
이유는 바로 MySQL에서 설정할 수 있는 서버 SQL 모드(Server SQL Mode)에 있다.

기본적으로 `SELECT @@global.sql_mode` 쿼리를 통해 현재 사용 중인 SQL 모드의 리스트를 확인할 수 있는데 LeetCode 홈페이지 내에서 사용할 경우 빈 배열이 반환되고 로컬 환경에서 사용할 경우,
[ ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION ]와 같은 배열이 반환되었다.

여기서 우리가 주목해야 할 부분은 바로 ONLY_FULL_GROUP 부분이다.
기본적으로 해당 모드는 켜져있는데, 만약 ONLY_FULL_GROUP 모드가 켜져 있다면
MySQL은 SELECT 구, HAVING 구에서의 조건, 그리고 ORDER BY 구에서의 정렬 기준에 집계 되지 않은 컬럼(Nonaggregated Column)을 사용하려 할 때 해당 쿼리를 거절하고 오류를 반환한다.
그래서 만약 로컬 환경에서 문제가 되었던 `GROUP BY "bin"` 구문을 실행하면 아래와 같은 오류를 반환한다.

ERROR 1055 (42000): Expression #1 of SELECT list is not in GROUP BY clause and contains
nonaggregated column 'test.Sessions.duration' which is not functionally dependent on columns in GROUP BY clause;
this is incompatible with sql_mode=only_full_group_by

`GROUP BY bin` 또는 `GROUP BY `bin``과 같은 표현의 경우 사용 가능한 이유는 결국
CASE 구의 표현의 별칭 자체가 집계 함수와 연관되어 있는 부분이기 때문이다.
다만, `GROUP BY "bin"`과 같은 표현에서 오류가 발생한 이유는 GROUP BY 구가 해당 문자열 리터럴(String Literal)을 읽었기 때문에 존재하지 않는 것을 기준으로 그룹화를 시도했고
그 과정에서 CASE 구에 들어 있는 duration 필드가 GROUP BY 구와 연관되어 있지 않기 때문에 오류를 발생시켰다.

만약 ONLY_FULL_GROUP_BY 모드가 꺼져있을 경우,
다시 말해 LeetCode에서는 bin 필드에 대한 값으로 `"[0-5>"`, total 필드에 대한 값으로 5를 반환했는데
GROUP BY 구가 작동하지 않고, 또한 그 기준과 CASE 구에서 사용한 duration 필드가 연관이 없더라도
단순히 COUNT 함수를 통해 전체 session_id 필드를 셈하고 가장 첫 번째 열(Row)의 duration 필드 값을 통해 CASE 구가 적용되어 `"[0-5"` 값이 반환되었다.

ONLY_FULL_GROUP_BY 모드가 꺼져 있을 경우 MySQL은 내부적으로 어떤 값을 선택해야할 지 모르기 때문에 무작위로 반환한다.
예를 들어 아래와 같은 Users 테이블이 존재한다고 가정해보자.

+----+------+
| id | name |
+----+------+
|  1 | ali  |
|  2 | john |
|  3 | ali  |
+----+------+

`SELECT id, name FROM Users GROUP BY name;`과 같이 쿼리를 실행하면 내부적으로 랜덤하게 값을 뽑아와서 아래와 같이 반환한다.

+----+------+
| id | name |
+----+------+
|  1 | ali  |
|  2 | john |
+----+------+

이때 `SET GLOBAL sql_mode=(SELECT REPLACE(@@sql_mode, 'ONLY_FULL_GROUP_BY', ''))`와 같이 형태로 원하는 SQL 모드를 끌 수 있다.
`SET GLOBAL sql_mode='...'`와 같은 형태로 다시 SQL 모드를 추가할 수 있는데, 이는 기존에 존재하던 모든 것을 지우고 ...에 들어가는 값으로 대체하는 것이기 때문에 기존에 있던 것에 추가만 하기를 원한다면 위 REPLACE 함수 대신
CONCAT 함수를 사용하여 `SET GLOBAL sql_mode=(SELECT CONCAT(@@sql_mode, 'ONLY_FULL_GROUP_BY'))`와 같은 형태로 쿼리를 실행하면 된다.
`SELECT @@session.sql_mode` 또는 `SELECT @@global.sql_mode`와 같은 쿼리를 통해 각각 세션 및 글로벌에서 켜져있는 SQL 모드를 조회할 수 있다.

참고로 1322. Ads Performance 문제에서 `0` 값으로 정수를 나눴는데 오류가 발생하지 않고 `NULL` 값이 반환된 이유도
위 모드 종류 중 ERROR_FOR_DIVISION_BY_ZERO 모드가 LeetCode 내에서 켜져 있지 않았기 때문이다.
로컬에서 `SELECT 2/0`과 같은 쿼리를 실행할 경우 쿼리 자체는 실행이 되고 값으로 `NULL`을 반환 받지만
`SHOW WARNINGS` 쿼리를 실행해보면 아래와 같이 `Division by 0`라는 메세지가 주의로 뜬 것을 확인할 수 있다.

+---------+------+---------------+
| Level   | Code | Message       |
+---------+------+---------------+
| Warning | 1365 | Division by 0 |
+---------+------+---------------+

추가로 홑 따옴표(Single Quotation)와 쌍 따옴표(Double Quotation)의 차이점에 대한 부분이다.
홑 따옴표의 경우 문자열 리터럴(String Literals) 또는 날짜 리터럴(Date Literals)에 주로 사용된다. 즉, 문자열(String) 또는 텍스트(Text)와 같은 실제 데이터에 사용된다.
쌍 타옴표의 경우 데이터베이스 식별자(Database Identifier)에 주로 사용된다. 즉, 다시 말해 컬럼이나 테이블의 이름으로 사용된다.
쿼리를 통해 예를 들면 아래와 같다.

INSERT INTO "USERS" ("LOGIN", "PASSWORD", "DT_BIRTH")
VALUES 'EDUARDO', '12345678', '1980-09-06');

MySQL에서는 백틱(``)이 쌍 따옴표와 동일하게 동작하는데
만약 SQL 모드 중 ANSI_QUOTES가 켜져있다면 쌍 따옴표를 문자열 리터럴(String Literals)에 사용할 수 없다. 기본적으로 ANSI_QUOTES는 꺼져있다.
SQL 모드에 대한 더 자세한 설명은 공식 문서 [5.1.11 Server SQL Modes](https://dev.mysql.com/doc/refman/8.0/en/sql-mode.html#sqlmode_only_full_group_by)에서 확인 가능하다.
*/