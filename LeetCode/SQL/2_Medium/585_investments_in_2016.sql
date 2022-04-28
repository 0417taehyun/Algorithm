-- [ LeetCode ] 585. Investments in 2016

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE (
    pid NOT IN (
        SELECT DISTINCT Insurance.pid
        FROM Insurance
        JOIN Insurance AS SameCities
        ON (
            Insurance.pid <> SameCities.pid
            AND
            Insurance.lat = SameCities.lat
            AND
            Insurance.lon = SameCities.lon
            )
    )
    AND
    tiv_2015 NOT IN (
        SELECT tiv_2015
        FROM Insurance
        GROUP BY tiv_2015
        HAVING COUNT(pid) = 1
    )
);


/*
아래와 같이 윈도우 함수(Widnow Function)를 사용하면 조금 더 쉽게 문제가 풀린다.
이때 유의할 점은 윈도우 함수 내에 ORDER BY 구를 사용했을 때다.

만약 아래와 같은 테이블이 존재한다고 가정해보자.

+-----+----------+----------+-----+-----+
| pid | tiv_2015 | tiv_2016 | lat | lon |
+-----+----------+----------+-----+-----+
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
+-----+----------+----------+-----+-----+


이때 아래 쿼리를 실행하면 그 결괏값은 아래 테이블과 같이 반환된다.

SELECT
    pid,
    COUNT(pid) OVER(PARTITION BY tiv_2015 ORDER BY pid) AS tiv_2015_cnt,
    COUNT(pid) OVER(PARTITION BY lat, lon ORDER BY pid) AS same_cities_cnt
FROM Insurance

+-----+--------------+-----------------+
| pid | tiv_2015_cnt | same_cities_cnt |
+-----+--------------+-----------------+
| 1   | 1            | 1               |
| 2   | 1            | 1               |
| 3   | 2            | 2               |
| 4   | 3            | 1               |
+-----+--------------+-----------------+


반대로 아래와 같이 ORDER BY 구 부분을 빼고 구현하면 아래와 같이 정상적으로 원하는 결괏값을 얻을 수 있다.

SELECT
    pid,
    COUNT(pid) OVER(PARTITION BY tiv_2015) AS tiv_2015_cnt,
    COUNT(pid) OVER(PARTITION BY lat, lon) AS same_cities_cnt
FROM Insurance

+-----+--------------+-----------------+
| pid | tiv_2015_cnt | same_cities_cnt |
+-----+--------------+-----------------+
| 1   | 3            | 1               |
| 2   | 3            | 2               |
| 3   | 1            | 2               |
| 4   | 3            | 1               |
+-----+--------------+-----------------+


윈도우 함수 내에 사용하는 ORDER BY 구의 경우 PARTITION BY 구를 통해 그룹화된 내부의 정렬을 행한다.
따라서 만약 전체적인 정렬을 원한다면 윈도우 함수 내부가 아닌 바깥에 ORDER BY 구를 사용해야 한다.

따라서 윈도우 함수의 결괏값을 반환하는 tiv_2015_cnt 필드의 경우
pid 필드를 기준으로 윈도우 함수를 사용하게 되면 tiv_2015 필드를 기준으로 묶이고 그에 따른 pid 값을 정렬하여 반환하기 때문에 결괏값이 아래와 같다.

+-----+--------------|
| pid | tiv_2015_cnt |
+-----+--------------+
| 1   | 1            |
| 3   | 2            |
| 4   | 3            |
| 2   | 1            |
+-----+--------------+

same_cities_cnt 필드 또한 마찬가지로 개별적으로 보면 아래와 같다.

+-----+--------------|
| pid | tiv_2015_cnt |
+-----+--------------+
| 1   | 1            |
| 2   | 1            |
| 3   | 2            |
| 4   | 1            |
+-----+--------------+

결론적으로 반환되는 게 실제 셈이 된 횟수가 아닌 해당 PARTITION BY 구에 의해 묶인 내부 그룹에서의 정렬된 순서가 반환되는 것이다.
따라서 ORDER BY 구를 사용하지 않아야 정상적으로 원하는 결괏값을 얻을 수 있다.

추가적으로 표준 SQL에서는 PARTITION BY 구에 컬럼 명만 사용할 수 있는데 MySQL의 경우 HOUR 함수와 같이 해당 컬럼을 조작하는 구를 사용할 수도 있다.
*/

SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM (
    SELECT
        pid,
        COUNT(pid) OVER(PARTITION BY tiv_2015) AS tiv_2015_cnt,
        COUNT(pid) OVER(PARTITION BY lat, lon) AS same_cities_cnt
    FROM Insurance
) AS InsuranceCnt
WHERE (
    tiv_2015_cnt > 1
    AND
    same_cities_cnt = 1
);
