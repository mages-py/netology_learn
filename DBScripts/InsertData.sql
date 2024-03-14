INSERT INTO public.artists ("name") VALUES
('Ария'),
('Гран-Куражъ'),
('Руки вверх'),
('Madonna');

INSERT INTO public.genres ("name") VALUES
('ROCK'),
('POP'),
('RAP'),
('FOLK ROCK'),
('TECHNO');

INSERT INTO public.artist_genres (artist_id, genre_id) VALUES
(1, 1),
(2, 4),
(3, 2),
(4, 2),
(4, 1);


INSERT INTO public.albums ("name", realease_year) VALUES
('Music', 2000), --Madonna
('Madame X', 2019),
('Герой асфальта', 1987), --Ария
('Химера', 2001),
('Феникс', 2020),
('Без тормозов', 1999), --Руки вверх
('Открой мне дверь', 2012),
('Вечная игра', 2006), --GranKuraz
('Жить как никто другой', 2020);


INSERT INTO public.artist_albums (artist_id, album_id) VALUES
(4, 1),
(4, 2),
(1, 3),
(1, 4),
(1, 5),
(3, 6),
(3, 7),
(2, 8),
(2, 9),
(3, 9);


INSERT INTO public.tracks (album_id, "name", duration) VALUES
(1, 'My music', 225),
(1, 'Runaway Lover', 287),
(1, 'Paradise', 399),
(2, 'Future', 233),
(2, 'Crave', 201), --5
(2, 'Crazy', 242),
(2, 'Come Alive', 242),
(3, 'Штиль', 335),
(3, 'Небо тебя найдет', 331),
(3, 'Осколок льда', 325), --10
(3, 'Путь в никуда', 328),
(4, 'Черный квадрат', 320),
(4, 'Феникс', 395),
(4, 'Атилла', 476),
(4, 'Реквием', 265), --15
(5, 'Без тормозов', 208),
(5, 'Лучший парень', 257),
(5, 'Руки вверх', 222),
(5, 'Дома не сиди', 281),
(6, 'Мама', 254), --20
(6, 'Я тебя люблю мой ангел', 252),
(6, 'Останься', 295),
(6, 'Девочка из прошлого', 209),
(7, 'Дождь', 308),
(7, 'Теория хаоса', 228), --25
(7, 'Помни обо мне', 366),
(7, 'Царь', 261),
(8, 'Жить как никто другой', 303),
(8, 'Глоток воды', 212),
(8, 'Наперекор штормам', 277); --30

INSERT INTO public.collections ("name", realease_year) VALUES
('Russian ROCK', 2019),
('Russian Music', 2021),
('WORD MUSIC', 2018),
('Ария The Best', 2020);


INSERT INTO public.collection_tracks (collection_id, track_id) VALUES
(1, 8),
(1, 9),
(1, 10),
(1, 25),
(1, 26),
(1, 27),
(2, 16),
(2, 20),
(2, 28),
(2, 23),
(3, 1),
(3, 3),
(3, 5),
(3, 14),
(3, 24),
(4, 8),
(4, 9),
(4, 10);

