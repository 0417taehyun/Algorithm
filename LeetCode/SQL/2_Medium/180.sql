-- [ LeetCode ] 180. Consecutive Numbers

SELECT
    DISTINCT Logs.num AS ConsecutiveNums
FROM Logs
JOIN Logs AS Second_Logs
ON (
    Logs.id = Second_Logs.id + 1
    AND
    Logs.num = Second_Logs.num
)
JOIN Logs AS Third_Logs
ON (
    Second_Logs.id = Third_Logs.id + 1
    AND
    Second_Logs.num = Third_Logs.num
);


/*
위와 같이 문제를 해결해도 정상적으로 통과되긴 했는데 문제는 기본 키(Primary Key)인 id 필드의 값이 중간에 손실되지 않았다는 보장이 없는 점이다.
단순히 "autoincrement column"이라는 표현만 있었을 뿐 예를 들어 `1`과 `3` 사이에 위치해야 할 값이 `2`인 레코드가 삭제되어서 중간이 비었을 수도 있다.
그럼에도 불구하고 id 필드의 값이 `1`과 `3`인 두 레코드의 num 필드 값이 동일하다면 그것은 연속적(Consecutive)이라고 할 수 있기 때문에 이 부분을 고려해주어야 한다.
더욱이 3번 연속되지 않을 수 있기 때문에 확장성을 생각한 쿼리를 설계할 필요도 있다.

아래와 같은 경우 HAVING 구에 숫자를 다르게 지정함으로써 확장성 있는 쿼리가 된다.
윈도우 함수(Window Function) 중 ROW_NUMBER 함수를 사용하여 중간에 레코드가 삭제되더라도 다음 레코드가 id 필드 기준으로 정렬되어 연속되는 것으로 만들 수 있다.
다음으로 id 필드 기준으로 정렬된 레코드를 PARTITION BY 키워드에 num 필드를 활용한 ROW_NUMBER 함수의 결괏값을 기본 행 번호에서 빼면 그룹을 만들 수 있게 된다.

예를 들어 아래와 같은 테이블이 존재한다고 가정해보자.

--------
|id|num|
|1 | 1 |
|4 | 1 |
|5 | 1 |
--------

id 필드의 값이 `4`와 `5`인 레코드의 행 번호는 각각 `2`와 `3`이 된다.
다음으로 id 필드를 기준으로 정렬이 된 이후 num 필드를 기준으로 그룹핑 된 다음 행 번호가 매겨지면 id 필드의 값이 `1`인 경우부터 차례로 그 행 번호의 값이 `1`, `2`, `3`이 된다.
결국 두 행 번호를 빼면 위 세 레코드의 값은 동일하게 `0`이 되고 따라서 중간에 유실된 레코드가 있더라도 연속된 수임을 판별할 수 있게 되는 것이다.

이후 이 뺄셈의 결괏값을 기준으로 GROUP BY 구를 사용한 다음 HAVING 구에서 그 갯수가 문제에서 제시된 `3`보다 큰 경우 3번 이상 연속으로 이어진 레코드들의 집합이기 때문에
이를 DISTINCT 키워드를 활용하여 조회한다.


추가적인 이해를 돕기 위해 만약 아래와 같은 테이블이 있다고 가정해보자.

--------
|id|num|
|1 | 1 |
|2 | 2 |
|4 | 1 |
|5 | 1 |
|7 | 1 |
|8 | 2 |
|9 | 2 |
--------

ROW_NUMBER 함수를 통해 얻게 된 결괏값 row_num 필드,
그리고 ROW_NUMBER 함수 내부에 PARTITON BY 키워드를 활용하여 num 필드를 기준으로 그룹핑해서 얻게 된 결괏값 group_id 필드,
끝으로 이 두 필드의 값을 뺀 row_num - grouped_id 필드를 구해보면 아래와 같다.

------------------------------------------------
|id|num|row_num|grouped_id|row_num - grouped_id|
|1 | 1 |   1   |    1     |         0          |
|2 | 2 |   2   |    1     |         1          |
|4 | 1 |   3   |    1     |         2          |
|5 | 1 |   4   |    2     |         2          |
|7 | 1 |   5   |    3     |         2          |
|9 | 1 |   6   |    4     |         2          |
|10| 2 |   7   |    1     |         6          |
------------------------------------------------

결과적으로 row_num 필드에서 grouped_id 필드를 뺀 값을 기준으로 GROUP BY 구를 실행했을 때
id 필드의 값이 `4`부터 `9`까지의 레코드의 갯수가 `4`개라 HAVING 구의 조건을 만족하기 때문에 결괏값으로 아래와 같은 테이블이 출력될 것이다.

-----------------
|ConsecutiveNums|
|      2        |
-----------------

*/

SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        num,
        (ROW_NUMBER() OVER(ORDER BY id) - ROW_NUMBER() OVER(PARTITION BY num ORDER BY id)) AS Grouped_Id
    FROM Logs
) AS Grouped_Logs
GROUP BY Grouped_Id
HAVING COUNT(num) >= 3;
