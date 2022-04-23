-- [ LeetCode ] 2230. The Users That Are Eligible for Discount

/*
CREATE FUNCTION 구와 같은 형태로 함수를 선언할 경우 반환값을 하나 밖에 설정해줄 수 없다.
만약 복수의 값을 반환하기를 원한다면 CREATE PROCEDURE 구를 통해 프로시저(Procedure)를 선언하고 사용해야 한다.

함수와 정의하는 방법이 유사한데 프로시저명, 그리고 받게 되는 매개변수를 선언하고 반환되는 값에 대해서는 별도로 선언해주지 않아도 된다.
함수와 마찬가지로 BEGIN 키워드로 프로시저에 대한 정의를 시작하고 END 키워드로 프로시저 정의를 종료한다.
이때 유의할 점은 선언되는 쿼리의 마지막에 잊지 말고 세미콜론(`;`)을 붙여줘야 한다는 것이다.

추가적으로 프로시저를 사용하면 쿼리에 대해 일괄적인 작업을 하는데 유용하며,
프로시저를 수정하기 전까지는 내부의 쿼리를 볼 수 없어 쿼리문이 보호되기 때문에 인젝션(Injection)으로 부터 안전하다.
그러나 그만큼 디버깅이나 유지보수 측면에서 어려움이 존재한다.
*/

CREATE PROCEDURE getUserIDs(startDate DATE, endDate DATE, minAmount INT)
BEGIN
    SELECT DISTINCT user_id AS user_id
    FROM Purchases
    WHERE (
        DATE(time_stamp) BETWEEN startDate AND DATE_SUB(endDate, INTERVAL 1 DAY)
        AND
        amount >= minAmount
    )
    ORDER BY user_id;
END