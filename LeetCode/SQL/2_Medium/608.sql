-- [ LeetCode ] 608. Tree Node

SELECT
    Tree.id AS id,
    CASE
        WHEN Tree.p_id IS NULL THEN 'Root'
        WHEN (
            Tree.p_id IS NOT NULL
            AND
            Nodes.id IS NOT NULL
        ) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
LEFT JOIN Tree AS Nodes
ON Tree.id = Nodes.p_id
GROUP BY Tree.id
ORDER BY id ASC;


/*
이미 첫 번째 WHEN 부분에서 p_id 필드의 값이 `NULL`인지 여부를 판단하기 때문에
그 다음 WHEN 부분에 따로 `IS NOT NULL`과 같은 표현식을 작성할 필요가 없다.
*/

SELECT
    Tree.id AS id,
    CASE
        WHEN Tree.p_id IS NULL THEN 'Root'
        WHEN Nodes.id IS NOT NULL THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
LEFT JOIN Tree AS Nodes
ON Tree.id = Nodes.p_id
GROUP BY Tree.id
ORDER BY id ASC;


/*
더 간단하게 아래와 같이 서브쿼리를 활용하여 굳이 LEFT JOIN 구를 사용하지 않아도 문제를 해결할 수 있다.
아래와 같이 문제를 풀면 속도 또한 훨씬 빠르다.

문제를 접근할 때 JOIN 구를 써야하는 이유에 대해서, 서브쿼리로 대신할 수 없는지에 대해서 한번 생각해보면 좋을 것 같다.
*/

SELECT
    id,
    CASE
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT DISTINCT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM Tree
ORDER BY id ASC;