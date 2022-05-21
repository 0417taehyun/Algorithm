-- [ LeetCode ] 1747. Leetflex Banned Accounts

SELECT DISTINCT LogInfo.account_id
FROM LogInfo
JOIN LogInfo AS Checker
ON (
    LogInfo.account_id = Checker.account_id
    AND
    LogInfo.ip_address <> Checker.ip_address
    AND
    Checker.login BETWEEN LogInfo.login AND LogInfo.logout
);
