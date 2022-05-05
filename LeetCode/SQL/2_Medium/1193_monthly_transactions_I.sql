-- [ LeetCode ] 1193. Monthly Transactions I

/*
MySQL의 경우 표준 SQL과 다르게 GROUP BY 구를 다룬다.

1. 표준 SQL의 경우 칼럼에 대해서만 GROUP BY 구에 작성할 수 있는데 MySQL에서는 칼럼 뿐만 아니라 함수 식과 같은 칼럼이 아닌(Noncolumn) 것도 작성할 수 있다.
2. 표준 SQL의 경우 별칭(Alias)은 GROUP BY 구에 작성할 수 없는데 MySQL에서는 SELECT 구에서 사용된 별칭 또한 작성할 수 있따.

위 두 가지 방법에 따라 아래 풀이 또한 MySQL 기준에서의 풀이이기 때문에
`GROUP BY DATE_FORMAT(trans_date, '%Y-%m'), country`와 같은 표현식이나
SELECT 구에 DATE_FORMAT 함수 부분이 `month`라는 필드로 별칭처리 되었다면 `GROUP BY month, country`와 같은 표현식 모두 가능하다.

가독성을 위해 별칭을 사용하는 게 더 깔끔할 것으로 판단되어 해당 풀이에서는 두 번째 방법을 사용하였다.
*/

SELECT
    DATE_FORMAT(trans_date, "%Y-%m") AS month,
    country,
    COUNT(state) AS trans_count,
    SUM(state='approved') AS approved_count,
    SUM(amount) AS trans_total_amount,
    SUM(IF(state='approved', amount, 0)) AS approved_total_amount
FROM Transactions
GROUP BY month, country;
