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
    password VARCHAR(60) NOT NULL,
    total_points INT NOT NULL,
    id_champion INT,
    id_sub_champion INT

);

ALTER TABLE USER ADD FOREIGN KEY (id_champion) REFERENCES COUNTRY(id_country);
ALTER TABLE USER ADD FOREIGN KEY (id_sub_champion) REFERENCES COUNTRY(id_country);

CREATE TABLE STAGE (
    id_stage INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50) NOT NULL
);

CREATE TABLE FOOTBALL_MATCH (
    id_match INT PRIMARY KEY AUTO_INCREMENT,
    date_match DATE NOT NULL,
    id_stage INT NOT NULL,
    id_home_country INT NOT NULL,
    id_away_country INT NOT NULL,
    score_home_country INT NOT NULL,
    score_away_country INT NOT NULL,
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


#Paises participantes
INSERT INTO COUNTRY(name) VALUES
('Argentina'),
('Bolivia'),
('Brasil'),
('Chile'),
('Colombia'),
('Ecuador'),
('Paraguay'),
('Perú'),
('Uruguay'),
('Venezuela'),
('Estados Unidos'),
('México'),
('Canadá'),
('Costa Rica'),
('Jamaica'),
('Panamá');


#Usuarios de prueba
INSERT INTO USER(document, username, name, surname, email, password, total_points, id_champion, id_sub_champion)
    VALUES
        ('5242903-0', 'Ionas_Josponis','Ionas', 'Josponis','ionas@gmail.com', '1234', 0, 1, 2),
        ('4658761-8', 'Lucas_Martino','Lucas', 'Martino','lucas@gmail.com', '1234', 0, 3, 5),
        ('1234567-8', 'Juan_Nocetti','Juan', 'Nocetti','juan@gmail.com', '1234', 0, 4, 6);

#Etapas de la copa
INSERT INTO STAGE(name) VALUES
('Primera ronda - Grupos'),
('Segunda ronda - Grupos'),
('Tercera Ronda - Grupos'),
('Cuartos de final'),
('Semifinales'),
('Tercer puesto'),
('Final');

#Partidos de la primera ronda
INSERT INTO FOOTBALL_MATCH(date_match, id_stage , id_home_country, id_away_country, score_home_country, score_away_country, id_winner)
    VALUES
        ('2024-06-20 21:00', 1 ,1, 13, 0, 0, null),
        ('2024-06-21 21:00', 1, 8, 4, 0, 0, null),
        ('2024-06-22 19:00', 1, 6, 10, 0, 0, null),
        ('2024-06-22 22:00', 1, 12, 15, 0, 0, null),
        ('2024-06-23 19:00', 1, 11, 2, 0, 0, null),
        ('2024-06-23 22:00', 1, 9, 16, 0, 0, null),
        ('2024-06-24 19:00', 1, 5, 7, 0, 0, null),
        ('2024-06-24 22:00', 1, 3, 14, 0, 0, null);
