
-- Paises participantes
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
('Costa Rica', 'D')
(' ', '-'); -- Pais sin equipo para cuando hay empate

-- Etapas de la copa
INSERT INTO STAGE(name) VALUES
('Primera ronda - Grupos'),
('Segunda ronda - Grupos'),
('Tercera Ronda - Grupos'),
('Cuartos de final'),
('Semifinales'),
('Tercer puesto'),
('Final');

-- Partidos de la primera ronda
INSERT INTO FOOTBALL_MATCH(date_match, id_stage, id_home_country, id_away_country, score_home_country, score_away_country, id_winner)
    VALUES
        ('2024-06-20 21:00', 1, 1, 4, NULL, NULL, NULL),
        ('2024-06-21 21:00', 1, 3, 2, NULL, NULL, NULL),
        ('2024-06-22 19:00', 1, 6, 7, NULL, NULL, NULL),
        ('2024-06-22 22:00', 1, 5, 8, NULL, NULL, NULL),
        ('2024-06-23 19:00', 1, 10, 12, NULL, NULL, NULL),
        ('2024-06-23 22:00', 1, 9, 11, NULL, NULL, NULL),
        ('2024-06-24 19:00', 1, 14, 15, NULL, NULL, NULL),
        ('2024-06-24 22:00', 1, 13, 16, NULL, NULL, NULL),
        ('2024-06-25 19:00', 1, 3, 4, NULL, NULL, NULL),
        ('2024-06-25 22:00', 1, 2, 1, NULL, NULL, NULL),
        ('2024-06-26 19:00', 1, 6, 8, NULL, NULL, NULL),
        ('2024-06-26 22:00', 1, 7, 5, NULL, NULL, NULL),
        ('2024-06-27 19:00', 1, 11, 10, NULL, NULL, NULL),
        ('2024-06-27 22:00', 1, 9, 12, NULL, NULL, NULL),
        ('2024-06-28 19:00', 1, 14, 16, NULL, NULL, NULL),
        ('2024-06-28 22:00', 1, 15, 13, NULL, NULL, NULL),
        ('2024-06-29 21:00', 1, 1, 3, NULL, NULL, NULL),
        ('2024-06-29 21:00', 1, 4, 2, NULL, NULL, NULL),
        ('2024-06-30 21:00', 1, 5, 6, NULL, NULL, NULL),
        ('2024-06-30 21:00', 1, 8, 7, NULL, NULL, NULL),
        ('2024-07-01 22:00', 1, 10, 9, NULL, NULL, NULL),
        ('2024-07-01 22:00', 1, 12, 11, NULL, NULL, NULL),
        ('2024-07-02 22:00', 1, 13, 14, NULL, NULL, NULL),
        ('2024-07-02 22:00', 1, 16, 15, NULL, NULL, NULL);

-- 50 Usuarios de prueba
INSERT INTO USER (document, username, name, surname, email, password, total_points, id_champion, id_sub_champion)
VALUES
    ('52429030', 'user1', 'John', 'Doe', 'user1@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 2),
    ('52429031', 'user2', 'Jane', 'Smith', 'user2@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 3, 4),
    ('52429032', 'user3', 'Michael', 'Johnson', 'user3@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 6),
    ('52429033', 'user4', 'Emily', 'Davis', 'user4@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 7, 8),
    ('52429034', 'user5', 'Daniel', 'Martinez', 'user5@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 9, 10),
    ('52429035', 'user6', 'Sophia', 'Garcia', 'user6@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 11, 12),
    ('52429036', 'user7', 'James', 'Rodriguez', 'user7@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 13, 14),
    ('52429037', 'user8', 'Olivia', 'Martinez', 'user8@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 15, 16),
    ('52429038', 'user9', 'William', 'Hernandez', 'user9@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 3),
    ('52429039', 'user10', 'Isabella', 'Lopez', 'user10@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 2, 4),
    ('52429040', 'user11', 'Alexander', 'Gonzalez', 'user11@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 7),
    ('52429041', 'user12', 'Mia', 'Perez', 'user12@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 6, 8),
    ('52429042', 'user13', 'Elijah', 'Wilson', 'user13@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 9, 11),
    ('52429043', 'user14', 'Amelia', 'Anderson', 'user14@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 10, 12),
    ('52429044', 'user15', 'Benjamin', 'Thomas', 'user15@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 13, 15),
    ('52429045', 'user16', 'Ava', 'Taylor', 'user16@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 14, 16),
    ('52429046', 'user17', 'Lucas', 'Moore', 'user17@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 5),
    ('52429047', 'user18', 'Charlotte', 'Jackson', 'user18@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 2, 6),
    ('52429048', 'user19', 'Mason', 'White', 'user19@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 3, 7),
    ('52429049', 'user20', 'Sophia', 'Harris', 'user20@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 4, 8),
    ('52429050', 'user21', 'Ethan', 'Martin', 'user21@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 9),
    ('52429051', 'user22', 'Olivia', 'Thompson', 'user22@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 6, 10),
    ('52429052', 'user23', 'Logan', 'Martinez', 'user23@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 7, 11),
    ('52429053', 'user24', 'Ava', 'Garcia', 'user24@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 8, 12),
    ('52429054', 'user25', 'James', 'Robinson', 'user25@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 9, 13),
    ('52429055', 'user26', 'Mia', 'Clark', 'user26@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 10, 14),
    ('52429056', 'user27', 'Henry', 'Lewis', 'user27@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 11, 15),
    ('52429057', 'user28', 'Amelia', 'Lee', 'user28@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 12, 16),
    ('52429058', 'user29', 'Jackson', 'Walker', 'user29@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 2),
    ('52429059', 'user30', 'Harper', 'Hall', 'user30@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 3, 4),
    ('52429060', 'user31', 'Sebastian', 'Allen', 'user31@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 6),
    ('52429061', 'user32', 'Evelyn', 'Young', 'user32@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 7, 8),
    ('52429062', 'user33', 'Jack', 'Hernandez', 'user33@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 9, 10),
    ('52429063', 'user34', 'Aria', 'King', 'user34@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 11, 12),
    ('52429064', 'user35', 'Aiden', 'Wright', 'user35@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 13, 14),
    ('52429065', 'user36', 'Ella', 'Lopez', 'user36@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 15, 16),
    ('52429066', 'user37', 'Samuel', 'Hill', 'user37@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 3),
    ('52429067', 'user38', 'Lily', 'Scott', 'user38@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 2, 4),
    ('52429068', 'user39', 'David', 'Green', 'user39@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 7),
    ('52429069', 'user40', 'Chloe', 'Adams', 'user40@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 6, 8),
    ('52429070', 'user41', 'Matthew', 'Baker', 'user41@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 9, 11),
    ('52429071', 'user42', 'Zoey', 'Gonzalez', 'user42@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 10, 12),
    ('52429072', 'user43', 'Jackson', 'Nelson', 'user43@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 13, 15),
    ('52429073', 'user44', 'Grace', 'Carter', 'user44@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 14, 16),
    ('52429074', 'user45', 'Liam', 'Mitchell', 'user45@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 1, 5),
    ('52429075', 'user46', 'Victoria', 'Perez', 'user46@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 2, 6),
    ('52429076', 'user47', 'Wyatt', 'Roberts', 'user47@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 3, 7),
    ('52429077', 'user48', 'Penelope', 'Phillips', 'user48@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 4, 8),
    ('52429078', 'user49', 'Andrew', 'Evans', 'user49@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 5, 9),
    ('52429079', 'user50', 'Avery', 'Turner', 'user50@example.com', '$2b$10$gB0QojkV6VQ/NCQHdHGvOuLfpNj3Tyl5dRdd70I80jMJu6aGc8eAS', 0, 6, 10);

-- Predicciones para el usuario 1
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (1, 1, 1, 4, 2, 1, NULL),
    (1, 2, 3, 2, 1, 1, NULL),
    (1, 3, 6, 7, 0, 2, NULL),
    (1, 4, 5, 8, 3, 1, NULL),
    (1, 5, 10, 12, 2, 2, NULL),
    (1, 6, 9, 11, 1, 0, NULL),
    (1, 7, 14, 15, 0, 0, NULL),
    (1, 8, 13, 16, 1, 1, NULL),
    (1, 9, 3, 4, 2, 1, NULL),
    (1, 10, 2, 1, 1, 3, NULL),
    (1, 11, 6, 8, 0, 1, NULL),
    (1, 12, 7, 5, 2, 0, NULL),
    (1, 13, 11, 10, 1, 2, NULL),
    (1, 14, 9, 12, 0, 0, NULL),
    (1, 15, 14, 16, 3, 3, NULL),
    (1, 16, 15, 13, 1, 1, NULL),
    (1, 17, 1, 3, 2, 0, NULL),
    (1, 18, 4, 2, 1, 1, NULL),
    (1, 19, 5, 6, 1, 3, NULL),
    (1, 20, 8, 7, 0, 1, NULL),
    (1, 21, 10, 9, 2, 1, NULL),
    (1, 22, 12, 11, 1, 0, NULL),
    (1, 23, 13, 14, 0, 0, NULL),
    (1, 24, 16, 15, 1, 2, NULL);

-- Predicciones para el usuario 2
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (2, 1, 1, 4, 1, 1, NULL),
    (2, 2, 3, 2, 2, 2, NULL),
    (2, 3, 6, 7, 1, 1, NULL),
    (2, 4, 5, 8, 0, 3, NULL),
    (2, 5, 10, 12, 2, 1, NULL),
    (2, 6, 9, 11, 3, 0, NULL),
    (2, 7, 14, 15, 0, 1, NULL),
    (2, 8, 13, 16, 2, 2, NULL),
    (2, 9, 3, 4, 1, 0, NULL),
    (2, 10, 2, 1, 2, 1, NULL),
    (2, 11, 6, 8, 1, 1, NULL),
    (2, 12, 7, 5, 0, 0, NULL),
    (2, 13, 11, 10, 2, 2, NULL),
    (2, 14, 9, 12, 1, 3, NULL),
    (2, 15, 14, 16, 0, 1, NULL),
    (2, 16, 15, 13, 2, 0, NULL),
    (2, 17, 1, 3, 1, 2, NULL),
    (2, 18, 4, 2, 1, 1, NULL),
    (2, 19, 5, 6, 0, 0, NULL),
    (2, 20, 8, 7, 3, 1, NULL),
    (2, 21, 10, 9, 1, 1, NULL),
    (2, 22, 12, 11, 0, 2, NULL),
    (2, 23, 13, 14, 1, 3, NULL),
    (2, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 3
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (3, 1, 1, 4, 3, 2, NULL),
    (3, 2, 3, 2, 1, 0, NULL),
    (3, 3, 6, 7, 2, 2, NULL),
    (3, 4, 5, 8, 0, 0, NULL),
    (3, 5, 10, 12, 1, 3, NULL),
    (3, 6, 9, 11, 1, 1, NULL),
    (3, 7, 14, 15, 3, 2, NULL),
    (3, 8, 13, 16, 2, 1, NULL),
    (3, 9, 3, 4, 1, 1, NULL),
    (3, 10, 2, 1, 2, 2, NULL),
    (3, 11, 6, 8, 1, 3, NULL),
    (3, 12, 7, 5, 1, 0, NULL),
    (3, 13, 11, 10, 0, 1, NULL),
    (3, 14, 9, 12, 2, 2, NULL),
    (3, 15, 14, 16, 1, 0, NULL),
    (3, 16, 15, 13, 0, 2, NULL),
    (3, 17, 1, 3, 0, 1, NULL),
    (3, 18, 4, 2, 3, 2, NULL),
    (3, 19, 5, 6, 2, 1, NULL),
    (3, 20, 8, 7, 1, 1, NULL),
    (3, 21, 10, 9, 2, 3, NULL),
    (3, 22, 12, 11, 2, 2, NULL),
    (3, 23, 13, 14, 1, 0, NULL),
    (3, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 4
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (4, 1, 1, 4, 1, 2, NULL),
    (4, 2, 3, 2, 0, 0, NULL),
    (4, 3, 6, 7, 3, 1, NULL),
    (4, 4, 5, 8, 2, 3, NULL),
    (4, 5, 10, 12, 1, 1, NULL),
    (4, 6, 9, 11, 0, 0, NULL),
    (4, 7, 14, 15, 2, 2, NULL),
    (4, 8, 13, 16, 3, 3, NULL),
    (4, 9, 3, 4, 0, 1, NULL),
    (4, 10, 2, 1, 2, 0, NULL),
    (4, 11, 6, 8, 1, 2, NULL),
    (4, 12, 7, 5, 2, 3, NULL),
    (4, 13, 11, 10, 0, 0, NULL),
    (4, 14, 9, 12, 1, 2, NULL),
    (4, 15, 14, 16, 3, 1, NULL),
    (4, 16, 15, 13, 2, 2, NULL),
    (4, 17, 1, 3, 1, 1, NULL),
    (4, 18, 4, 2, 3, 2, NULL),
    (4, 19, 5, 6, 0, 0, NULL),
    (4, 20, 8, 7, 1, 1, NULL),
    (4, 21, 10, 9, 2, 2, NULL),
    (4, 22, 12, 11, 3, 3, NULL),
    (4, 23, 13, 14, 2, 1, NULL),
    (4, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 5
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (5, 1, 1, 4, 0, 1, NULL),
    (5, 2, 3, 2, 1, 2, NULL),
    (5, 3, 6, 7, 1, 1, NULL),
    (5, 4, 5, 8, 3, 0, NULL),
    (5, 5, 10, 12, 2, 1, NULL),
    (5, 6, 9, 11, 2, 2, NULL),
    (5, 7, 14, 15, 0, 3, NULL),
    (5, 8, 13, 16, 1, 1, NULL),
    (5, 9, 3, 4, 3, 2, NULL),
    (5, 10, 2, 1, 1, 0, NULL),
    (5, 11, 6, 8, 2, 3, NULL),
    (5, 12, 7, 5, 1, 1, NULL),
    (5, 13, 11, 10, 3, 0, NULL),
    (5, 14, 9, 12, 0, 0, NULL),
    (5, 15, 14, 16, 1, 1, NULL),
    (5, 16, 15, 13, 2, 1, NULL),
    (5, 17, 1, 3, 0, 2, NULL),
    (5, 18, 4, 2, 1, 1, NULL),
    (5, 19, 5, 6, 3, 1, NULL),
    (5, 20, 8, 7, 0, 0, NULL),
    (5, 21, 10, 9, 1, 3, NULL),
    (5, 22, 12, 11, 2, 2, NULL),
    (5, 23, 13, 14, 1, 0, NULL),
    (5, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 6
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (6, 1, 1, 4, 1, 2, NULL),
    (6, 2, 3, 2, 0, 0, NULL),
    (6, 3, 6, 7, 3, 1, NULL),
    (6, 4, 5, 8, 2, 3, NULL),
    (6, 5, 10, 12, 1, 1, NULL),
    (6, 6, 9, 11, 0, 0, NULL),
    (6, 7, 14, 15, 2, 2, NULL),
    (6, 8, 13, 16, 3, 3, NULL),
    (6, 9, 3, 4, 0, 1, NULL),
    (6, 10, 2, 1, 2, 0, NULL),
    (6, 11, 6, 8, 1, 2, NULL),
    (6, 12, 7, 5, 2, 3, NULL),
    (6, 13, 11, 10, 0, 0, NULL),
    (6, 14, 9, 12, 1, 2, NULL),
    (6, 15, 14, 16, 3, 1, NULL),
    (6, 16, 15, 13, 2, 2, NULL),
    (6, 17, 1, 3, 1, 1, NULL),
    (6, 18, 4, 2, 3, 2, NULL),
    (6, 19, 5, 6, 0, 0, NULL),
    (6, 20, 8, 7, 1, 1, NULL),
    (6, 21, 10, 9, 2, 2, NULL),
    (6, 22, 12, 11, 3, 3, NULL),
    (6, 23, 13, 14, 2, 1, NULL),
    (6, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 7
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (7, 1, 1, 4, 0, 1, NULL),
    (7, 2, 3, 2, 1, 2, NULL),
    (7, 3, 6, 7, 1, 1, NULL),
    (7, 4, 5, 8, 3, 0, NULL),
    (7, 5, 10, 12, 2, 1, NULL),
    (7, 6, 9, 11, 2, 2, NULL),
    (7, 7, 14, 15, 0, 3, NULL),
    (7, 8, 13, 16, 1, 1, NULL),
    (7, 9, 3, 4, 3, 2, NULL),
    (7, 10, 2, 1, 1, 0, NULL),
    (7, 11, 6, 8, 2, 3, NULL),
    (7, 12, 7, 5, 1, 1, NULL),
    (7, 13, 11, 10, 3, 0, NULL),
    (7, 14, 9, 12, 0, 0, NULL),
    (7, 15, 14, 16, 1, 1, NULL),
    (7, 16, 15, 13, 2, 1, NULL),
    (7, 17, 1, 3, 0, 2, NULL),
    (7, 18, 4, 2, 1, 1, NULL),
    (7, 19, 5, 6, 3, 1, NULL),
    (7, 20, 8, 7, 0, 0, NULL),
    (7, 21, 10, 9, 1, 3, NULL),
    (7, 22, 12, 11, 2, 2, NULL),
    (7, 23, 13, 14, 1, 0, NULL),
    (7, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 8
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (8, 1, 1, 4, 1, 2, NULL),
    (8, 2, 3, 2, 0, 0, NULL),
    (8, 3, 6, 7, 3, 1, NULL),
    (8, 4, 5, 8, 2, 3, NULL),
    (8, 5, 10, 12, 1, 1, NULL),
    (8, 6, 9, 11, 0, 0, NULL),
    (8, 7, 14, 15, 2, 2, NULL),
    (8, 8, 13, 16, 3, 3, NULL),
    (8, 9, 3, 4, 0, 1, NULL),
    (8, 10, 2, 1, 2, 0, NULL),
    (8, 11, 6, 8, 1, 2, NULL),
    (8, 12, 7, 5, 2, 3, NULL),
    (8, 13, 11, 10, 0, 0, NULL),
    (8, 14, 9, 12, 1, 2, NULL),
    (8, 15, 14, 16, 3, 1, NULL),
    (8, 16, 15, 13, 2, 2, NULL),
    (8, 17, 1, 3, 1, 1, NULL),
    (8, 18, 4, 2, 3, 2, NULL),
    (8, 19, 5, 6, 0, 0, NULL),
    (8, 20, 8, 7, 1, 1, NULL),
    (8, 21, 10, 9, 2, 2, NULL),
    (8, 22, 12, 11, 3, 3, NULL),
    (8, 23, 13, 14, 2, 1, NULL),
    (8, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 9
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (9, 1, 1, 4, 0, 1, NULL),
    (9, 2, 3, 2, 1, 2, NULL),
    (9, 3, 6, 7, 1, 1, NULL),
    (9, 4, 5, 8, 3, 0, NULL),
    (9, 5, 10, 12, 2, 1, NULL),
    (9, 6, 9, 11, 2, 2, NULL),
    (9, 7, 14, 15, 0, 3, NULL),
    (9, 8, 13, 16, 1, 1, NULL),
    (9, 9, 3, 4, 3, 2, NULL),
    (9, 10, 2, 1, 1, 0, NULL),
    (9, 11, 6, 8, 2, 3, NULL),
    (9, 12, 7, 5, 1, 1, NULL),
    (9, 13, 11, 10, 3, 0, NULL),
    (9, 14, 9, 12, 0, 0, NULL),
    (9, 15, 14, 16, 1, 1, NULL),
    (9, 16, 15, 13, 2, 1, NULL),
    (9, 17, 1, 3, 0, 2, NULL),
    (9, 18, 4, 2, 1, 1, NULL),
    (9, 19, 5, 6, 3, 1, NULL),
    (9, 20, 8, 7, 0, 0, NULL),
    (9, 21, 10, 9, 1, 3, NULL),
    (9, 22, 12, 11, 2, 2, NULL),
    (9, 23, 13, 14, 1, 0, NULL),
    (9, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 10
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (10, 1, 1, 4, 1, 2, NULL),
    (10, 2, 3, 2, 0, 0, NULL),
    (10, 3, 6, 7, 3, 1, NULL),
    (10, 4, 5, 8, 2, 3, NULL),
    (10, 5, 10, 12, 1, 1, NULL),
    (10, 6, 9, 11, 0, 0, NULL),
    (10, 7, 14, 15, 2, 2, NULL),
    (10, 8, 13, 16, 3, 3, NULL),
    (10, 9, 3, 4, 0, 1, NULL),
    (10, 10, 2, 1, 2, 0, NULL),
    (10, 11, 6, 8, 1, 2, NULL),
    (10, 12, 7, 5, 2, 3, NULL),
    (10, 13, 11, 10, 0, 0, NULL),
    (10, 14, 9, 12, 1, 2, NULL),
    (10, 15, 14, 16, 3, 1, NULL),
    (10, 16, 15, 13, 2, 2, NULL),
    (10, 17, 1, 3, 1, 1, NULL),
    (10, 18, 4, 2, 3, 2, NULL),
    (10, 19, 5, 6, 0, 0, NULL),
    (10, 20, 8, 7, 1, 1, NULL),
    (10, 21, 10, 9, 2, 2, NULL),
    (10, 22, 12, 11, 3, 3, NULL),
    (10, 23, 13, 14, 2, 1, NULL),
    (10, 24, 16, 15, 1, 0, NULL);
    
-- Predicciones para el usuario 11
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (11, 1, 1, 4, 0, 1, NULL),
    (11, 2, 3, 2, 1, 2, NULL),
    (11, 3, 6, 7, 1, 1, NULL),
    (11, 4, 5, 8, 3, 0, NULL),
    (11, 5, 10, 12, 2, 1, NULL),
    (11, 6, 9, 11, 2, 2, NULL),
    (11, 7, 14, 15, 0, 3, NULL),
    (11, 8, 13, 16, 1, 1, NULL),
    (11, 9, 3, 4, 3, 2, NULL),
    (11, 10, 2, 1, 1, 0, NULL),
    (11, 11, 6, 8, 2, 3, NULL),
    (11, 12, 7, 5, 1, 1, NULL),
    (11, 13, 11, 10, 3, 0, NULL),
    (11, 14, 9, 12, 0, 0, NULL),
    (11, 15, 14, 16, 1, 1, NULL),
    (11, 16, 15, 13, 2, 1, NULL),
    (11, 17, 1, 3, 0, 2, NULL),
    (11, 18, 4, 2, 1, 1, NULL),
    (11, 19, 5, 6, 3, 1, NULL),
    (11, 20, 8, 7, 0, 0, NULL),
    (11, 21, 10, 9, 1, 3, NULL),
    (11, 22, 12, 11, 2, 2, NULL),
    (11, 23, 13, 14, 1, 0, NULL),
    (11, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 12
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (12, 1, 1, 4, 1, 2, NULL),
    (12, 2, 3, 2, 0, 0, NULL),
    (12, 3, 6, 7, 3, 1, NULL),
    (12, 4, 5, 8, 2, 3, NULL),
    (12, 5, 10, 12, 1, 1, NULL),
    (12, 6, 9, 11, 0, 0, NULL),
    (12, 7, 14, 15, 2, 2, NULL),
    (12, 8, 13, 16, 3, 3, NULL),
    (12, 9, 3, 4, 0, 1, NULL),
    (12, 10, 2, 1, 2, 0, NULL),
    (12, 11, 6, 8, 1, 2, NULL),
    (12, 12, 7, 5, 2, 3, NULL),
    (12, 13, 11, 10, 0, 0, NULL),
    (12, 14, 9, 12, 1, 2, NULL),
    (12, 15, 14, 16, 3, 1, NULL),
    (12, 16, 15, 13, 2, 2, NULL),
    (12, 17, 1, 3, 1, 1, NULL),
    (12, 18, 4, 2, 3, 2, NULL),
    (12, 19, 5, 6, 0, 0, NULL),
    (12, 20, 8, 7, 1, 1, NULL),
    (12, 21, 10, 9, 2, 2, NULL),
    (12, 22, 12, 11, 3, 3, NULL),
    (12, 23, 13, 14, 2, 1, NULL),
    (12, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 13
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (13, 1, 1, 4, 0, 1, NULL),
    (13, 2, 3, 2, 1, 2, NULL),
    (13, 3, 6, 7, 1, 1, NULL),
    (13, 4, 5, 8, 3, 0, NULL),
    (13, 5, 10, 12, 2, 1, NULL),
    (13, 6, 9, 11, 2, 2, NULL),
    (13, 7, 14, 15, 0, 3, NULL),
    (13, 8, 13, 16, 1, 1, NULL),
    (13, 9, 3, 4, 3, 2, NULL),
    (13, 10, 2, 1, 1, 0, NULL),
    (13, 11, 6, 8, 2, 3, NULL),
    (13, 12, 7, 5, 1, 1, NULL),
    (13, 13, 11, 10, 3, 0, NULL),
    (13, 14, 9, 12, 0, 0, NULL),
    (13, 15, 14, 16, 1, 1, NULL),
    (13, 16, 15, 13, 2, 1, NULL),
    (13, 17, 1, 3, 0, 2, NULL),
    (13, 18, 4, 2, 1, 1, NULL),
    (13, 19, 5, 6, 3, 1, NULL),
    (13, 20, 8, 7, 0, 0, NULL),
    (13, 21, 10, 9, 1, 3, NULL),
    (13, 22, 12, 11, 2, 2, NULL),
    (13, 23, 13, 14, 1, 0, NULL),
    (13, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 14
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (14, 1, 1, 4, 1, 2, NULL),
    (14, 2, 3, 2, 0, 0, NULL),
    (14, 3, 6, 7, 3, 1, NULL),
    (14, 4, 5, 8, 2, 3, NULL),
    (14, 5, 10, 12, 1, 1, NULL),
    (14, 6, 9, 11, 0, 0, NULL),
    (14, 7, 14, 15, 2, 2, NULL),
    (14, 8, 13, 16, 3, 3, NULL),
    (14, 9, 3, 4, 0, 1, NULL),
    (14, 10, 2, 1, 2, 0, NULL),
    (14, 11, 6, 8, 1, 2, NULL),
    (14, 12, 7, 5, 2, 3, NULL),
    (14, 13, 11, 10, 0, 0, NULL),
    (14, 14, 9, 12, 1, 2, NULL),
    (14, 15, 14, 16, 3, 1, NULL),
    (14, 16, 15, 13, 2, 2, NULL),
    (14, 17, 1, 3, 1, 1, NULL),
    (14, 18, 4, 2, 3, 2, NULL),
    (14, 19, 5, 6, 0, 0, NULL),
    (14, 20, 8, 7, 1, 1, NULL),
    (14, 21, 10, 9, 2, 2, NULL),
    (14, 22, 12, 11, 3, 3, NULL),
    (14, 23, 13, 14, 2, 1, NULL),
    (14, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 15
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (15, 1, 1, 4, 0, 1, NULL),
    (15, 2, 3, 2, 1, 2, NULL),
    (15, 3, 6, 7, 1, 1, NULL),
    (15, 4, 5, 8, 3, 0, NULL),
    (15, 5, 10, 12, 2, 1, NULL),
    (15, 6, 9, 11, 2, 2, NULL),
    (15, 7, 14, 15, 0, 3, NULL),
    (15, 8, 13, 16, 1, 1, NULL),
    (15, 9, 3, 4, 3, 2, NULL),
    (15, 10, 2, 1, 1, 0, NULL),
    (15, 11, 6, 8, 2, 3, NULL),
    (15, 12, 7, 5, 1, 1, NULL),
    (15, 13, 11, 10, 3, 0, NULL),
    (15, 14, 9, 12, 0, 0, NULL),
    (15, 15, 14, 16, 1, 1, NULL),
    (15, 16, 15, 13, 2, 1, NULL),
    (15, 17, 1, 3, 0, 2, NULL),
    (15, 18, 4, 2, 1, 1, NULL),
    (15, 19, 5, 6, 3, 1, NULL),
    (15, 20, 8, 7, 0, 0, NULL),
    (15, 21, 10, 9, 1, 3, NULL),
    (15, 22, 12, 11, 2, 2, NULL),
    (15, 23, 13, 14, 1, 0, NULL),
    (15, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 16
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (16, 1, 1, 4, 1, 2, NULL),
    (16, 2, 3, 2, 0, 0, NULL),
    (16, 3, 6, 7, 3, 1, NULL),
    (16, 4, 5, 8, 2, 3, NULL),
    (16, 5, 10, 12, 1, 1, NULL),
    (16, 6, 9, 11, 0, 0, NULL),
    (16, 7, 14, 15, 2, 2, NULL),
    (16, 8, 13, 16, 3, 3, NULL),
    (16, 9, 3, 4, 0, 1, NULL),
    (16, 10, 2, 1, 2, 0, NULL),
    (16, 11, 6, 8, 1, 2, NULL),
    (16, 12, 7, 5, 2, 3, NULL),
    (16, 13, 11, 10, 0, 0, NULL),
    (16, 14, 9, 12, 1, 2, NULL),
    (16, 15, 14, 16, 3, 1, NULL),
    (16, 16, 15, 13, 2, 2, NULL),
    (16, 17, 1, 3, 1, 1, NULL),
    (16, 18, 4, 2, 3, 2, NULL),
    (16, 19, 5, 6, 0, 0, NULL),
    (16, 20, 8, 7, 1, 1, NULL),
    (16, 21, 10, 9, 2, 2, NULL),
    (16, 22, 12, 11, 3, 3, NULL),
    (16, 23, 13, 14, 2, 1, NULL),
    (16, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 17
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (17, 1, 1, 4, 0, 1, NULL),
    (17, 2, 3, 2, 1, 2, NULL),
    (17, 3, 6, 7, 1, 1, NULL),
    (17, 4, 5, 8, 3, 0, NULL),
    (17, 5, 10, 12, 2, 1, NULL),
    (17, 6, 9, 11, 2, 2, NULL),
    (17, 7, 14, 15, 0, 3, NULL),
    (17, 8, 13, 16, 1, 1, NULL),
    (17, 9, 3, 4, 3, 2, NULL),
    (17, 10, 2, 1, 1, 0, NULL),
    (17, 11, 6, 8, 2, 3, NULL),
    (17, 12, 7, 5, 1, 1, NULL),
    (17, 13, 11, 10, 3, 0, NULL),
    (17, 14, 9, 12, 0, 0, NULL),
    (17, 15, 14, 16, 1, 1, NULL),
    (17, 16, 15, 13, 2, 1, NULL),
    (17, 17, 1, 3, 0, 2, NULL),
    (17, 18, 4, 2, 1, 1, NULL),
    (17, 19, 5, 6, 3, 1, NULL),
    (17, 20, 8, 7, 0, 0, NULL),
    (17, 21, 10, 9, 1, 3, NULL),
    (17, 22, 12, 11, 2, 2, NULL),
    (17, 23, 13, 14, 1, 0, NULL),
    (17, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 18
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (18, 1, 1, 4, 1, 2, NULL),
    (18, 2, 3, 2, 0, 0, NULL),
    (18, 3, 6, 7, 3, 1, NULL),
    (18, 4, 5, 8, 2, 3, NULL),
    (18, 5, 10, 12, 1, 1, NULL),
    (18, 6, 9, 11, 0, 0, NULL),
    (18, 7, 14, 15, 2, 2, NULL),
    (18, 8, 13, 16, 3, 3, NULL),
    (18, 9, 3, 4, 0, 1, NULL),
    (18, 10, 2, 1, 2, 0, NULL),
    (18, 11, 6, 8, 1, 2, NULL),
    (18, 12, 7, 5, 2, 3, NULL),
    (18, 13, 11, 10, 0, 0, NULL),
    (18, 14, 9, 12, 1, 2, NULL),
    (18, 15, 14, 16, 3, 1, NULL),
    (18, 16, 15, 13, 2, 2, NULL),
    (18, 17, 1, 3, 1, 1, NULL),
    (18, 18, 4, 2, 3, 2, NULL),
    (18, 19, 5, 6, 0, 0, NULL),
    (18, 20, 8, 7, 1, 1, NULL),
    (18, 21, 10, 9, 2, 2, NULL),
    (18, 22, 12, 11, 3, 3, NULL),
    (18, 23, 13, 14, 2, 1, NULL),
    (18, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 19
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (19, 1, 1, 4, 0, 1, NULL),
    (19, 2, 3, 2, 1, 2, NULL),
    (19, 3, 6, 7, 1, 1, NULL),
    (19, 4, 5, 8, 3, 0, NULL),
    (19, 5, 10, 12, 2, 1, NULL),
    (19, 6, 9, 11, 2, 2, NULL),
    (19, 7, 14, 15, 0, 3, NULL),
    (19, 8, 13, 16, 1, 1, NULL),
    (19, 9, 3, 4, 3, 2, NULL),
    (19, 10, 2, 1, 1, 0, NULL),
    (19, 11, 6, 8, 2, 3, NULL),
    (19, 12, 7, 5, 1, 1, NULL),
    (19, 13, 11, 10, 3, 0, NULL),
    (19, 14, 9, 12, 0, 0, NULL),
    (19, 15, 14, 16, 1, 1, NULL),
    (19, 16, 15, 13, 2, 1, NULL),
    (19, 17, 1, 3, 0, 2, NULL),
    (19, 18, 4, 2, 1, 1, NULL),
    (19, 19, 5, 6, 3, 1, NULL),
    (19, 20, 8, 7, 0, 0, NULL),
    (19, 21, 10, 9, 1, 3, NULL),
    (19, 22, 12, 11, 2, 2, NULL),
    (19, 23, 13, 14, 1, 0, NULL),
    (19, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 20
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (20, 1, 1, 4, 1, 2, NULL),
    (20, 2, 3, 2, 0, 0, NULL),
    (20, 3, 6, 7, 3, 1, NULL),
    (20, 4, 5, 8, 2, 3, NULL),
    (20, 5, 10, 12, 1, 1, NULL),
    (20, 6, 9, 11, 0, 0, NULL),
    (20, 7, 14, 15, 2, 2, NULL),
    (20, 8, 13, 16, 3, 3, NULL),
    (20, 9, 3, 4, 0, 1, NULL),
    (20, 10, 2, 1, 2, 0, NULL),
    (20, 11, 6, 8, 1, 2, NULL),
    (20, 12, 7, 5, 2, 3, NULL),
    (20, 13, 11, 10, 0, 0, NULL),
    (20, 14, 9, 12, 1, 2, NULL),
    (20, 15, 14, 16, 3, 1, NULL),
    (20, 16, 15, 13, 2, 2, NULL),
    (20, 17, 1, 3, 1, 1, NULL),
    (20, 18, 4, 2, 3, 2, NULL),
    (20, 19, 5, 6, 0, 0, NULL),
    (20, 20, 8, 7, 1, 1, NULL),
    (20, 21, 10, 9, 2, 2, NULL),
    (20, 22, 12, 11, 3, 3, NULL),
    (20, 23, 13, 14, 2, 1, NULL),
    (20, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 21
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (21, 1, 1, 4, 0, 1, NULL),
    (21, 2, 3, 2, 1, 2, NULL),
    (21, 3, 6, 7, 1, 1, NULL),
    (21, 4, 5, 8, 3, 0, NULL),
    (21, 5, 10, 12, 2, 1, NULL),
    (21, 6, 9, 11, 2, 2, NULL),
    (21, 7, 14, 15, 0, 3, NULL),
    (21, 8, 13, 16, 1, 1, NULL),
    (21, 9, 3, 4, 3, 2, NULL),
    (21, 10, 2, 1, 1, 0, NULL),
    (21, 11, 6, 8, 2, 3, NULL),
    (21, 12, 7, 5, 1, 1, NULL),
    (21, 13, 11, 10, 3, 0, NULL),
    (21, 14, 9, 12, 0, 0, NULL),
    (21, 15, 14, 16, 1, 1, NULL),
    (21, 16, 15, 13, 2, 1, NULL),
    (21, 17, 1, 3, 0, 2, NULL),
    (21, 18, 4, 2, 1, 1, NULL),
    (21, 19, 5, 6, 3, 1, NULL),
    (21, 20, 8, 7, 0, 0, NULL),
    (21, 21, 10, 9, 1, 3, NULL),
    (21, 22, 12, 11, 2, 2, NULL),
    (21, 23, 13, 14, 1, 0, NULL),
    (21, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 22
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (22, 1, 1, 4, 1, 2, NULL),
    (22, 2, 3, 2, 0, 0, NULL),
    (22, 3, 6, 7, 3, 1, NULL),
    (22, 4, 5, 8, 2, 3, NULL),
    (22, 5, 10, 12, 1, 1, NULL),
    (22, 6, 9, 11, 0, 0, NULL),
    (22, 7, 14, 15, 2, 2, NULL),
    (22, 8, 13, 16, 3, 3, NULL),
    (22, 9, 3, 4, 0, 1, NULL),
    (22, 10, 2, 1, 2, 0, NULL),
    (22, 11, 6, 8, 1, 2, NULL),
    (22, 12, 7, 5, 2, 3, NULL),
    (22, 13, 11, 10, 0, 0, NULL),
    (22, 14, 9, 12, 1, 2, NULL),
    (22, 15, 14, 16, 3, 1, NULL),
    (22, 16, 15, 13, 2, 2, NULL),
    (22, 17, 1, 3, 1, 1, NULL),
    (22, 18, 4, 2, 3, 2, NULL),
    (22, 19, 5, 6, 0, 0, NULL),
    (22, 20, 8, 7, 1, 1, NULL),
    (22, 21, 10, 9, 2, 2, NULL),
    (22, 22, 12, 11, 3, 3, NULL),
    (22, 23, 13, 14, 2, 1, NULL),
    (22, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 23
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (23, 1, 1, 4, 0, 1, NULL),
    (23, 2, 3, 2, 1, 2, NULL),
    (23, 3, 6, 7, 1, 1, NULL),
    (23, 4, 5, 8, 3, 0, NULL),
    (23, 5, 10, 12, 2, 1, NULL),
    (23, 6, 9, 11, 2, 2, NULL),
    (23, 7, 14, 15, 0, 3, NULL),
    (23, 8, 13, 16, 1, 1, NULL),
    (23, 9, 3, 4, 3, 2, NULL),
    (23, 10, 2, 1, 1, 0, NULL),
    (23, 11, 6, 8, 2, 3, NULL),
    (23, 12, 7, 5, 1, 1, NULL),
    (23, 13, 11, 10, 3, 0, NULL),
    (23, 14, 9, 12, 0, 0, NULL),
    (23, 15, 14, 16, 1, 1, NULL),
    (23, 16, 15, 13, 2, 1, NULL),
    (23, 17, 1, 3, 0, 2, NULL),
    (23, 18, 4, 2, 1, 1, NULL),
    (23, 19, 5, 6, 3, 1, NULL),
    (23, 20, 8, 7, 0, 0, NULL),
    (23, 21, 10, 9, 1, 3, NULL),
    (23, 22, 12, 11, 2, 2, NULL),
    (23, 23, 13, 14, 1, 0, NULL),
    (23, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 24
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (24, 1, 1, 4, 1, 2, NULL),
    (24, 2, 3, 2, 0, 0, NULL),
    (24, 3, 6, 7, 3, 1, NULL),
    (24, 4, 5, 8, 2, 3, NULL),
    (24, 5, 10, 12, 1, 1, NULL),
    (24, 6, 9, 11, 0, 0, NULL),
    (24, 7, 14, 15, 2, 2, NULL),
    (24, 8, 13, 16, 3, 3, NULL),
    (24, 9, 3, 4, 0, 1, NULL),
    (24, 10, 2, 1, 2, 0, NULL),
    (24, 11, 6, 8, 1, 2, NULL),
    (24, 12, 7, 5, 2, 3, NULL),
    (24, 13, 11, 10, 0, 0, NULL),
    (24, 14, 9, 12, 1, 2, NULL),
    (24, 15, 14, 16, 3, 1, NULL),
    (24, 16, 15, 13, 2, 2, NULL),
    (24, 17, 1, 3, 1, 1, NULL),
    (24, 18, 4, 2, 3, 2, NULL),
    (24, 19, 5, 6, 0, 0, NULL),
    (24, 20, 8, 7, 1, 1, NULL),
    (24, 21, 10, 9, 2, 2, NULL),
    (24, 22, 12, 11, 3, 3, NULL),
    (24, 23, 13, 14, 2, 1, NULL),
    (24, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 25
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (25, 1, 1, 4, 0, 1, NULL),
    (25, 2, 3, 2, 1, 2, NULL),
    (25, 3, 6, 7, 1, 1, NULL),
    (25, 4, 5, 8, 3, 0, NULL),
    (25, 5, 10, 12, 2, 1, NULL),
    (25, 6, 9, 11, 2, 2, NULL),
    (25, 7, 14, 15, 0, 3, NULL),
    (25, 8, 13, 16, 1, 1, NULL),
    (25, 9, 3, 4, 3, 2, NULL),
    (25, 10, 2, 1, 1, 0, NULL),
    (25, 11, 6, 8, 2, 3, NULL),
    (25, 12, 7, 5, 1, 1, NULL),
    (25, 13, 11, 10, 3, 0, NULL),
    (25, 14, 9, 12, 0, 0, NULL),
    (25, 15, 14, 16, 1, 1, NULL),
    (25, 16, 15, 13, 2, 1, NULL),
    (25, 17, 1, 3, 0, 2, NULL),
    (25, 18, 4, 2, 1, 1, NULL),
    (25, 19, 5, 6, 3, 1, NULL),
    (25, 20, 8, 7, 0, 0, NULL),
    (25, 21, 10, 9, 1, 3, NULL),
    (25, 22, 12, 11, 2, 2, NULL),
    (25, 23, 13, 14, 1, 0, NULL),
    (25, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 26
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (26, 1, 1, 4, 1, 2, NULL),
    (26, 2, 3, 2, 0, 0, NULL),
    (26, 3, 6, 7, 3, 1, NULL),
    (26, 4, 5, 8, 2, 3, NULL),
    (26, 5, 10, 12, 1, 1, NULL),
    (26, 6, 9, 11, 0, 0, NULL),
    (26, 7, 14, 15, 2, 2, NULL),
    (26, 8, 13, 16, 3, 3, NULL),
    (26, 9, 3, 4, 0, 1, NULL),
    (26, 10, 2, 1, 2, 0, NULL),
    (26, 11, 6, 8, 1, 2, NULL),
    (26, 12, 7, 5, 2, 3, NULL),
    (26, 13, 11, 10, 0, 0, NULL),
    (26, 14, 9, 12, 1, 2, NULL),
    (26, 15, 14, 16, 3, 1, NULL),
    (26, 16, 15, 13, 2, 2, NULL),
    (26, 17, 1, 3, 1, 1, NULL),
    (26, 18, 4, 2, 3, 2, NULL),
    (26, 19, 5, 6, 0, 0, NULL),
    (26, 20, 8, 7, 1, 1, NULL),
    (26, 21, 10, 9, 2, 2, NULL),
    (26, 22, 12, 11, 3, 3, NULL),
    (26, 23, 13, 14, 2, 1, NULL),
    (26, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 27
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (27, 1, 1, 4, 0, 1, NULL),
    (27, 2, 3, 2, 1, 2, NULL),
    (27, 3, 6, 7, 1, 1, NULL),
    (27, 4, 5, 8, 3, 0, NULL),
    (27, 5, 10, 12, 2, 1, NULL),
    (27, 6, 9, 11, 2, 2, NULL),
    (27, 7, 14, 15, 0, 3, NULL),
    (27, 8, 13, 16, 1, 1, NULL),
    (27, 9, 3, 4, 3, 2, NULL),
    (27, 10, 2, 1, 1, 0, NULL),
    (27, 11, 6, 8, 2, 3, NULL),
    (27, 12, 7, 5, 1, 1, NULL),
    (27, 13, 11, 10, 3, 0, NULL),
    (27, 14, 9, 12, 0, 0, NULL),
    (27, 15, 14, 16, 1, 1, NULL),
    (27, 16, 15, 13, 2, 1, NULL),
    (27, 17, 1, 3, 0, 2, NULL),
    (27, 18, 4, 2, 1, 1, NULL),
    (27, 19, 5, 6, 3, 1, NULL),
    (27, 20, 8, 7, 0, 0, NULL),
    (27, 21, 10, 9, 1, 3, NULL),
    (27, 22, 12, 11, 2, 2, NULL),
    (27, 23, 13, 14, 1, 0, NULL),
    (27, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 28
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (28, 1, 1, 4, 1, 2, NULL),
    (28, 2, 3, 2, 0, 0, NULL),
    (28, 3, 6, 7, 3, 1, NULL),
    (28, 4, 5, 8, 2, 3, NULL),
    (28, 5, 10, 12, 1, 1, NULL),
    (28, 6, 9, 11, 0, 0, NULL),
    (28, 7, 14, 15, 2, 2, NULL),
    (28, 8, 13, 16, 3, 3, NULL),
    (28, 9, 3, 4, 0, 1, NULL),
    (28, 10, 2, 1, 2, 0, NULL),
    (28, 11, 6, 8, 1, 2, NULL),
    (28, 12, 7, 5, 2, 3, NULL),
    (28, 13, 11, 10, 0, 0, NULL),
    (28, 14, 9, 12, 1, 2, NULL),
    (28, 15, 14, 16, 3, 1, NULL),
    (28, 16, 15, 13, 2, 2, NULL),
    (28, 17, 1, 3, 1, 1, NULL),
    (28, 18, 4, 2, 3, 2, NULL),
    (28, 19, 5, 6, 0, 0, NULL),
    (28, 20, 8, 7, 1, 1, NULL),
    (28, 21, 10, 9, 2, 2, NULL),
    (28, 22, 12, 11, 3, 3, NULL),
    (28, 23, 13, 14, 2, 1, NULL),
    (28, 24, 16, 15, 1, 0, NULL);

-- Predicciones para el usuario 29
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (29, 1, 1, 4, 0, 1, NULL),
    (29, 2, 3, 2, 1, 2, NULL),
    (29, 3, 6, 7, 1, 1, NULL),
    (29, 4, 5, 8, 3, 0, NULL),
    (29, 5, 10, 12, 2, 1, NULL),
    (29, 6, 9, 11, 2, 2, NULL),
    (29, 7, 14, 15, 0, 3, NULL),
    (29, 8, 13, 16, 1, 1, NULL),
    (29, 9, 3, 4, 3, 2, NULL),
    (29, 10, 2, 1, 1, 0, NULL),
    (29, 11, 6, 8, 2, 3, NULL),
    (29, 12, 7, 5, 1, 1, NULL),
    (29, 13, 11, 10, 3, 0, NULL),
    (29, 14, 9, 12, 0, 0, NULL),
    (29, 15, 14, 16, 1, 1, NULL),
    (29, 16, 15, 13, 2, 1, NULL),
    (29, 17, 1, 3, 0, 2, NULL),
    (29, 18, 4, 2, 1, 1, NULL),
    (29, 19, 5, 6, 3, 1, NULL),
    (29, 20, 8, 7, 0, 0, NULL),
    (29, 21, 10, 9, 1, 3, NULL),
    (29, 22, 12, 11, 2, 2, NULL),
    (29, 23, 13, 14, 1, 0, NULL),
    (29, 24, 16, 15, 0, 1, NULL);

-- Predicciones para el usuario 30
INSERT INTO PREDICTION (id_user, id_match, id_home_country, id_away_country, score_home_country, score_away_country, points)
VALUES
    (30, 1, 1, 4, 1, 2, NULL),
    (30, 2, 3, 2, 0, 0, NULL),
    (30, 3, 6, 7, 3, 1, NULL),
    (30, 4, 5, 8, 2, 3, NULL),
    (30, 5, 10, 12, 1, 1, NULL),
    (30, 6, 9, 11, 0, 0, NULL),
    (30, 7, 14, 15, 2, 2, NULL),
    (30, 8, 13, 16, 3, 3, NULL),
    (30, 9, 3, 4, 0, 1, NULL),
    (30, 10, 2, 1, 2, 0, NULL),
    (30, 11, 6, 8, 1, 2, NULL),
    (30, 12, 7, 5, 2, 3, NULL),
    (30, 13, 11, 10, 0, 0, NULL),
    (30, 14, 9, 12, 1, 2, NULL),
    (30, 15, 14, 16, 3, 1, NULL),
    (30, 16, 15, 13, 2, 2, NULL),
    (30, 17, 1, 3, 1, 1, NULL),
    (30, 18, 4, 2, 3, 2, NULL),
    (30, 19, 5, 6, 0, 0, NULL),
    (30, 20, 8, 7, 1, 1, NULL),
    (30, 21, 10, 9, 2, 2, NULL),
    (30, 22, 12, 11, 3, 3, NULL),
    (30, 23, 13, 14, 2, 1, NULL),
    (30, 24, 16, 15, 1, 0, NULL);