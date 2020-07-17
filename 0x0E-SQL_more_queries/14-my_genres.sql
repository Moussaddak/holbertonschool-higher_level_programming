-- 14. My genres
-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
USE tv_genres
SELECT name
FROM tv_genres
INNER JOIN tv_show_genres
ON id = tv_show_genres.genre_id
INNER JOIN tv_shows
ON tv_show_genres.show_id = tv_shows.id
WHERE tv_shows.title = "Dexter"
ORDER BY tv_genres.name;
