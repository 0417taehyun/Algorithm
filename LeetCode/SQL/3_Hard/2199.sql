-- [ LeetCode ] 2199. Finding the Topic of Each Post

/*
GROUP_CONCAT 함수의 사용법은 다음과 같다.

GROUP_CONCAT(
    DISTINCT expression
    ORDER BY expression
    SEPARATOR sep
);

어떤 표현을 결합하여 한 컬럼 내에 표현할 것인지 선택하고 다음으로 해당 컬럼의 순서를 결정한 다음 이를 구분하는 방법을 결정한다.
SEPARATOR 키워드의 경우 만약 따로 제시하지 않을 경우 기본 값은 콤마( `,` )다.
*/

SELECT
    Posts.post_id,
    IFNULL(GROUP_CONCAT(DISTINCT Keywords.topic_id ORDER BY Keywords.topic_id), 'Ambiguous!') AS topic
FROM Posts
LEFT JOIN Keywords
ON (
    Posts.content LIKE Keywords.word
    OR
    Posts.content LIKE CONCAT('% ', Keywords.word)
    OR
    Posts.content LIKE CONCAT('% ', Keywords.word, ' %')
    OR
    Posts.content LIKE CONCAT(Keywords.word, ' %')
)
GROUP BY Posts.post_id;
