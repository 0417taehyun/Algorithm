-- [ LeetCode ] 1934. Confirmation Rate

SELECT
    Signups.user_id,
    ROUND(IFNULL((SUM(Confirmations.action = 'confirmed') / COUNT(Confirmations.action)), 0), 2) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
USING (user_id)
GROUP BY Signups.user_id;


/*
아래와 같이 AVG 함수 내에 IF 함수를 사용하여 더 간단하게 해결할 수도 있다.
IF 함수 덕분에 NULL 값에 대한 처리를 `0`으로 하기 때문에 위 풀이처럼 따로 IFNULL 함수를 사용하지 않아도 된다.
action 필드의 값이 `confirmed`가 아닌 모든 값이 전부 `0`이 되기 때문에 `timeout` 뿐만 아니라 NULL 또한 `0`으로 변환된다.

조건에 따른 평균을 구하는 문제에 있어 보통 SUM 함수 내부에 IF 함수 또는 CASE 구를 사용해서 분자를 구하고,
COUNT 함수를 사용해서 분모를 구해 값을 구할 때가 많았는데
AVG 함수를 조금 더 적극적으로 사용해야겠다.
*/

SELECT
    Signups.user_id,
    ROUND(AVG(IF(action='confirmed', 1, 0)), 2) AS confirmation_rate
FROM Signups
LEFT JOIN Confirmations
USING (user_id)
GROUP BY Signups.user_id;
