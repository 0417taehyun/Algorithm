-- [ LeetCode ] 1132. Reported Posts II

/*
처음에 단순히 AVG 함수를 사용하여 문제를 해결하려 했는데 제출했을 때 오류가 났다.
게시글 별로 따지는 것이기 때문에 여러 사용자가 하나의 게시글에 대해 당일날 똑같이 action 필드 값이 `report`, extra 필드의 값이 `spam`인 경우라면 동일하게 처리를 해야 한다.
다시 말해 똑같은 action_date 필드의 값을 가진 post_id 필드의 값에 대해서는 중복 처리를 해줘야 한다는 의미였다.

Removals 테이블을 마찬가지로 LEFT JOIN 구를 활용해 결합할 때도 결국 SELECT 구에서 DISTINCT 키워드를 활용해 중복을 제거해주기 때문에
똑같이 COUNT 함수 내부에 DISTINCT 키워드를 사용해서 중복을 제거해줘야 한다.
그렇지 않으면 SELECT 구는 -ORDER BY 구, LIMIT 구 등 일부 구문을 제외하고는- 가장 늦게 실행되기 때문에 필드의 값이 중복되어 계산된다.

LEFT JOIN 구에 조건으로 Removals 테이블의; remove_date 필드 값이 action_date 필드의 값보다 크거나 같은 경우를 따진 이유는
문제 속 "after being reported as spam"이라는 표현 때문이었다.
action 필드의 값이 `spam`이기 이전에 다른 값으로 신고가 들어가고 결과 처리가 되었을 수도 있기 때문이다.

Removals 테이블은 post_id 필드를 외래 키(Foregin Key)로 갖는 일종의 Actions 테이블의 자식 테이블이다.
이때 따로 삭제 작업을 통해 물리적으로 레코드를 지우는 게 아니라 이 Removals 테이블을 활용하여 삭제 날짜를 입력하는 식으로 논리적으로 데이터를 삭제하는 경우이기 때문에
로직 상의 오류가 발생하여 게시글이 삭제가 되었는데 뷰에 남아 있어 사용자가 한번 더 action 필드의 값이 `spam`인 경우로 요청을 보내 테이블에 레코드가 생성될 수 있다.

실제 인터뷰를 진행하면서 문제를 풀 때는 이러한 부분을 고려해서 질문을 하면 좋을 것 같다.
*/


SELECT ROUND(AVG(average_percent) * 100, 2) AS average_daily_percent
FROM (
    SELECT COUNT(DISTINCT Removals.post_id) / COUNT(DISTINCT SpamActions.post_id) AS average_percent
    FROM (
        SELECT
            post_id,
            action_date
        FROM Actions
        WHERE (
            action = 'report'
            AND
            extra = 'spam'
        )
    ) AS SpamActions
    LEFT JOIN Removals
    ON (
        SpamActions.post_id = Removals.post_id
        AND
        SpamActions.action_date <= Removals.remove_date
    )
    GROUP BY action_date
) AS Reports;
