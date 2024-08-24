CREATE DATABASE VDOrderDB;

USE VDOrderDB;


CREATE TABLE Orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_total DECIMAL(10, 2) NOT NULL,
    total_items INT NOT NULL,
    tip_amount DECIMAL(10, 2) DEFAULT 0.00,
    roundedDollar DECIMAL(10, 2) DEFAULT 0.00 NOT NULL
);


CREATE TABLE OrderItems (
    order_item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT NOT NULL,
    item_id INT NOT NULL,
    quantity INT NOT NULL CHECK (quantity > 0),
    FOREIGN KEY (order_id) REFERENCES Orders(order_id),
    FOREIGN KEY (item_id) REFERENCES Items(item_id)
);


CREATE TABLE Items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE,
    price DECIMAL(10, 2) NOT NULL,
    category_id INT NOT NULL,
    FOREIGN KEY (category_id) REFERENCES Categories(cat_id)
);

CREATE TABLE Categories (
    cat_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL UNIQUE
);


SHOW TABLES;  -- To list all tables
DESCRIBE Orders;  -- To describe the Orders table (do this for each table)

CREATE INDEX idx_order_date ON Orders(order_date);
CREATE INDEX idx_item_name ON Items(name);

