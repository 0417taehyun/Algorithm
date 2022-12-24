-- [ LeetCode ] 1683. Invalid Tweets

-- LENGTH 함수를 사용하면 문자열의 길이를 얻을 수 있다.

SELECT tweet_id
FROM Tweets
WHERE LENGTH(content) > 15;


/*
그런데 사실 위 정답은 정확하게 따지면 틀린 답이었다.
왜냐하면 LENGTH 함수는 정확하게는 바이트 단위로 계산을 하기 때문이다.
2바이트로 문자가 엔코드되는 유니코드나 더 다양한 바이트의 경우가 존재하는 UTF-8의 경우 조심해야 한다.

예를 들어 아래와 같은 구문은 LENGTH 함수를 사용했기 때문에 바이트 단위로 계산이 되어 `3`을 반환한다.

SELECT LENGTH('€')

반대로 아래와 같은 구문은 CHAR_LENGTH 함수를 사용했기 때문에 문자 단위로 계산이 되어 `1`을 반환한다.

SELECT CHAR_LENGTH('€')

*/

SELECT tweet_id
FROM Tweets
WHERE CHAR_LENGTH(content) > 15;