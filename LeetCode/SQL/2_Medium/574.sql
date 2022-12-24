-- [ LeetCode ] 574. Winning Candidate

SELECT name
FROM Candidate
JOIN (
    SELECT candidateId
    FROM Vote
    GROUP BY candidateId
    ORDER BY COUNT(id) DESC
    LIMIT 1
) AS Winner
ON Candidate.id = Winner.candidateId;
