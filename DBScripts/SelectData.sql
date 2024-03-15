--============================== Задание 2 =====================================================
-- 1. Название и продолжительность самого длительного трека.
SELECT 
	"name", 
	duration 
FROM public.tracks
WHERE duration = (SELECT max(duration) AS max_duration FROM public.tracks t);

-- 2. Название треков, продолжительность которых не менее 3,5 минут.
SELECT 
	"name" 
FROM public.tracks
WHERE duration >= 210;

-- 3. Названия сборников, вышедших в период с 2018 по 2020 год включительно.
SELECT 
	"name" 
FROM public.collections
WHERE realease_year BETWEEN 2018 AND 2020;

-- 4. Исполнители, чьё имя состоит из одного слова.
SELECT 
	id, 
	"name" 
FROM public.artists
WHERE POSITION (' ' IN regexp_replace(trim("name"), '[^a-zA-Zа-яА-Я0-9 ]', ' ')) = 0;

-- 5. Название треков, которые содержат слово «мой» или «my».
SELECT 
	"name"
FROM public.tracks
WHERE strpos(upper("name"), 'MY') + strpos(upper("name"), 'МОЙ') > 0;


--============================== Задание 3 =====================================================
-- 1. Количество исполнителей в каждом жанре.
SELECT 
	ge."name" AS genre,
	count(ag.artist_id) AS qty_artists
FROM public.genres ge 
INNER JOIN public.artist_genres ag ON ge.id  = ag.genre_id  
GROUP BY ge."name";

-- 2. Количество треков, вошедших в альбомы 2019–2020 годов.
SELECT 
	a.realease_year AS year,
	count(DISTINCT t.id) AS qty 
FROM public.albums a
INNER JOIN public.tracks t  ON a.id = t.album_id
WHERE a.realease_year BETWEEN 2019 AND 2020
GROUP BY a.realease_year;

-- 3. Средняя продолжительность треков по каждому альбому.
SELECT 
	a."name" AS album,
	round(avg(t.duration)) AS avg_duration
FROM public.albums a
INNER JOIN public.tracks t  ON a.id = t.album_id
GROUP BY a."name";

-- 4. Все исполнители, которые не выпустили альбомы в 2020 году.
SELECT 
	art."name" 
FROM public.artists art
WHERE NOT art.id IN (
	SELECT DISTINCT aa.artist_id 
	FROM public.artist_albums aa 
	INNER JOIN public.albums a ON aa.album_id = a.id 
	WHERE a.realease_year = 2020);

-- 5. Названия сборников, в которых присутствует конкретный исполнитель (Ария id = 1).
SELECT DISTINCT  
	coll."name" AS collection
FROM public.collections AS coll
INNER JOIN public.collection_tracks ct ON coll.id  = ct.collection_id 
INNER JOIN public.tracks t ON ct.track_id  = t.id 
INNER JOIN public.artist_albums aa ON aa.album_id = t.album_id 
WHERE aa.artist_id = 1;


--============================== Задание 4 =====================================================
-- 1. Названия альбомов, в которых присутствуют исполнители более чем одного жанра.
SELECT 
	a."name" AS album 
FROM public.albums a
INNER JOIN public.artist_albums aa ON a.id  = aa.album_id 
WHERE aa.artist_id IN (SELECT ag.artist_id FROM public.artist_genres ag GROUP BY ag.artist_id HAVING count(ag.genre_id) > 1);

-- 2. Наименования треков, которые не входят в сборники.
SELECT 
	"name" AS track 
FROM public.tracks AS t
WHERE NOT EXISTS (SELECT 1 FROM public.collection_tracks ct WHERE ct.track_id = t.id);

-- 3. Исполнитель или исполнители, написавшие самый короткий по продолжительности трек, — теоретически таких треков может быть несколько.
SELECT 
	a."name" AS artist 
FROM public.artists a
INNER JOIN public.artist_albums aa ON a.id  = aa.artist_id 
INNER JOIN public.tracks t  ON aa.album_id  = t.album_id 
WHERE t.duration = (SELECT min(t2.duration) AS min_duration FROM public.tracks t2);

-- 4. Названия альбомов, содержащих наименьшее количество треков.
SELECT 
	a."name" AS album
FROM public.tracks t 
INNER JOIN public.albums a ON t.album_id  = a.id 
GROUP  BY a."name" 
HAVING count(t.id) = (SELECT count(id) AS qty FROM public.tracks GROUP BY album_id ORDER BY count(id) LIMIT 1);
