/* selects all films directed by George Lucas */
select * from imdb.directors D INNER JOIN imdb.person_basics P on D.person_id = P.person_id  where primary_name = 'George Lucas';

/* returns the number of movies Tom Cruise has been in */
select count(*) from (select * from imdb.stars S inner join imdb.person_basics P on S.person_id = P.person_id where P.primary_name = 'Tom Cruise');

/* selects the movies that Tom Cruise has starred in */
select * from imdb.stars S inner join imdb.person_basics P on S.person_id = P.person_id where P.primary_name = 'Tom Cruise';

/* lists the projects that Tom Cruise has starred in (Actual title and information from title_basics)*/
select * from (select * from imdb.stars S inner join imdb.person_basics P on S.person_id = P.person_id) D inner join imdb.title_basics T on D.title_id = T.title_id where D.primary_name = 'Tom Cruise';

/* lists the projects that Steven Spielberg has directed (Actual title and info from title_basics)*/
select * from (select * from imdb.directors S inner join imdb.person_basics P on S.person_id = P.person_id) D inner join imdb.title_basics T on D.title_id = T.title_id where D.primary_name = 'Steven Spielberg';

/* lists the MOVIES that Steven Spielberg has directed (Actual title and info from title_basics)*/
select * from (select * from imdb.directors S inner join imdb.person_basics P on S.person_id = P.person_id) D inner join imdb.title_basics T on D.title_id = T.title_id where D.primary_name = 'Steven Spielberg' and T.title_type = 'movie';

/* selects the principals from the movie Interstellar and lists film info */
select * from (select * from imdb.principals S inner join imdb.person_basics P on S.person_id = P.person_id) D inner join imdb.title_basics T on D.title_id = T.title_id where T.primary_title = 'Interstellar' and title_type = 'movie';

/* Lists projects included in IMDB by ascending runtime */
select * from imdb.title_basics order by title_basics.runtime_minutes;

/* Lists all projects included in IMDB with title_basics and genre from the start_year 2012 */
select * from imdb.title_basics TB inner join imdb.title_genres TG on TB.title_id = TG.title_id where TB.start_year = 2012;

/* Lists the information and IMDB ratings for movies called "Memento" */
select * from imdb.title_ratings TR inner join imdb.title_basics TB on TR.title_id = TB.title_id where TB.primary_title = 'Memento' and TB.title_type = 'movie';

/* lists all directors with projects ordered by director birth year */
select * from imdb.directors D inner join imdb.person_basics PB on D.person_id = PB.person_id order by PB.birth_year;

/* lists all directors in person_basics alphabetized */
select * from imdb.person_basics PB inner join imdb.person_professions PP on PB.person_id = PP.person_id where PP.profession = 'director' order by PB.primary_name;

/* lists all movies form title_basics joined to ratings, orders by descending rating */
select * from imdb.title_basics TB inner join imdb.title_ratings TR on TB.title_id = TR.title_id where TB.title_type = 'movie' order by TR.average_rating desc;

/* selects episodes of the TV Show "Fringe" */
select * from imdb.title_episodes TE inner join imdb.title_basics TB on TE.title_id = TB.title_id where TB.primary_title = 'Fringe' order by TB.start_year asc;

/* displays JJ Abrams various roles */
select distinct PB.primary_name, PP.profession from imdb.person_professions PP inner join imdb.person_basics PB on PP.person_id = PP.person_id where PB.primary_name = 'J.J. Abrams' order by PP.profession;

/* Lists all writers alphabetically */
select PB.primary_name as "Writers" from imdb.writers W inner join imdb.person_basics PB on W.person_id = PB.person_id order by PB.primary_name;

/* selects stars from person_basics , displays both */
select * from imdb.stars S inner join imdb.person_basics PB on S.person_id = PB.person_id order by PB.primary_name;

/* lists the projects in imdb ordered by most recent to least */ 
select * from imdb.title_basics TB order by TB.start_year desc;

/* Alphabetizes project titles */
select PB.primary_name from imdb.person_basics PB order by PB.primary_name;

/* orders projects by genre */
select * from imdb.title_basics TB inner join imdb.title_genres G on TB.title_id = G.title_id order by G.genre;