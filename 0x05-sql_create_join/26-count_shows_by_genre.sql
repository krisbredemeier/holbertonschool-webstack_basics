-- Write a script that lists all genres from hbtn_0d_tvshows and displays
-- the number of shows linked to each.
SELECT tv_genres.name AS `genre`,
COUNT(*) AS `number_shows`
FROM tv.genre
JOIN tv_show.genres
ON tv_genre.id = tv_show_genres.genre_id
GROUP BY tv_genre.name
ORDER BY DESC `number_shows`;
