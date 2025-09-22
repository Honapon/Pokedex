
CREATE USER 'pokedata'@'%' IDENTIFIED BY 'pokekopi';
GRANT SELECT, INSERT, UPDATE ON pokemon TO 'pokedata'@'%' identified by 'pokekopi'; 
FLUSH PRIVILEGES;

CREATE DATABASE pokedex;

CREATE TABLE IF NOT EXISTS pokedex.pokemon(
id INT PRIMARY KEY,
pmon VARCHAR(100) NOT NULL,
height INT,
weight INT,
imageurl VARCHAR(255) NOT NULL
);


