#Exercicios Neo4J

##Execicio 1

* Exercise 1.1: Retrieve all nodes from the database.
#### Comando
~~~~ javascript
MATCH(m) return m
~~~~


• Exercise 1.2: Examine the data model for the graph.
#### Resultado
~~~~ javascript
 DONE
~~~~


• Exercise 1.3: Retrieve all Person nodes.
#### Comando
~~~~ javascript
MATCH(p:Person) return p
~~~~

• Exercise 1.4: Retrieve all Movie nodes.
#### Comando
~~~~ javascript
MATCH(m:Movie) return m
~~~~

## Exercicio 2

* Exercise 2.1: Retrieve all movies that were released in a specific year.
#### Comando
~~~~ javascript
MATCH(m:Movie) WHERE m.released = 1986 return m
~~~~

• Exercise 2.2: View the retrieved results as a table.
#### Comando
~~~~ javascript
 DONE

~~~~

• Exercise 2.3: Query the database for all property keys.
#### Comando
~~~~ javascript
MATCH (l) UNWIND keys(l) as key RETURN distinct key
~~~~

• Exercise 2.4: Retrieve all Movies released in a specific year, returning
their titles.
#### Comando
~~~~ javascript
MATCH(m:Movie) WHERE m.released = 1986 return m.title
~~~~

• Exercise 2.5: Display title, released, and tagline values for every Movie
node in the graph.
#### Comando
~~~~ javascript
MATCH(m:Movie) return m.title, m.released, m.tagline
~~~~

• Exercise 2.6: Display more user-friendly headers in the table
#### Comando
~~~~ javascript
MATCH(m:Movie) return m.title as Titulo, m.released as Ano, m.tagline as Subtitulo
~~~~


Exercicio 3

Exercise 3.1: Display the schema of the database.
#### Comando
~~~~ javascript
call db.schema.visualization
~~~~

• Exercise 3.2: Retrieve all people who wrote the movie Speed Racer.
#### Comando
~~~~ javascript
MATCH (speed {title: "Speed Racer"})<-[:WROTE]-(directors) RETURN directors.name
~~~~

• Exercise 3.3: Retrieve all movies that are connected to the person,
Tom Hanks.
#### Comando
~~~~ javascript
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies) RETURN tom,tomHanksMovies
~~~~

• Exercise 3.4: Retrieve information about the relationships Tom Hanks
had with the set of movies retrieved earlier.
#### Comando
~~~~ javascript
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies)-[relatedTo]-(p:Person) RETURN tom,tomHanksMovies,Type(relatedTo)
~~~~

• Exercise 3.5: Retrieve information about the roles that Tom Hanks
acted in.
#### Comando
~~~~ javascript
MATCH (tom:Person {name: "Tom Hanks"})-[:ACTED_IN]->(tomHanksMovies)-[relatedTo]-(p:Person) RETURN tom,tomHanksMovies,Type(relatedTo)
~~~~


## Execicio 4

* Exercise 4.1: Retrieve all movies that Tom Cruise acted in.
#### Comando
~~~~ javascript
MATCH (tom:Person {name: "Tom Cruise"})-[:ACTED_IN]->(tomMovies) RETURN tom,tomMovies
~~~~

* Exercise 4.2: Retrieve all people that were born in the 70’s.
#### Comando
~~~~ javascript
MATCH(p:Person) where p.born >= 1970 and p.born < 1980 return p
~~~~
* Exercise 4.3: Retrieve the actors who acted in the movie The Matrix
who were born after 1960.
#### Comando
~~~~ javascript
MATCH(p:Person)- [:ACTED_IN]->(m:Movie {title: "The Matrix"}) WHERE p.born >= 1960 return p
~~~~
* Exercise 4.4: Retrieve all movies by testing the node label and a property.
#### Comando
~~~~ javascript
MATCH (m) WHERE m:Movie AND m.released = 1999 RETURN m.title
~~~~
* Exercise 4.5: Retrieve all people that wrote movies by testing the relationship between two nodes.
#### Comando
~~~~ javascript
MATCH (p)-[rel]->(m) WHERE p:Person AND type(rel) = 'WROTE' AND m:Movie RETURN p.name as Name, m.title as Movie
~~~~
* Exercise 4.6: Retrieve all people in the graph that do not have a property.
#### Comando
~~~~ javascript
MATCH (p:Person) WHERE NOT exists(p.born) RETURN p.name as Name
~~~~
* Exercise 4.7: Retrieve all people related to movies where the relationship has a property.
#### Comando
~~~~ javascript
MATCH (p:Person)-[rel]->(m:Movie) WHERE exists(rel.rating) RETURN p.name as Name, m.title as Movie, rel.rating as Rating
~~~~
* Exercise 4.8: Retrieve all actors whose name begins with James.
#### Comando
~~~~ javascript
MATCH (p:Person)-[:ACTED_IN]->(:Movie) WHERE p.name STARTS WITH 'James' RETURN p.name
~~~~
* Exercise 4.9: Retrieve all all REVIEW relationships from the graph with filtered results.
#### Comando
~~~~ javascript
MATCH (:Person)-[r:REVIEWED]->(m:Movie) WHERE toLower(r.summary) CONTAINS 'fun' RETURN  m.title as Movie, r.summary as Review, r.rating as Rating~~~~

* Exercise 4.10: Retrieve all people who have produced a movie, but have not directed a movie.
#### Comando
~~~~ javascript
MATCH (a:Person)-[:PRODUCED]->(m:Movie) WHERE NOT ((a)-[:DIRECTED]->(:Movie)) RETURN a.name, m.title
~~~~
* Exercise 4.11: Retrieve the movies and their actors where one of the actors also directed the movie.
#### Comando
~~~~ javascript
MATCH (p1:Person)-[:ACTED_IN]->(m:Movie)<-[:ACTED_IN]-(p2:Person) WHERE exists( (p2)-[:DIRECTED]->(m) ) RETURN  p1.name as Actor, p2.name as `Actor/Director`, m.title as Movie 
~~~~
* Exercise 4.12: Retrieve all movies that were released in a set of years.
#### Comando
~~~~ javascript
MATCH (m:Movie) WHERE m.released in [1999, 2000] RETURN m.title, m.released
~~~~
* Exercise 4.13: Retrieve the movies that have an actor’s role that is the name of the movie.
#### Comando
~~~~ javascript
MATCH (p:Person)-[r:ACTED_IN]->(m:Movie)
WHERE m.title in r.roles
RETURN  m.title as Movie, p.name as Actor
~~~~


## Execicio 5

* Exercise 5.1: Retrieve data using multiple MATCH patterns.
#### Comando
~~~~ javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)<-[:DIRECTED]-(diretor:Person),
      (p2:Person)-[:ACTED_IN]->(m)
WHERE p.name = 'Gene Hackman'
RETURN m.title as movie, diretor.name AS diretor , p2.name AS `outros atores`
~~~~
* Exercise 5.2: Retrieve particular nodes that have a relationship.
#### Comando
~~~~ javascript
MATCH (p1:Person)-[:FOLLOWS]-(p2:Person)
WHERE p1.name = 'Paul Blythe'
RETURN p1, p2
~~~~
* Exercise 5.3: Modify the query to retrieve nodes that are exactly three hops away.
#### Comando
~~~~ javascript
MATCH (p1:Person)-[:FOLLOWS*3]-(p2:Person)
WHERE p1.name = 'Paul Blythe'
RETURN p1, p2
~~~~
* Exercise 5.4: Modify the query to retrieve nodes that are one and two hops away.
#### Comando
~~~~ javascript
MATCH (p1:Person)-[:FOLLOWS*1..2]-(p2:Person)
WHERE p1.name = 'Paul Blythe'
RETURN p1, p2
~~~~
* Exercise 5.5: Modify the query to retrieve particular nodes that are connected no matter how many hops are required.
#### Comando
~~~~ javascript
MATCH (p1:Person)-[:FOLLOWS*]-(p2:Person)
WHERE p1.name = 'Paul Blythe'
RETURN p1, p2
~~~~
* Exercise 5.6: Specify optional data to be retrieved during the query.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 5.7: Retrieve nodes by collecting a list.
#### Comando
~~~~ javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
RETURN p.name as actor, collect(m.title) AS `movie list`
~~~~
* Exercise 5.9: Retrieve nodes as lists and return data associated with the corresponding lists.
#### Comando
~~~~ javascript
MATCH (p:Person)-[:REVIEWED]->(m:Movie)
RETURN m.title as filme, count(p) as numero_revisores, collect(p.name) as revisores
~~~~
* Exercise 5.10: Retrieve nodes and their relationships as lists.
#### Comando
~~~~ javascript
MATCH (d:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(a:Person)
RETURN d.name AS director, count(a) AS `number actors` , collect(a.name) AS `actors worked with`
~~~~
* Exercise 5.11: Retrieve the actors who have acted in exactly five movies.
#### Comando
~~~~ javascript
MATCH (dir:Person)-[:DIRECTED]->(m:Movie)<-[:ACTED_IN]-(ator:Person)
RETURN dir.name AS diretor, count(ator) AS `numero de atores` , collect(ator.name) AS `atores que  trabalharam`
~~~~
* Exercise 5.12: Retrieve the movies that have at least 2 directors with other optional data.
#### Comando
~~~javascript
MATCH (m:Movie)
WITH m, size((:Person)-[:DIRECTED]->(m)) AS directors
WHERE directors >= 2
OPTIONAL MATCH (p:Person)-[:REVIEWED]->(m)
RETURN  m.title, p.name
~~~ 


## Execicio 6

* Exercise 6.1: Execute a query that returns duplicate records.
#### Comando
~~~javascript
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)
RETURN DISTINCT m.released, m.title, collect(a.name)
~~~ 
* Exercise 6.2: Modify the query to eliminate duplication.
#### Comando
~~~javascript
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)
RETURN  m.released, collect(m.title), collect(a.name)
~~~ 

* Exercise 6.3: Modify the query to eliminate more duplication.
#### Comando
~~~javascript
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)
RETURN  m.released, collect(DISTINCT m.title), collect(a.name)
~~~ 

* Exercise 6.4: Sort results returned.
#### Comando
~~~javascript
MATCH (a:Person)-[:ACTED_IN]->(m:Movie)
RETURN  m.released, collect(DISTINCT m.title), collect(a.name)
ORDER BY m.released DESC
~~~ 

* Exercise 6.5: Retrieve the top 5 ratings and their associated movies.
#### Comando
~~~javascript
MATCH (:Person)-[r:REVIEWED]->(m:Movie)
RETURN  m.title AS filme, r.rating AS nota
ORDER BY r.rating DESC LIMIT 5
~~~ 

## Execicio 7

* Exercise 7.1: Collect and use lists.
#### Comando
~~~javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie),
      (m)<-[:PRODUCED]-(p2:Person)
WITH  m, collect(DISTINCT p.name) AS elenco, collect(DISTINCT p2.name) AS produtores
RETURN DISTINCT m.title as titulo, elenco, produtores
ORDER BY size(elenco)
~~~ 

* Exercise 7.2: Collect a list.
#### Comando
~~~javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WITH p, collect(m) AS filmes
WHERE size(filmes)  > 5
RETURN p.name, filmes
~~~ 

* Exercise 7.3: Unwind a list.
#### Comando
~~~javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WITH p, collect(m) AS filmes
WHERE size(filmes)  > 5
WITH p, filmes UNWIND filmes AS filme
RETURN p.name, filme.title
~~~ 

* Exercise 7.4: Perform a calculation with the date type.
#### Comando
~~~javascript
MATCH (p:Person)-[:ACTED_IN]->(m:Movie)
WHERE p.name = 'Tom Cruise'
RETURN  m.title, m.released, date().year  - m.released as anosDoLanc, m.released  - p.born AS `Idade de Tom Cruise`
ORDER BY anosDoLanc
~~~ 

## Execicio 8

* Exercise 8.1: Create a Movie node.
#### Comando
~~~javascript
CREATE (:Movie {title: 'Pulp Fiction'})
~~~ 

* Exercise 8.2: Retrieve the newly-created node.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN m
~~~ 

* Exercise 8.3: Create a Person node.
#### Comando
~~~javascript
CREATE (:Person {name: 'Quentin Tarantino'})
~~~ 

* Exercise 8.4: Retrieve the newly-created node.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name = 'Quentin Tarantino'
RETURN p
~~~ 

* Exercise 8.5: Add a label to a node.
#### Comando
~~~javascript
MATCH (m:Movie)
SET m:classificacao18
RETURN DISTINCT labels(m)
~~~ 

* Exercise 8.6: Retrieve the node using the new label.
#### Comando
~~~javascript
MATCH (m:clasificacao18)
RETURN m.title, m.released
~~~ 

* Exercise 8.7: Add the Female label to selected nodes.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name STARTS WITH 'Demi'
SET p:Female
~~~ 

* Exercise 8.8: Retrieve all Female nodes.

#### Comando
~~~javascript
MATCH (p:Female)
RETURN p.name
~~~ 

* Exercise 8.9: Remove the Female label from the nodes that have this label.
#### Comando
~~~javascript
MATCH (p:Female)
REMOVE p:Female
~~~ 

* Exercise 8.10: View the current schema of the graph.
#### Comando
~~~javascript
CALL db.schema.visualization
~~~ 

* Exercise 8.11: Add properties to a movie.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
SET m:classificacao18,
    m.released = 1994,
    m.tagline = "Tempo de violencia",
    m.lengthInMinutes = 154
~~~ 

* Exercise 8.12: Retrieve an OlderMovie node to confirm the label and properties.
#### Comando
~~~javascript
MATCH (m:OlderMovie)
RETURN m
~~~ 

* Exercise 8.13: Add properties to the person, Robin Wright.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name = 'Robin Wright'
SET p.born = 1966
~~~ 

* Exercise 8.14: Retrieve an updated Person node.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name = 'Quentin Tarantino'
RETURN p
~~~ 

* Exercise 8.15: Remove a property from a Movie node.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
SET m.tagline = null
~~~ 

* Exercise 8.16: Retrieve the node to confirm that the property has been removed.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN m
~~~ 

* Exercise 8.17: Remove a property from a Person node.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name = 'Quentin Tarantino'
REMOVE p.born
~~~ 

* Exercise 8.18: Retrieve the node to confirm that the property has been removed.
#### Comando
~~~javascript
MATCH (p:Person)
WHERE p.name = 'Quentin Tarantino'
RETURN p
~~~ 


##Exercicio 9

* Exercise 9.1: Create ACTED_IN relationships.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
MATCH (p:Person)
WHERE p.name = 'John Travolta' OR p.name = 'Samuel L. Jackson' OR p.name = 'Uma Thurman'
CREATE (p)-[:ACTED_IN]->(m)
~~~ 

* Exercise 9.2: Create DIRECTED relationships.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
MATCH (p:Person)
WHERE p.name = 'Quentin Tarantino'
CREATE (p)-[:DIRECTED]->(m)
~~~ 


* Exercise 9.3: Create a HELPED relationship.
#### Comando
~~~javascript
MATCH (p1:Person)
WHERE p1.name = 'Charles Collum'
MATCH (p2:Person)
WHERE p2.name = 'Quentin Tarantino'
CREATE (p1)-[:HELPED]->(p2)
~~~ 

* Exercise 9.4: Query nodes and new relationships.
#### Comando
~~~javascript
MATCH (p:Person)-[rel]-(m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN p, rel, m
~~~ 

* Exercise 9.5: Add properties to relationships.
#### Comando
~~~javascript
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Pulp Fiction'
SET rel.roles =
CASE p.name
  WHEN 'John Travolta' THEN ['Grease']
  WHEN 'Samuel L. Jackson' THEN ['Avengers']
  WHEN 'Uma Thurman' THEN ['Kill Bill']
END
~~~ 

* Exercise 9.6: Add a property to the HELPED relationship.
#### Comando
~~~javascript
MATCH (p1:Person)-[rel:HELPED]->(p2:Person)
WHERE p1.name = 'Charles Collum' AND p2.name = 'Quentin Tarantino'
SET rel.research = 'direção de arte'
~~~ 

* Exercise 9.7: View the current list of property keys in the graph.
#### Comando
~~~javascript
call db.propertyKeys
~~~ 

* Exercise 9.8: View the current schema of the graph.
#### Comando
~~~javascript
call db.schema.visualization
~~~ 

* Exercise 9.9: Retrieve the names and roles for actors.
#### Comando
~~~javascript
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN p.name, rel.roles
~~~ 

* Exercise 9.10: Retrieve information about any specific relationships.
#### Comando
~~~javascript
MATCH (p1:Person)-[rel:HELPED]-(p2:Person)
RETURN p1.name, rel, p2.name
~~~ 

* Exercise 9.11: Modify a property of a relationship.
#### Comando
~~~javascript
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Pulp Fiction' AND p.name = 'John Travolta'
SET rel.roles =['Vicent Vega']
~~~ 

* Exercise 9.12: Remove a property from a relationship.
#### Comando
~~~javascript
MATCH (p1:Person)-[rel:HELPED]->(p2:Person)
WHERE p2.name = 'Quentin Tarantino' AND p1.name = 'Charles Collum'
REMOVE rel.research
~~~ 

* Exercise 9.13: Confirm that your modifications were made to the graph.
#### Comando
~~~javascript
MATCH (p:Person)-[rel:ACTED_IN]->(m:Movie)
WHERE m.title = 'Pulp Fiction'
return p, rel, m
~~~ 


##Exercicio 10

* Exercise 10.1: Delete a relationship.
#### Comando
~~~javascript
MATCH (:Person)-[rel:HELPED]-(:Person)
DELETE rel
~~~ 

* Exercise 10.2: Confirm that the relationship has been deleted.
#### Comando
~~~javascript
MATCH (:Person)-[rel:HELPED]-(:Person)
RETURN rel
~~~ 

* Exercise 10.3: Retrieve a movie and all of its relationships.
#### Comando
~~~javascript
MATCH (p:Person)-[rel]-(m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN p, rel, m
~~~ 

* Exercise 10.4: Try deleting a node without detaching its relationships.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Forrest Gump'
DELETE m
~~~ 

* Exercise 10.5: Delete a Movie node, along with its relationships.
#### Comando
~~~javascript
MATCH (m:Movie)
WHERE m.title = 'Pulp Fiction'
DETACH DELETE m
~~~ 

* Exercise 10.6: Confirm that the Movie node has been deleted.
#### Comando
~~~javascript
MATCH (p:Person)-[rel]-(m:Movie)
WHERE m.title = 'Pulp Fiction'
RETURN p, rel, m
~~~ 




