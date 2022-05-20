-- [ LeetCode ] 1699. Number of Calls Between Two Persons

SELECT
    from_id AS person1,
    to_id AS person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration
FROM (
    SELECT
        IF(from_id > to_id, to_id, from_id) AS from_id,
        IF(from_id > to_id, from_id, to_id) AS to_id,
        duration
    FROM Calls
) AS FormattedCalls
GROUP BY from_id, to_id;


/*
MySQL에서 GROUP BY 구는 SELECT 구가 실행되기 이전에 실행되지만 SELECT 구에서 사용하는 별칭(Alias)을 사용할 수 있다.
그래서 아래와 같이 서브쿼리를 사용하지 않더라도 문제를 해결할 수 있다.
*/

SELECT
    IF(from_id > to_id, to_id, from_id) AS person1,
    IF(from_id > to_id, from_id, to_id) AS person2,
    COUNT(duration) AS call_count,
    SUM(duration) AS total_duration
FROM Calls
GROUP BY person1, person2;
