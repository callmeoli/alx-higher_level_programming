-- create database and insert table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities( id INT UNIQUE NOT NULL PRIMARY KEY AUTO_INCREMENT, 
	FOREIGN KEY (state_id) REFERENCES states(id) NOT NULL,
       	name VARCHAR(256) NOT NULL );
