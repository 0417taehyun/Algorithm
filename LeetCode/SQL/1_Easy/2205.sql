-- [ LeetCode ] 2205. The Number of Users That Are Eligible for Discount

/*
함수 내부에 SQL 쿼리를 작성하는 게 문제였다.
함수 자체를 사용해 본 적이 없어서 관련하여 내용을 정리하기 이전에 쿼리 관련된 부분을 먼저 이야기하고자 한다.


우선 time_stamp 필드의 값이 `2020-01-01 14:23:59`과 같이 초단위까지 저장이 되는 형태였다.
이때 해당 값이 제시되는 startDate 및 endDate 사이여야 했는데 startDate 및 endDate 값은 `2020-01-01` 같이 일(Day)까지만 제시되었다.
여기서 `2020-01-01 14:23:59` 값은 endDate 값이 `2020-01-01`일 때 포함되어야 할까 제외되어야 할까?
결론적으로는 포함이 안 되었어야 했는데 실제 인터뷰 형식의 문제였다면 아마 질문을 하는 게 좋았을 것 같다.
추가적인 문제는 BETWEEN 부분을 사용할 때였다. 포함이 안 된다고 생각하고 BETWEEN 부분에 endDate 값을 그대로 사용하였는데
프로그래밍에서 `range` 함수처럼 BETWEEN 또한 뒷 부분의 값이 자동으로 `-1`이 된다고 생각했기 때문이다.
그런데 알고보니까 뒷 부분도 포함되는 형태여서 DATE_SUB 함수를 사용하여 문제를 해결했다.

다음으로 amount 필드의 값이 최소 minAmount 매개변수의 값이어야 했다.
처음에 user_id 필드의 값 및 timestamp 필드의 값 중 DATE 부분이 동일한 경우 해당 부분을 SUM 함수를 사용하여 더해서 minAmount 값보다 큰지 비교하는 줄 알았다.
하지만 그냥 개별적으로 비교하는 문제였다. 이 부분도 만약 인터뷰 형식이었다면 물어봤다면 좋았을 것 같다.


SQL에서 함수를 사용하는 방법은 무척 다채롭지만 매우 단순한 형태로는 CREATE FUNCTION 구와 함께 함수의 이름 및 매개변수를 나열하고 어떤 것을 반환하는지 작성해주면 된다.
아래 함수의 경우 이름은 `getUserIDs`이며 매개변수로 DATE 자료형의 `startDate` 및 `endDate`, 그리고 INT 자료형의 `minAmount`를 받고 INT 자료형을 반환한다.
따라서 만약 2개 이상의 값 혹은 컬럼을 반환할 경우 오류가 발생한다. 만약 복수의 열을 반환하고 싶다면 `FUNCTION`이 아닌 `PROCEDURE`를 사용하면 된다.

추가적으로 BEGIN 키워드를 기점으로 함수에 대한 정의를 시작하며 END 키워드를 기점으로 함수 정의를 마무리한다.
이때 RETURN 구에 반환할 값, 다시 말해 함수의 표현으로 정의할 쿼리를 작성했는데 하나의 값만 필요했기 때문에 서브쿼리 형태로 해당 쿼리를 작성했다.
또 유의할 점은 RETURN 키워드의 마지막 부분에 세미콜론(`;`)을 붙여줘야 한다는 점이다.

만들어진 함수를 사용하는 방법은 `SELECT getUserIDs("2020-01-01", "2020-02-01", 1000)`과 같이 표현하면 된다.

추가적으로 MySQL에서 변수를 선언하는 방법을 먼저 살펴보면 좋을 것 같다.
SET 구를 활용하여 변수를 선언할 수 있는데 `SET @myVar = "test";`와 같은 표현식을 통해 `myVar`라는 변수에 `"test"`라는 값을 할당할 수 있다.
이때 해당 변수를 사용할 때 동일하게 `@`를 변수명 앞에 붙여서 `SELECT @myVar;`와 같은 표현식을 통해 해당 변수를 사용할 수 있다.
*/

CREATE FUNCTION getUserIDs(startDate DATE, endDate DATE, minAmount INT) RETURNS INT
BEGIN
  RETURN (
      SELECT COUNT(DISTINCT user_id)
      FROM Purchases
      WHERE (
          DATE(time_stamp) BETWEEN startDate AND DATE_SUB(endDATE, INTERVAL 1 DAY)
          AND
          amount >= minAmount
      )
  );
END