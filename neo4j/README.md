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
AQUI
~~~~

* Exercise 4.2: Retrieve all people that were born in the 70’s.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.3: Retrieve the actors who acted in the movie The Matrix
who were born after 1960.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.4: Retrieve all movies by testing the node label and a
property.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.5: Retrieve all people that wrote movies by testing the
relationship between two nodes.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.6: Retrieve all people in the graph that do not have a
property.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.7: Retrieve all people related to movies where the
relationship has a property.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.8: Retrieve all actors whose name begins with James.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.9: Retrieve all all REVIEW relationships from the graph
with filtered results.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.10: Retrieve all people who have produced a movie, but
have not directed a movie.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.11: Retrieve the movies and their actors where one of the
actors also directed the movie.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.12: Retrieve all movies that were released in a set of
years.
#### Comando
~~~~ javascript
AQUI
~~~~
* Exercise 4.13: Retrieve the movies that have an actor’s role that is
the name of the movie.
#### Comando
~~~~ javascript
AQUI
~~~~
