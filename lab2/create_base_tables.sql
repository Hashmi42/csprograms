CREATE TABLE title_basics (
  title_id varchar(10) primary key,
  title_type varchar(12),
  primary_title varchar(400),
  original_title varchar(400),
  is_adult varchar(12),
  start_year int,
  end_year int,
  runtime_minutes int 
);

CREATE TABLE person_basics (
  person_id varchar(10) primary key,
  primary_name varchar(105),
  birth_year int,
  death_year int
);

CREATE TABLE directors (
  title_id varchar(10),
  person_id varchar(10),
  primary key(title_id,person_id)
);

CREATE TABLE person_professions (
  person_id varchar(10) references person_basics(person_id),
  profession varchar(25),
  primary key (person_id,profession)
);

CREATE TABLE principals (
  title_id varchar(10),
  person_id varchar(10),
  primary key (title_id, person_id)
);

CREATE TABLE stars (
  person_id varchar(10),
  title_id varchar(10),
  primary key(title_id,person_id)
);

CREATE TABLE title_episodes (
  title_id varchar(10) references title_basics(title_id),
  parent_title_id varchar(10),
  season_num int,
  episode_num int,
  primary key(title_id,parent_title_id)
);


CREATE TABLE title_genres (
  title_id varchar(10) references title_basics(title_id),
  genre varchar(11),
  primary key(title_id,genre)
);


CREATE TABLE title_ratings (
  title_id varchar(10) primary key references title_basics(title_id),
  average_rating numeric(3,1),
  num_votes int
);


CREATE TABLE writers (
  title_id varchar(10),
  person_id varchar(10),
  primary key(title_id,person_id)
);
