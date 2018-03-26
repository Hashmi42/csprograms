/* selects all titles where average_rating on IMDB is equal to the average rating on movielens */
create view v_movielens_rating as select tb.primary_title as Title, tb.start_year as Year, tr.average_rating as IMDB_Rating, tr.movielens_rating as MovieLens_Rating from title_ratings tr
join title_basics tb on tr.title_id = tb.title_id
where tr.movielens_rating = tr.average_rating;