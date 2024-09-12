-- Create the database (if needed, done in scripts outside this schema)
-- CREATE DATABASE VDOrderDB;
-- USE VDOrderDB;

-- 1. Create the Categories table first since Items will reference it
CREATE TABLE Categories (
    cat_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);

-- 2. Create the Items table next, referencing Categories
CREATE TABLE Items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL CHECK (price >= 0),  -- Ensure price is non-negative
    category_id INT DEFAULT NULL,  -- Category can be NULL if not all items require a category
    FOREIGN KEY (category_id) REFERENCES Categories(cat_id) 
        ON DELETE SET NULL  -- Set category_id to NULL if the category is deleted
);

-- 3. Create the Orders table
CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_total DECIMAL(10, 2) NOT NULL CHECK (order_total >= 0),  -- Ensure total is non-negative
    total_items INT NOT NULL CHECK (total_items > 0),  -- Ensure total items are positive
    tip_amount DECIMAL(10, 2) DEFAULT 0.00 CHECK (tip_amount >= 0),  -- Ensure tip is non-negative
    roundedDollar DECIMAL(10, 2) DEFAULT 0.00 NOT NULL CHECK (roundedDollar >= 0)  -- Non-negative rounding value
);

-- 4. Create the OrderItems table, which references both Orders and Items
CREATE TABLE OrderItems (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),  -- Ensure quantity is positive
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
        ON DELETE CASCADE,  -- Cascade delete to remove all order items if the order is deleted
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
        ON DELETE CASCADE  -- Cascade delete to remove all associated items if an item is deleted
);

-- Create indexes to optimize performance
CREATE INDEX idx_order_date ON Orders(order_date);  -- Index on order date for fast retrieval
CREATE INDEX idx_item_name ON Items(name);  -- Index on item name for faster lookups

-- Queries to verify the schema
-- SHOW TABLES;  -- To list all tables
-- DESCRIBE Orders;  -- To describe the Orders table (do this for each table)
