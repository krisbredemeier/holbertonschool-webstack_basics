SELECT tv_shows.title, tv_show_genres.genre_id
FROM tvshows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id = tv_show_genres.show_id;
