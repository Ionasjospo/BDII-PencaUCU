CREATE DATABASE PENCA_UCU;

USE PENCA_UCU;

CREATE TABLE COUNTRY (
    id_country INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL,
    cup_group VARCHAR(1) NOT NULL
);


CREATE TABLE USER (
    id_student INT PRIMARY KEY AUTO_INCREMENT,
    document VARCHAR(9) NOT NULL,
    username VARCHAR(50) NOT NULL,
    name VARCHAR(50) NOT NULL,
    surname VARCHAR(50) NOT NULL,
    email VARCHAR(50) NOT NULL,
    password VARCHAR(60) NOT NULL,
    total_points INT NOT NULL DEFAULT 0,
    id_champion INT,
    id_sub_champion INT,
    profile_picture VARCHAR(255)
);

ALTER TABLE USER ADD FOREIGN KEY (id_champion) REFERENCES COUNTRY(id_country);
ALTER TABLE USER ADD FOREIGN KEY (id_sub_champion) REFERENCES COUNTRY(id_country);

CREATE TABLE STAGE (
    id_stage INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE FOOTBALL_MATCH (
    id_match INT PRIMARY KEY AUTO_INCREMENT,
    date_match DATETIME NOT NULL,
    id_stage INT NOT NULL,
    id_home_country INT NOT NULL,
    id_away_country INT NOT NULL,
    score_home_country INT,
    score_away_country INT,
    id_winner INT
);

ALTER TABLE FOOTBALL_MATCH ADD FOREIGN KEY (id_stage) REFERENCES STAGE(id_stage);
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
    points INT,
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

-- Creacion de Indices
CREATE INDEX idx_username ON USER(username);
CREATE INDEX idx_id_user ON PREDICTION(id_user);
CREATE INDEX idx_id_match ON PREDICTION(id_match);
CREATE INDEX idx_id_stage ON FOOTBALL_MATCH(id_stage);
CREATE INDEX idx_id_home_country ON FOOTBALL_MATCH(id_home_country);
CREATE INDEX idx_id_away_country ON FOOTBALL_MATCH(id_away_country);
CREATE INDEX idx_id_winner ON FOOTBALL_MATCH(id_winner);
CREATE INDEX idx_cup_group ON COUNTRY(cup_group);
