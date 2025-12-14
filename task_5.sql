-- Task 5: Insert a single customer
-- File: task_5.sql
SELECT * FROM customers;
INSERT INTO customers (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');
