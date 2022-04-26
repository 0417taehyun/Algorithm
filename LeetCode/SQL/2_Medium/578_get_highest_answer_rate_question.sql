-- [ LeetCode ] 578. Get Highest Answer Rate Question

SELECT question_id AS survey_log
FROM SurveyLog
GROUP BY survey_log
ORDER BY (SUM(action='answer') / SUM(action='show')) DESC, survey_log ASC
LIMIT 1;
