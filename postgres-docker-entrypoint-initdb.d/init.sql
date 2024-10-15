CREATE TABLE films (
  id SERIAL PRIMARY KEY,
  title TEXT NOT NULL,
  release_year INT NOT NULL CHECK (release_year > 1800)
);
