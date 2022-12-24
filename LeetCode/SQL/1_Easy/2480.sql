-- [ LeetCode ] 2480. Form a Chemical Bond

SELECT
    Metals.symbol AS metal, 
    Nonmetals.symbol AS nonmetal
FROM Elements AS Metals, Elements AS Nonmetals
WHERE (
    Metals.type = "Metal"
    AND
    Nonmetals.type = "Nonmetal"
)
