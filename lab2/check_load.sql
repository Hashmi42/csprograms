select count(*) from directors;
/* returns 31084804 */

select count(*) from person_basics;
/* returns 8108929 */

select count(*) from person_professions;
/* returns 9177654 */

select count(*) from principals;
/* returns 25139892 */

select count(*) from stars;
/* returns 13867186 */

select count(*) from title_basics;
/* returns 4486305 */

select count(*) from title_episodes;
/* returns 2949107 */

select count(*) from title_genres;
/* returns 6571818 */

select count(*) from title_ratings;
/* returns 759962 */

select count(*) from writers;
/* returns 4828480 */

/* displays JJ Abrams various roles; can compare with results from lab1 */
select distinct PB.primary_name, PP.profession from person_professions PP inner join person_basics PB on PP.person_id = PP.person_id where PB.primary_name = 'J.J. Abrams' order by PP.profession;

/* lists the projects that Tom Cruise has starred in (Actual title and information from title_basics); can compare with results from lab1 on Athena for verification*/
select * from (select * from stars S inner join person_basics P on S.person_id = P.person_id) D inner join title_basics T on D.title_id = T.title_id where D.primary_name = 'Tom Cruise';

/* Lists the information and IMDB ratings for movies called "Memento"; can crosscheck with results from Lab1 on Athena*/
select * from title_ratings TR inner join title_basics TB on TR.title_id = TB.title_id where TB.primary_title = 'Memento' and TB.title_type = 'movie';