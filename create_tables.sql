
#USE magicbase.db "указать путь или выбирать бд из консольки и для нее выполнять запросы?"

CREATE TABLE FILMS_BLACKHOLE (id integer NOT NULL AUTOINCREMENT, film_id integer NOT NULL, film_name text NOT NULL, description text NOT NULL);
CREATE TABLE films_genre (id integer NOT NULL AUTOINCREMENT, genre_id integer NOT NULL ,film_id integer NOT NULL );
CREATE TABLE film_mood (id integer NOT NULL AUTOINCREMENT, mood_id integer NOT NULL , film_id integer NOT NULL );
CREATE TABLE watched_films (id integer NOT NULL AUTOINCREMENT, integer NOT NULL , user_id NOT NULL, film_id integer NOT NULL );
CREATE TABLE genre (id integer NOT NULL AUTOINCREMENT, name text NOT NULL);
CREATE TABLE mood (id integer NOT NULL AUTOINCREMENT, name text NOT NULL);
CREATE TABLE Regular_User (id integer NOT NULL AUTOINCREMENT, email text NOT NULL, username text NOT NULL, password text NOT NULL);
