-- Create tables for customers products, orders, and items in the order

CREATE TABLE customers (
-- personal id
-- first name 
-- last name 
-- area they are from (?)
-- date they signed up 
);

CREATE TABLE products (
-- product id 
-- name 
-- kind of product
-- price 
);

CREATE TABLE orders (
-- order id
-- customer id (from customers table)
-- date of order
);

CREATE TABLE order_items (
-- item id 
-- order id (from orders table)
-- product id (from products table)
-- quantity 
);