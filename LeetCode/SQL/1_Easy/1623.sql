-- [ LeetCode ] 1623. All Valid Triplets That Can Represent a Country

/*
아래와 같이 CROSS JOIN 구를 사용하여 교차결합, 다시 말해 곱집합(Catesian Products)을 통해 문제를 해결했다.
하지만 데이터가 많을 경우 많은 양의 데이터를 합친 다음에 WHERE 구를 통해 조건을 걸어 그 많은 양의 데이터에 대한 필터링을 해줘야 하기 때문에 비효율적이다.
더욱이 아래와 같이 CROSS JOIN 구를 사용한 이후 양 티이블의 상관관계에 대한 조건을 WHERE 구에 작성하는 방식 자체가 이미 INNER JOIN 구와 거의 유사하게 작동한다.
*/

SELECT
    A.student_name AS member_A,
    B.student_name AS member_B,
    C.student_name AS member_C
FROM SchoolA AS A
CROSS JOIN SchoolB AS B
CROSS JOIN SchoolC AS C
WHERE (
    (
        A.student_name <> B.student_name
        AND
        B.student_name <> C.student_name
        AND
        C.student_name <> A.student_name
    )
    AND
    (
        A.student_id <> B.student_id
        AND
        B.student_id <> C.student_id
        AND
        C.student_id <> A.student_id
    )
);


-- CROSS JOIN 구보다 아래와 같이 INNER JOIN 구를 사용하고 그 조건으로 동일하지 않은 경우를 걸어주는 게 데이터가 더 커졌을 때 훨씬 효율적이다.

SELECT
    A.student_name AS member_A,
    B.student_name AS member_B,
    C.student_name AS member_C
FROM SchoolA AS A
JOIN SchoolB AS B
ON (
    A.student_id <> B.student_id
    AND
    A.student_name <> B.student_name
)
JOIN SchoolC AS C
ON (
    A.student_id <> C.student_id
    AND
    A.student_name <> C.student_name
)
WHERE (
    B.student_id <> C.student_id
    AND
    B.student_name <> C.student_name
);


-- 더 좋은 건 아래와 같이 JOIN 구에 모든 조건을 걸어주는 것이다.

SELECT
    A.student_name AS member_A,
    B.student_name AS member_B,
    C.student_name AS member_C
FROM SchoolA AS A
JOIN SchoolB AS B
ON (
    A.student_id <> B.student_id
    AND
    A.student_name <> B.student_name
)
JOIN SchoolC AS C
ON (
    A.student_id <> C.student_id
    AND
    A.student_name <> C.student_name
    AND
    B.student_id <> C.student_id
    AND
    B.student_name <> C.student_name
);
