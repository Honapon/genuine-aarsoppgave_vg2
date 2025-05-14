CREATE USER 'stiimDb'@'%' IDENTIFIED BY 'steamkopi';
GRANT ALL PRIVILEGES ON *.* TO 'stiimDb'@'%' identified by 'steamkopi'; 
FLUSH PRIVILEGES;


CREATE DATABASE IF NOT EXISTS stiim;

CREATE TABLE IF NOT EXISTS stiim.brukere (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
