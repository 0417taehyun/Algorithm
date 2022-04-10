-- [ LeetCode ] 1527. Patients With a Condition

SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE conditions REGEXP '^DIAB1|\\sDIAB1';


-- 아래와 같이 굳이 정규표현식을 사용하지 않더라도 LIKE 조건을 나눠 생각해서 문제를 해결할 수도 있다.

SELECT
    patient_id,
    patient_name,
    conditions
FROM Patients
WHERE (
    conditions LIKE 'DIAB1%'
    OR
    conditions LIKE '% DIAB1%'
)