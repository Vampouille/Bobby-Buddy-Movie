CREATE TABLE films (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  release_year INT NOT NULL CHECK (release_year > 1800),
  review TEXT NULL
);



INSERT INTO films (title, release_year, review) VALUES ('The Godfather', 1972, 'un bon film');
INSERT INTO films (title, release_year) VALUES ('Pulp Fiction', 1994);
INSERT INTO films (title, release_year) VALUES ('Schindler''s List', 1993);
INSERT INTO films (title, release_year) VALUES ('Inception', 2010);
INSERT INTO films (title, release_year) VALUES ('The Dark Knight', 2008);
INSERT INTO films (title, release_year) VALUES ('Fight Club', 1999);
INSERT INTO films (title, release_year) VALUES ('The Matrix', 1999);
INSERT INTO films (title, release_year) VALUES ('Forrest Gump', 1994);
INSERT INTO films (title, release_year) VALUES ('Gladiator', 2000);
INSERT INTO films (title, release_year) VALUES ('Braveheart', 1995);
INSERT INTO films (title, release_year) VALUES ('The Lord of the Rings: The Fellowship of the Ring', 2001);
INSERT INTO films (title, release_year) VALUES ('Star Wars: Episode IV - A New Hope', 1977);
INSERT INTO films (title, release_year) VALUES ('Saving Private Ryan', 1998);
INSERT INTO films (title, release_year) VALUES ('The Shawshank Redemption', 1994);
INSERT INTO films (title, release_year) VALUES ('The Silence of the Lambs', 1991);
INSERT INTO films (title, release_year) VALUES ('Goodfellas', 1990);
INSERT INTO films (title, release_year) VALUES ('The Departed', 2006);
INSERT INTO films (title, release_year) VALUES ('Se7en', 1995);
INSERT INTO films (title, release_year) VALUES ('Avatar', 2009);
INSERT INTO films (title, release_year) VALUES ('Jurassic Park', 1993);
