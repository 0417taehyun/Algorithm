-- [ 프로그래머스 ] 나이 정보가 없는 회원 수 구하기

SELECT COUNT(USER_ID) AS USERS
FROM USER_INFO
WHERE AGE IS NULL


SELECT SUM(AGE IS NULL) AS USERS
FROM USER_INFO
