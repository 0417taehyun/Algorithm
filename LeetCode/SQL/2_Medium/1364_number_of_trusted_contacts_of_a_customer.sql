-- [ LeetCode ] 1364. Number of Trusted Contacts of a Customer

/*
아래와 같이 서브쿼리를 활용하여 계층적으로 문제를 풀었는데 상당히 효율성이 떨어진다.
아래 쿼리에서 한 가지 유의해야 할 사항은 만약 값이 `NULL`인 경우에 대한 SUM 함수를 실행하면 `0`이 아닌 결국 `NULL`이 반환되기 때문에 IFNULL 함수 등을 사용해서 변환을 하거나
COUNT 함수를 활용하면 NULL 값은 셈을 하지 않기 때문에 정상적으로 `0`을 반환 받을 수 있다는 것이다.
*/

SELECT
    invoice_id,
    customer_name,
    price,
    contacts_cnt,
    trusted_contacts_cnt
FROM Invoices
JOIN (
    SELECT
        Customers.customer_id AS user_id,
        Customers.customer_name AS customer_name,
        COUNT(TrustedCustomers.trusted_state) AS contacts_cnt,
        COUNT(IF(TrustedCustomers.trusted_state = TRUE, TRUE, NULL)) AS trusted_contacts_cnt
    FROM Customers
    LEFT JOIN (
        SELECT
            Contacts.user_id AS customer_id,
            IF(Customers.customer_id IS NULL, FALSE, TRUE) AS trusted_state
        FROM Contacts
        LEFT JOIN Customers
        ON (
            Contacts.contact_name = Customers.customer_name
            AND
            Contacts.contact_email = Customers.email
        )
    ) AS TrustedCustomers
    USING (customer_id)
    GROUP BY Customers.customer_id
) AS CountedCustomers
USING (user_id)
ORDER BY invoice_id ASC;


/*
아래와 같이 Invoices 테이블을 기준으로 계층적으로 하지 않더라도 세 번의 JOIN 구를 실행해 문제를 해결할 수 있다.
JOIN 구를 실행할 때 굳이 계층적으로 하지 않더라도 문제를 해결할 수 있다는 점을 잊지 말아야겠다.
속도는 사실 그렇게 차이가 나지 않는데 우선 가독성이 좋다는 부분에 있어 훨씬 좋은 정답이라 생각한다.
속도에 대한 측면은 WITH 구를 활용하여 CTE(Common Table Expression)를 만들어 해결할 수 있을 것 같다.
*/

SELECT
    invoice_id,
    Users.customer_name AS customer_name,
    price,
    COUNT(Contacts.user_id) AS contacts_cnt,
    COUNT(Customers.customer_id) AS trusted_contacts_cnt
FROM Invoices
JOIN Customers AS Users
ON Invoices.user_id = Users.customer_id
LEFT JOIN Contacts
ON Users.customer_id = Contacts.user_id
LEFT JOIN Customers
ON (
    Contacts.contact_name = Customers.customer_name
    AND
    Contacts.contact_email = Customers.email
)
GROUP BY invoice_id
ORDER BY invoice_id ASC;
