/* creates title_rating_facts tables that are later joined to create title_rating_facts */
CREATE TABLE Title_Rating_Facts_Appalling AS 
select tb.title_type as title_type, tb.start_year as year, tg.genre as genre, count(tr.average_rating) as appalling_titles 
from title_basics tb 
join title_ratings tr on tb.title_id = tr.title_id 
join title_genres tg on tb.title_id=tg.title_id 
where tb.start_year is not null and tr.average_rating <= 2.0 
group by tb.title_type, tb.start_year, tg.genre 
order by tb.start_year, tb.title_type, tg.genre;

CREATE TABLE Title_Rating_Facts_Average AS 
select tb.title_type as title_type, tb.start_year as year, tg.genre as genre, count(tr.average_rating) as average_titles 
from title_basics tb 
join title_ratings tr on tb.title_id = tr.title_id 
join title_genres tg on tb.title_id=tg.title_id 
where tb.start_year is not null and tr.average_rating > 2.0 and tr.average_rating <= 7.9 
group by tb.title_type, tb.start_year, tg.genre 
order by tb.start_year, tb.title_type, tg.genre;

CREATE TABLE Title_Rating_Facts_Outstanding AS 
select tb.title_type as title_type, tb.start_year as year, tg.genre as genre, count(tr.average_rating) as outstanding_titles 
from title_basics tb 
join title_ratings tr on tb.title_id = tr.title_id 
join title_genres tg on tb.title_id=tg.title_id 
where tb.start_year is not null and tr.average_rating >= 8.0 
group by tb.title_type, tb.start_year, tg.genre 
order by tb.start_year, tb.title_type, tg.genre;

/* selects even where trfav.title_type, etc. are not null*/
CREATE TABLE title_rating_facts as 
select trfav.title_type, trfav.year, trfav.genre, trfap.appalling_titles, trfav.average_titles, trfo.outstanding_titles 
FROM title_rating_facts_appalling trfap 
full outer join title_rating_facts_average trfav on (trfap.title_type = trfav.title_type and trfap.year = trfav.year and trfap.genre = trfav.genre) 
full outer join title_rating_facts_outstanding trfo on (trfo.title_type = trfav.title_type and trfo.year = trfav.year and trfo.genre = trfav.genre) 
where (trfav.title_type is not null and trfav.year is not null and trfav.genre is not null);

update title_rating_facts set appalling_titles = 0 where appalling_titles is null;

update title_rating_facts set average_titles = 0 where average_titles is null;
  
update title_rating_facts set outstanding_titles = 0 where outstanding_titles is null;

ALTER TABLE title_rating_facts ADD CONSTRAINT PK_title_rating_facts PRIMARY KEY (title_type, year, genre);

CREATE VIEW v_outstanding_titles_by_year_genre AS 
select year, genre, sum(outstanding_titles) 
from title_rating_facts 
where year > 1930 and outstanding_titles > 0 
group by year, genre 
order by year, genre limit 100;