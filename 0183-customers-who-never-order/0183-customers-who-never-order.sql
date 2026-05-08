# Write your MySQL query statement below
SELECT name AS cUSTOMERS
FROM Customers
LEFT JOIN Orders ON Customers.id=Orders.customerId
WHERE Orders.customerID IS NULL;