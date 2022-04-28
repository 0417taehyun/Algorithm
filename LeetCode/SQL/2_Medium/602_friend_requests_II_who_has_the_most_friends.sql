-- [ LeetCode ] 602. Friend Requests II: Who Has the Most Friends

/*
처음에 INNER JOIN을 사용해서 문제를 해결했는데 통과하지 못한 테스트 케이스가 존재했다.
예를 들어 아래와 같이 레코드가 존재하는 경우다.

--------------------------------------
|requester_id|accepter_id|accept_date|
|       1    |      2    |2016/06/03 |
|       1    |      3	 |2016/06/08 |
--------------------------------------

JOIN 구의 조건이 되는 구를 충족하지 않을 경우 레코드 자체가 생성이 되지 않기 때문에 발생한 문제로
INNER JOIN 구가 아닌 LEFT JOIN 구를 사용하면 정상적으로 문제가 해결된다.
*/

SELECT
    Requesters.requester_id AS id,
    COUNT(DISTINCT Requesters.accepter_id) + COUNT(DISTINCT Accepters.requester_id) AS num
FROM RequestAccepted AS Requesters
JOIN RequestAccepted AS Accepters
ON Requesters.requester_id = Accepters.accepter_id
GROUP BY Requesters.requester_id
ORDER BY num DESC
LIMIT 1;


-- 아래와 같이 UNION ALL 키워드를 활용하여 문제를 해결할 수도 있다.

SELECT
    id,
    COUNT(id) AS num
FROM (
    SELECT requester_id AS id
    FROM RequestAccepted
    UNION ALL
    SELECT accepter_id AS id
    FROM RequestAccepted
) AS Total
GROUP BY id
ORDER BY num DESC
LIMIT 1;
