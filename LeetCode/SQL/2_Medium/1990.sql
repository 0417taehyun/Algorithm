-- [ LeetCode ] 1990. Count the Number of Experiments

SELECT
    PlatformsWithExperiments.platform,
    PlatformsWithExperiments.experiment_name,
    COUNT(Experiments.experiment_id) AS num_experiments
FROM (
    SELECT
        platform,
        experiment_name
    FROM (
        SELECT 'Android' AS platform
        UNION ALL
        SELECT 'IOS'
        UNION ALL
        SELECT 'Web'
    ) AS Platforms
    JOIN (
        SELECT 'Reading' AS experiment_name
        UNION ALL
        SELECT 'Sports'
        UNION ALL
        SELECT 'Programming'
    ) AS ExperimentTypes
) AS PlatformsWithExperiments
LEFT JOIN Experiments
USING (platform, experiment_name)
GROUP BY PlatformsWithExperiments.platform, PlatformsWithExperiments.experiment_name;
