-- [ LeetCode ] 1495. Friendly Movies Streamed Last Month

/*
아래와 같이 문제를 해결했었는데 YEAR 함수와 MONTH 함수는 최적화(Optimize)되지 않는다는 피드백을 보았다.
YEAR 함수 및 MONTH 함수의 대상이 되는 program_date 필드가 기본 키(Primary Key)이기 때문에 B-TREE 인덱스(Index)를 사용하여 인덱싱 된다.
그렇다면 우선 인덱스와 B-TREE 인덱스에 대해서 먼저 알아볼 필요가 있다.

DBMS가 데이터베이스 테이블의 모든 데이터를 검색해서 원하는 결과를 조회하는데 너무 많인 자원이 요구되기 때문에
칼럼의 값과 레코드가 저장된 주소를 키-값(Key-Value) 형태로 만들어 인덱스(Index)로 만든다.
그러면 마치 SortedList 형태의 자료구조처럼 칼럼의 값이 주어진 순서에 따라 미리 정렬되어 보관되기 때문에
데이터가 변경될 때마다 값을 정렬해야 하므로 그 과정이 복잡하고 느리지만 이미 정렬된 값을 조회하는 것에 있어서는 좋은 효율을 보여준다.

결론적으로 특정 컬럼을 기준으로 메모리 영역에 목차를 생성해서 SELECT 구의 효율을 높이고,
데이터에 대한 변경이 있을 때마다 다시 재정렬을 해야 하기 때문에 INSERT, UPDATE, DELETE 구의 효율을 희생하는 것이다.
이때 주의할 점은 UPDATE, DELETE 행위 자체가 느린 것이지 UPDATE, DELETE를 위해 데이터를 조회하는 행위 자체는 이미 인덱스 되어 있기 때문에 빠르다.

추가적으로 별다른 인덱스 없이 데이터베이스 내 테이블의 전체 값을 조회하는 것을 풀 테이블 스캔(Full Table Scan)이라 한다.

인덱스는 두 개의 키로 분류될 수 있다.

먼저 기본 키(Primary Key)가 있는데 레코드를 대표하는 컬럼의 값으로 만들어진 인덱스다. NULL 겂과 중복을 허용하지 않는 게 특징이다.
다음으로 대체 키(Secondary Key)가 있는데 

구조에 따라 아래와 같이 세 개의 인덱스로 구분할 수 있다.

먼저 B-TREE 인덱스다. 데이터를 트리 구조로 저장하는 형태로 대부분의 인덱스는 이를 사용 중이다.
예를 들어 별다른 수식 없이 CREATE INDEX 명령문을 실행하면 자동으로 B-TREE 인덱스를 생성한다.
B-TREE 인덱스가 검색 알고리즘으로 매우 뛰어난 성능을 보이지는 않아서 대부분의 데이터베이스는 트리의 리프 노드에만 키값을 저장하는 B+TREE 알고리즘을 사용 중이다.
B+TREE를 사용하는 가장 큰 이유 중 하나는 루트와 리프의 거리를 가능한 일정하게 유지하려 하기 때문이다. 따라서 균형이 잘 잡혀 있어 검색 성능 자체가 안정적이다.
더욱이 트리의 깊이 또한 3-4 정도의 수준으로 일정하고, 데이터가 정렬 상태를 유지하기 때문에 이분 탐색을 통해 검색 비용을 크게 줄일 수 있다.
끝으로 데이터가 정렬되어 있는 만큼 잘 활용하면 집약 함수 등에서 요구되는 정렬을 하지 않은 채 넘어갈 수도 있다.

다음으로 비트맵 인덱스는 데이터를 비트 플래그로 변환해서 저장하는 형태의 인덱스로 카디널리티(Cardinality)가 낮은 필드에 대해 효과가 발휘된다.
하지만 갱신할 때 오버헤드가 너무 크기 때문에 빈번한 갱신이 일어나지 않는 경우에만 사용해야 한다.
이때 카디널리티란 상대적인 중복 수치를 의미하는 것으로 중복도가 낮으면 카디널리티가 높고 반대로 중복도가 낮으면 카디널리티가 낮다.
중요한 것은 카디널리티가 상대적인 개념이라는 것이다.
예를 들어 주민등록번호에 비해 이름은 상대적으로 중복도가 높기 때문에 카디널리티가 낮다고 할 수 있다.
그러나 중복도가 훨씬 높은 다른 컬럼과 이름을 비교한다면 이름은 카디널리티가 그 컬럼에 비해 높다.

해시 인덱스의 경우 키를 해시 분산해서 등가 검색을 고속으로 실행하고 만들어진 인덱스다.
하지만 등가 검색 외에는 효과가 거의 없고 범위 검색을 할 수 없기 때문에 잘 사용되지 않는다.
또한 PostgreSQL, Oracle 내에서의 반대 키 인덱스(Reverse Key Index)와 같이 한정적인 데이터베이스에서만 구현을 지원한다.
이때 등가 검색이란 등가 비교 검색이라고도 하며 값이 같은지 혹은 다른지 비교하여 검색하는 걸 의미한다.

기본적으로 B+TREE 인덱스를 사용하기 때문에 이에 대해 조금 더 자세히 살펴보고자 한다.
우선 쉽게 키(Key)에 

There is one small change that can improve the performance.
Since we have a primary key on these columns (program_date, content_id). the program_date is indexed (which is commonly done using B-TREE indexes).
The date checking part in your query does not utilize the indexes. The query optimizer should extract the month and the year for each date which means that all the rows have to be scanned and the indexes are not utilized.
If we change the date checking part to p.program_date BETWEEN '2020-06-01' AND '2020-06-30', then the query optimizer will be able to quickly filter the rows without scannign all the rows.

*/

SELECT title
FROM Content
JOIN (
    SELECT DISTINCT content_id AS content_id
    FROM TVProgram
    WHERE YEAR(program_date) = 2020 AND MONTH(program_date) = 6
) AS Filtered_TVProgram
USING (content_id)
WHERE Kids_content = "Y" AND content_type = "Movies";
