-- [ LeetCode ] 2228. Users With Two Purchases Within Seven Days

SELECT DISTINCT Purchases.user_id
FROM Purchases
JOIN Purchases AS SubPurchases
ON (
    Purchases.purchase_id <> SubPurchases.purchase_id
    AND
    Purchases.user_id = SubPurchases.user_id
    AND
    DATEDIFF(SubPurchases.purchase_date, Purchases.purchase_date) BETWEEN 0 AND 7
)
ORDER BY user_id ASC;
