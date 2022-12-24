-- [ LeetCode ] 1939. Users That Actively Request Confirmation Messages

/*
Confirmations 테이블 내에 user_id 및 timestamp 필드가 기본 키(Primary Key)이기 때문에
동일한 사용자에 대해 정확히 동일한 시간(Date)으로 레코드가 저장되는 경우는 존재하지 않는다.

이때 문제에서 'twice'라고 작성된 부분이 24시간 이내에 요청을 받은 횟수가 두 번이라는 의미지
테이블 내 한 명의 사용자마다 무조건적으로 두 개의 레코드씩 저장되어 있다는 보장을 의미하지는 않는 것 같아서
INNER JOIN 구를 사용하여 그 조건으로 user_id 필드의 값이 같은 대신 time_stamp 필드의 값이 합쳐지는 테이블 쪽이 더 큰 경우로 작성하였다.

결론적으로 이를 통해 Confirmations 테이블 내에 레코드가 하나 밖에 존재하지 않는 사용자나
두 개 이상 존재하는데 그 나열된 레코드 중에서 한번이라도 24시간 내에 두번의 요청이 발생했던 사용자를 추출할 수 있게 된다.

추가적으로 DATE_ADD 함수가 아닌 TIMESTAMPDIFF 함수를 사용하여 24시간을 초로 만들어서 `24*60*60` 값과 비교하는 방법도 있다.
*/

SELECT
    DISTINCT Confirmations.user_id AS user_id
FROM Confirmations
JOIN Confirmations AS Last_Timestamp
ON (
    Confirmations.user_id = Last_Timestamp.user_id
    AND
    Confirmations.time_stamp < Last_Timestamp.time_stamp
)
WHERE DATE_ADD(Confirmations.time_stamp, INTERVAL 24 HOUR) >= Last_Timestamp.time_stamp;


/*
아래와 같이 Window Function 종류 중 하나인 LAG 함수 및 TIMESTAMPDIFF 함수를 사용하여 문제를 해결할 수 있다.
LAG 함수는 현재 행(Row)의 이전 행을 가져오는 함수다.
TIMESTASMP 함수의 경우 첫 번째 인자로 단위를, 두 번째 인자로 시작 값을, 마지막 인자로 마무리 값을 받는다.
따라서 아래 식을 해석해보면 초 단위(`second`) 계산을 행하는데 `time_stamp` 필드에서 LAG 함수를 통해 얻게 된 바로 직전의 `time_stamp` 필드를 빼는 것이다.

이때 `NULL` 값은 무시되며 time_stamp 필드를 기준으로 오름차순 정렬된 값을 빼기 때문에 음수로 그 차이를 얻게 되어서 ABS 함수를 통해 절댓값화시켰다.
더욱이 초로 계산하기 때문에 24시간을 초 단위로 바꾼 `24*60*60`을 기준으로 조건을 걸어주었다.
만약 TEIMSTAMPDIFF 함수의 단위를 `hour`로 설정하거나 DATEDIFF 함수를 사용할 경우 1일하고 1초가 많은 값도 1일로 여겨지기 때문에 원하는 결괏값이 나오지 않음에 주의해야 한다.
*/

SELECT
   DISTINCT user_id AS user_id
FROM (
    SELECT
        user_id,
        TIMESTAMPDIFF(second, time_stamp, LAG(time_stamp) OVER(PARTITION BY user_id ORDER BY time_stamp)) AS diff
    FROM Confirmations
) AS Timestamp_Diff
WHERE ABS(diff) <= 24 * 60 * 60;
