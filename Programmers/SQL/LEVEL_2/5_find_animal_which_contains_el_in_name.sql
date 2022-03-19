-- [ 프로그래머스 ] 이름에 el이 들어가는 동물 찾기

/*
메타문자인 `%`의 경우 빈 문자열과도 매치가 되기 때문에 "Elly"와 같이 "EL" 단어 앞에 아무런 단어가 존재하지 않아도, 다시 말해 빈 문자열이라도 조건에 일치한다.
만약 임의의 문자 하나를 의미하고 싶으면 문자열을 의미하는 메타문자인 `%` 대신 `_`를 사용해야 한다.

추가적으로 LIKE 문법은 대소문자를 구별하지 않기 때문에 대소문자를 구별하기 위해서는,
BINARY(NAME) LIKE "%EL%"과 같이 조건에 해당하는 필드를 BINARY 문법을 사용하여 감싸주면 된다.
*/

SELECT ANIMAL_ID, NAME
FROM ANIMAL_INS
WHERE (
    ANIMAL_TYPE = "Dog"
    AND
    NAME LIKE "%EL%"
)
ORDER BY NAME;