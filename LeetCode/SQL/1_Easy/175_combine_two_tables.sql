-- [ LeetCode ] 175. Combine Two Tables

SELECT
    firstName,
    lastName,
    city,
    state
FROM Person
LEFT JOIN Address
USING (personId);
