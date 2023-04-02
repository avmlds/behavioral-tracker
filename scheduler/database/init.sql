INSERT INTO
    activity (title, translations, value)
VALUES
    ('Health',      '{"en":"Health","ru":"Здоровье"}',        0),
    ('Chores',      '{"en":"Chores","ru":"Дом"}',             0),
    ('Work',        '{"en":"Work","ru":"Работа"}',            0),
    ('Study',       '{"en":"Study","ru":"Учёба"}',            0),
    ('Myself',      '{"en":"Myself","ru":"Я"}',               0),
    ('Environment', '{"en":"Environment","ru":"Обстановка"}', 0),
    ('Social',      '{"en":"Social","ru":"Окружение"}',       0),
    ('Family',      '{"en":"Family","ru":"Семья"}',           0);

INSERT INTO
    mood (id, title, translations, value)
VALUES
    (1, 'Mood',         '{"en":"Mood","ru": "Настроение"}', 0),
    (2, 'Disposition',  '{"en":"Disposition","ru": "Спокойствие"}', 0),
    (3, 'Productivity', '{"en":"Productivity","ru": "Продуктивность"}', 0),
    (4, 'Confidence',   '{"en":"Confidence","ru": "Уверенность"}', 0);

INSERT INTO
    spectrum (mood_id, title, translations, weight)
VALUES
    (1, 'Happy', '{"en":"Happy","ru":""}', 2),
    (1, 'Content', '{"en":"Content","ru":""}',1),
    (1, 'Neutral', '{"en":"Neutral","ru":""}',0),
    (1, 'Disappointed', '{"en":"Disappointed","ru":""}',-1),
    (1, 'Depressed', '{"en":"Depressed","ru":""}',-2),

    (2, 'Calm', '{"en":"Calm","ru":""}', 2),
    (2, 'Frustrated', '{"en":"Frustrated","ru":""}',1),
    (2, 'Irritated', '{"en":"Irritated","ru":""}',0),
    (2, 'Annoyed', '{"en":"Annoyed","ru":""}',-1),
    (2, 'Angry', '{"en":"Angry","ru":"З"}',-2),

    (3, 'Productive', '{"en":"Productive","ru":""}',2),
    (3, 'Motivated', '{"en":"Motivated","ru":""}',1),
    (3, 'Indecisive', '{"en":"Indecisive","ru":""}',0),
    (3, 'Overwhelmed', '{"en":"Overwhelmed","ru":""}',-1),
    (3, 'Procrastinating', '{"en":"Procrastinating","ru":""}',-2),

    (4, 'Confident', '{"en":"Confident","ru":""}',2),
    (4, 'Apprehensive', '{"en":"Apprehensive","ru":""}',1),
    (4, 'Nervous', '{"en":"Nervous","ru":""}',0),
    (4, 'Stressed', '{"en":"Stressed","ru":""}',-1),
    (4, 'Anxious', '{"en":"Anxious","ru":""}',-2);
