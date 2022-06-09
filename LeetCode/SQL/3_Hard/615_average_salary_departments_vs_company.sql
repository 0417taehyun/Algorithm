-- [ LeetCode ] 615. Average Salary: Departments VS Company

SELECT
    DepartmentAverages.pay_month,
    DepartmentAverages.department_id,
    CASE
        WHEN DepartmentAverages.department_average > CompanyAverages.company_average THEN 'higher'
        WHEN DepartmentAverages.department_average < CompanyAverages.company_average THEN 'lower'
        ELSE 'same'
    END AS comparison
FROM (
    SELECT
        DATE_FORMAT(Salary.pay_date, '%Y-%m') AS pay_month,
        Employee.department_id,
        AVG(amount) AS department_average
    FROM Salary
    JOIN Employee
    USING (employee_id)
    GROUP BY pay_month, Employee.department_id
) AS DepartmentAverages
JOIN (
    SELECT
        DATE_FORMAT(Salary.pay_date, '%Y-%m') AS pay_month,
        AVG(amount) AS company_average
    FROM Salary
    GROUP BY pay_month
) AS CompanyAverages
USING (pay_month);
