CREATE DATABASE PENCA_UCU;

USE PENCA_UCU;

CREATE TABLE COUNTRY (
    id_country INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE USER (
    id_student INT PRIMARY KEY AUTO_INCREMENT,
    document VARCHAR(9) NOT NULL,
    username VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    total_points INT NOT NULL,
    id_champion INT,
    id_sub_champion INT

);

ALTER TABLE USER ADD FOREIGN KEY (id_champion) REFERENCES COUNTRY(id_country);
ALTER TABLE USER ADD FOREIGN KEY (id_sub_champion) REFERENCES COUNTRY(id_country);

CREATE TABLE FOOTBALL_MATCH (
    id_match INT PRIMARY KEY AUTO_INCREMENT,
    date_match DATE NOT NULL,
    id_home_country INT NOT NULL,
    id_away_country INT NOT NULL,
    score_home_country INT NOT NULL,
    score_away_country INT NOT NULL,
    id_winner INT
);

ALTER TABLE FOOTBALL_MATCH ADD FOREIGN KEY (id_home_country) REFERENCES COUNTRY(id_country);
ALTER TABLE FOOTBALL_MATCH ADD FOREIGN KEY (id_away_country) REFERENCES COUNTRY(id_country);
ALTER TABLE FOOTBALL_MATCH ADD FOREIGN KEY (id_winner) REFERENCES COUNTRY(id_country);

CREATE TABLE PREDICTION (
    id_user INT NOT NULL,
    id_match INT NOT NULL,
    id_home_country INT NOT NULL,
    id_away_country INT NOT NULL,
    score_home_country INT NOT NULL,
    score_away_country INT NOT NULL,
    points INT NOT NULL,
    PRIMARY KEY (id_user, id_match)
);

ALTER TABLE PREDICTION ADD FOREIGN KEY (id_user) REFERENCES USER(id_student);
ALTER TABLE PREDICTION ADD FOREIGN KEY (id_match) REFERENCES FOOTBALL_MATCH(id_match);
ALTER TABLE PREDICTION ADD FOREIGN KEY (id_home_country) REFERENCES COUNTRY(id_country);
ALTER TABLE PREDICTION ADD FOREIGN KEY (id_away_country) REFERENCES COUNTRY(id_country);

CREATE TABLE NOTIFICATION (
    id_notification INT PRIMARY KEY AUTO_INCREMENT,
    id_user INT NOT NULL,
    message VARCHAR(100) NOT NULL
);

ALTER TABLE NOTIFICATION ADD FOREIGN KEY (id_user) REFERENCES USER(id_student);


#ver si se puede hacer un trigger para que se actualicen los puntos de los usuarios cuando se actualiza la tabla de partidos
#CREATE TRIGGER update_points AFTER UPDATE ON FOOTBALL_MATCH
#FOR EACH ROW
#BEGIN
#    UPDATE USER
#    SET total_points = total_points + 1
#    WHERE id_champion = id_winner OR id_sub_champion = id_winner;
#END;
#DELIMITER 1;
CREATE TABLE ADMIN (
    id_admin INT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

CREATE TABLE PRIZE (
    id_prize INT PRIMARY KEY AUTO_INCREMENT,
    description VARCHAR(50) NOT NULL,
    points INT NOT NULL
);


INSERT INTO STUDENT(name, surname, document)
    VALUE ("Ionas", "Josponis", "5242903-0");