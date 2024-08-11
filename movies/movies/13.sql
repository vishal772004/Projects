SELECT p.name FROM movies AS m JOIN stars AS s ON m.id=s.movie_id JOIN people AS p ON p.id=s.person_id WHERE NOT p.name="Kevin Bacon" AND s.movie_id IN
(SELECT p.name FROM movies AS m JOIN stars AS s ON m.id=s.movie_id JOIN people AS p ON p.id=s.person_id WHERE p.name="Kevin Bacon" AND p.birth=1958);
