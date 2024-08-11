SELECT m.title FROM movies AS m JOIN stars AS s ON m.id=s.movie_id JOIN people AS p ON p.id=s.person_id WHERE p.name="Jennifer Lawrence" AND m.title IN
(SELECT m.title FROM movies AS m JOIN stars AS s ON m.id=s.movie_id JOIN people AS p ON p.id=s.person_id WHERE p.name="Bradley Cooper");
