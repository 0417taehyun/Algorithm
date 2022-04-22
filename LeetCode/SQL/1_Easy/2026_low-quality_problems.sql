-- [ LeetCode ] 2026. Low-Quality Problems

SELECT problem_id
FROM Problems
WHERE ((likes) / (likes + dislikes)) * 100 < 60
ORDER BY problem_id;
