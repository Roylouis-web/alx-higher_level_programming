-- a script that lists all shows contained in the database hbtn_0d_tvshows.

SELECT DISTINCT `tv_shows`.`title`, `tv_show_genres`.`genre_id` FROM `tv_shows`
JOIN `tv_show_genres`
SELECT "NULL"
IF (`tv_show_genres`.`genre_id` IS NULL)
ORDER BY `tv_shows`.`title`, `tv_show_genres`.`genre_id` ASC; 
