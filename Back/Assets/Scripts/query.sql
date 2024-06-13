-- Actualizar Puntaje Usuarios
WITH Total_points AS (
    SELECT id_user, SUM(points) as Total_Points
    FROM PREDICTION
    WHERE points IS NOT NULL
    GROUP BY id_user
)
UPDATE USER
SET total_points = (SELECT Total_Points FROM Total_points WHERE Total_points.id_user = USER.id_student)
WHERE id_student IN (SELECT id_user FROM Total_points);

-- -- Actualizar puntaje en la prediccion de quienes acertaron Resultado Exacto
WITH exact_result AS (
    SELECT P.id_user, P.id_match
    FROM FOOTBALL_MATCH FM
    INNER JOIN PREDICTION P ON FM.id_match = P.id_match
    WHERE FM.score_home_country = P.score_home_country
    AND FM.score_away_country = P.score_away_country
)
UPDATE PREDICTION
SET points = 4
WHERE (id_user, id_match) IN (
    SELECT id_user, id_match
    FROM exact_result
);

-- Actualizar puntaje en la prediccion de quienes acertaron Ganador 
WITH winner_result AS (
    SELECT
        P.id_user,
        P.id_match
    FROM FOOTBALL_MATCH FM
    INNER JOIN PREDICTION P ON FM.id_match = P.id_match
    WHERE FM.id_winner = CASE
                            WHEN P.score_home_country > P.score_away_country THEN P.id_home_country
                            WHEN P.score_home_country < P.score_away_country THEN P.id_away_country
                        END
)
UPDATE PREDICTION
SET points = 2
WHERE (id_user, id_match) IN (
    SELECT id_user, id_match
    FROM winner_result
);