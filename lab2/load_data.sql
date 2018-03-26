\copy title_basics from /Users/jonathan/Downloads/pg/title_basics.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy person_basics from /Users/jonathan/Downloads/pg/person_basics.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy directors from /Users/jonathan/Downloads/split_directors/xaa (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy directors from /Users/jonathan/Downloads/split_directors/xab (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy directors from /Users/jonathan/Downloads/split_directors/xac (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy directors from /Users/jonathan/Downloads/split_directors/xad (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy person_professions from /Users/jonathan/Downloads/pg/person_professions.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xaa (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xab (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xac (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xad (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xae (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xaf (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xag (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xah (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xai (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xaj (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xak (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xal (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy principals from /Users/jonathan/Downloads/split_principals/xam (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xaa (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xab (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xac (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xad (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xae (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xaf (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy stars from /Users/jonathan/Downloads/split_stars/xag (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy title_episodes from /Users/jonathan/Downloads/pg/title_episodes.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy title_genres from /Users/jonathan/Downloads/pg/title_genres.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy title_ratings from /Users/jonathan/Downloads/pg/title_ratings.csv (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy writers from /Users/jonathan/Downloads/split_writers/xaa (header TRUE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy writers from /Users/jonathan/Downloads/split_writers/xab (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

\copy writers from /Users/jonathan/Downloads/split_writers/xac (header FALSE, format csv, delimiter ',', null '', encoding 'UTF8');

alter table principals add foreign key(title_id) references title_basics(title_id);
alter table principals add foreign key(person_id) references person_basics(person_id);

alter table directors add foreign key(title_id) references title_basics(title_id);
alter table directors add foreign key(person_id) references person_basics(person_id);

alter table stars add foreign key(title_id) references title_basics(title_id);
alter table stars add foreign key(person_id) references person_basics(person_id);

alter table writers add foreign key(title_id) references title_basics(title_id);
alter table writers add foreign key(person_id) references person_basics(person_id);