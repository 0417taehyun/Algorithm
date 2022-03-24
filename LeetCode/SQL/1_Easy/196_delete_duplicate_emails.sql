-- [ LeetCode ] 196. Delete Duplicate Emails

/*
DELETE 문에서도 복수의 테이블을 다룰 수 있다.
이때 DELETE 키워드 다음에 어떤 테이블에 대해 명령을 실행할 것인지 명시해줘야 한다.
따라서 아래와 같이 (INNER) JOIN 구를 사용하여 id 값이 더 큰 경우를 삭제해 중복된 이메일 중 id 값이 가장 작은 필드만 남길 수 있다.
*/

DELETE Person
FROM Person
JOIN Person AS Joined_Table
USING (email)
WHERE Person.id > Joined_table.id