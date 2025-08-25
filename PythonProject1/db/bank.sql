CREATE DATABASE bank_db;

USE bank_db;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE,
    password VARCHAR(100),
    balance DECIMAL(10,2) DEFAULT 0.00
);
