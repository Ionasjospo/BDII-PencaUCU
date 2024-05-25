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
    date_match DATETIME NOT NULL,
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
INSERT INTO COUNTRY(name, cup_group) VALUES
('Argentina', 'A'),
('Chile', 'A'),
('Perú', 'A'),
('Canadá', 'A'),
('México', 'B'),
('Ecuador', 'B'),
('Venezuela', 'B'),
('Jamaica', 'B'),
('Uruguay', 'C' ),
('Estados Unidos', 'C'),
('Panamá', 'C'),
('Bolivia', 'C'),
('Brasil', 'D'),
('Colombia', 'D'),
('Paraguay', 'D'),
('Costa Rica', 'D');


#Usuarios de prueba, no se puede porque la contra debe ser hasheada
# INSERT INTO USER(document, username, name, surname, email, password, total_points, id_champion, id_sub_champion)
#     VALUES
#         ('5242903-0', 'ionas9','Ionas', 'Josponis','ionas@gmail.com', '1234', 0, 1, 2),
#         ('4658761-8', 'marti','Lucas', 'Martino','lucas@gmail.com', '1234', 0, 3, 5),
#         ('1234567-8', 'juana','Juan', 'Nocetti','juan@gmail.com', '1234', 0, 4, 6);

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
INSERT INTO FOOTBALL_MATCH(date_match, id_stage, id_home_country, id_away_country, score_home_country, score_away_country, id_winner)
    VALUES
        ('2024-06-20 21:00', 1, 1, 4, 0, 0, NULL),
        ('2024-06-21 21:00', 1, 3, 2, 0, 0, NULL),
        ('2024-06-22 19:00', 1, 6, 7, 0, 0, NULL),
        ('2024-06-22 22:00', 1, 5, 8, 0, 0, NULL),
        ('2024-06-23 19:00', 1, 10, 12, 0, 0, NULL),
        ('2024-06-23 22:00', 1, 9, 11, 0, 0, NULL),
        ('2024-06-24 19:00', 1, 14, 15, 0, 0, NULL),
        ('2024-06-24 22:00', 1, 13, 16, 0, 0, NULL),
        ('2024-06-25 19:00', 1, 3, 4, 0, 0, NULL),
        ('2024-06-25 22:00', 1, 2, 1, 0, 0, NULL),
        ('2024-06-26 19:00', 1, 6, 8, 0, 0, NULL),
        ('2024-06-26 22:00', 1, 7, 5, 0, 0, NULL),
        ('2024-06-27 19:00', 1, 11, 10, 0, 0, NULL),
        ('2024-06-27 22:00', 1, 9, 12, 0, 0, NULL),
        ('2024-06-28 19:00', 1, 14, 16, 0, 0, NULL),
        ('2024-06-28 22:00', 1, 15, 13, 0, 0, NULL),
        ('2024-06-29 21:00', 1, 1, 3, 0, 0, NULL),
        ('2024-06-29 21:00', 1, 4, 2, 0, 0, NULL),
        ('2024-06-30 21:00', 1, 5, 6, 0, 0, NULL),
        ('2024-06-30 21:00', 1, 8, 7, 0, 0, NULL),
        ('2024-07-01 22:00', 1, 10, 9, 0, 0, NULL),
        ('2024-07-01 22:00', 1, 12, 11, 0, 0, NULL),
        ('2024-07-02 22:00', 1, 13, 14, 0, 0, NULL),
        ('2024-07-02 22:00', 1, 16, 15, 0, 0, NULL);
