-- [ LeetCode ] 1501. Countries You Can Safely Invest In

/*
아래와 같이 SUBSTRING 함수 및 HAVING 구에서의 서브쿼리를 활용하여 문제를 해결했다.
한 가지 유의해야 할 사항은 MySQL에서 인덱스의 시작은 `1`이며 끝을 가리킬 때 바로 그 직전까지를 의미하는 것이 아닌 정말로 그 끝을 포함하여 의미한다는 것이다.
그래서 `SUBSTRING(Persone.phone_number, 1, 3)`이라는 표현이 결국 문자열의 첫 번째 문자부터 세 번째 문자까지 총 길이가 3인 문자열을 추출하는 걸 의미한다.

추가적으로 HAVING 구의 조건에 대해 서브쿼리에서 AVG 함수를 매번 실행해야 하기 때문에 성능면에서 많이 떨어지지 않을까 싶었다. 크게 신경쓰지 않아도 될 부분일 것 같다.
관련해서는 추후에 SQL 성능 관련 책을 훑어보면서 공부해야겠다.
*/

SELECT Country.name AS country
FROM Calls
JOIN Person
ON (
    Calls.caller_id = Person.id
    OR
    Calls.callee_id = Person.id
)
JOIN Country
ON SUBSTRING(Person.phone_number, 1, 3) = Country.country_code
GROUP BY Country.name
HAVING AVG(duration) > (SELECT AVG(duration) FROM Calls);
