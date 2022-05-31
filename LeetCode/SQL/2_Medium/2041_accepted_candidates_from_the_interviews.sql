-- [ LeetCode ] 2041. Accepted Candidates From the Interviews

SELECT Candidates.candidate_id
FROM Candidates
JOIN (
    SELECT interview_id
    FROM Rounds
    GROUP BY interview_id
    HAVING SUM(score) > 15
) AS IntervieweeScores
USING (interview_id)
WHERE Candidates.years_of_exp >= 2;
