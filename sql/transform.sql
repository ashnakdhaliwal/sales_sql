-- data warehouse schema 

-- fact table (core transactional data)
CREATE TABLE fact_sales AS 
SELECT --orderitemid, orderid, productid, customerid, orderdate, price
-- quantity, itemtotal (quantity * price)
FROM order_items oi, orders o, products p 

-- Dim customers (lookup table for customer metadata)

-- Dim products (product catalog and pricing)

-- Dim date (time-based lookup table for reporting)