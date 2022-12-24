-- [ LeetCode ] 597. Friend Requests I: Overall Acceptance Rate

/*
계속 Submission이 Wrong이 떠서 무엇이 문제인지 이해가 되지 않아 정답을 보았다. 문제 속 아래와 같은 부분이 고려해야 할 중요 사항이었다.

The accepted requests are not necessarily from the table friend_request.
In this case, you just need to simply count the total accepted requests (no matter whether they are in the original requests),
and divide it by the number of requests to get the acceptance rate. 

반드시 Accepted된 요청이 FriendRequest 테이블에서만 오지는 않는다는 것이다.
이 경우에는 RequestAccepted 테이블에 Accepted된 수를 계산하여 FriendRequest의 수로부터 나누기만 하면 된다는 조건이었다.

우선 문제는 아래와 같이 해결할 수 있다. DISTINCT 키워드를 통해 중복된 경우를 제거한다.
GROUP BY는 내부적으로 정렬을 사용하기 때문에 단순히 정렬된 데이터와 무관하게 중복되는 경우만을 제거하기 위해서는 DISTINCT 키워드가 훨씬 효율적이다.

이때 유의할 점은 `SELECT sender_id DISTINCT send_to_id FROM FriendRequest`와 같이 DISTINCT 키워드 이전에 필드를 조회할 수 없다. 중복된 값을 제거할 수 없기 때문이다.
또한 DISTINCT 키워드 뒤에 `DISTINCT sender_id, send_to_id`와 같이 복수의 필드를 지정할 수 있다.

추가적으로 ROUND 함수의 경우 올림을 의미한다.

인터뷰를 볼 때 총 요청의 수를 FriendRequest 테이블로만 확인하는 것으로 문제에서 가정하는 것인지,
아니면 RequestAccept 테이블 내에서 FriendRequest 테이블 요청이 Accepted 된 경우만을 놓고 봐야하는 것인지를 물으면 좋을 것 같다.
*/

SELECT ROUND(
    IFNULL(
        (
            SELECT COUNT(*)
            FROM (
                SELECT DISTINCT requester_id, accepter_id
                FROM RequestAccepted
            ) AS Unique_Accept
        )
        /
        (
            SELECT COUNT(*)
            FROM (
                SELECT DISTINCT sender_id, send_to_id
                FROM FriendRequest
            ) AS Unique_Request
        )
    , 0)
, 2) AS accept_rate;