# Exercicios MongoDB

 ## Execicio 1

1.1  Adicione outro Peixe e um Hamster com nome Frodo

#### Comando
~~~~ javascript
db.pets.insertMany([{name: "Frodo", species: "Hamster"}, {name: "Nemo", species: "Peixe"}])
~~~~

#### Resultado
~~~json
{
    "acknowledged" : true,
    "insertedIds" : [ 
        ObjectId("5eaabff0294ec351098c9e67"), 
        ObjectId("5eaabff0294ec351098c9e68")
    ]
}
~~~

1.2 Faça uma contagem dos pets na coleção

#### Comando
~~~~ javascript
db.pets.count()
~~~~

#### Resultado
```
8
```

1.3 Retorne apenas um elemento o método prático possível
~~~~ javascript
db.pets.findOne({})
~~~~

#### Resultado
~~~json
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e61"),
    "name" : "Mike",
    "species" : "Hamster"
}
~~~

1.4 Identifique o ID para o Gato Kilha.
~~~~ javascript
db.pets.findOne({name: "Kilha"}, {"_id": 1})
~~~~

#### Resultado
~~~json
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e63")
}
~~~

1.5 Faça uma busca pelo ID e traga o Hamster Mike
#### Comando
~~~~ javascript
var id = db.pets.findOne({"name": "Mike", "species": "Hamster"}, {_id: 1})
db.pets.findOne(id)
~~~~

#### Resultado
~~~json

    {
		"_id" : ObjectId("5eaabf3d294ec351098c9e61"),
		"name" : "Mike",
		"species" : "Hamster"
	}

~~~

1.6 Use o find para trazer todos os Hamsters
#### Comando
~~~~ javascript
db.pets.find({"species": "Hamster"})

~~~~

#### Resultado
~~~json
/* 1 */
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e61"),
    "name" : "Mike",
    "species" : "Hamster"
}

/* 2 */
{
    "_id" : ObjectId("5eaabff0294ec351098c9e67"),
    "name" : "Frodo",
    "species" : "Hamster"
}
~~~

1.7 Use o find para listar todos os pets com nome Mike
#### Comando
~~~~ javascript
db.pets.find({"name": "Mike"})
~~~~

#### Resultado
~~~json
/* 1 */
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e61"),
    "name" : "Mike",
    "species" : "Hamster"
}

/* 2 */
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e64"),
    "name" : "Mike",
    "species" : "Cachorro"
}
~~~

1.8 Liste apenas o documento que é um Cachorro chamado Mike
#### Comando
~~~~ javascript
db.pets.find({"name": "Mike", "species" : "Cachorro"})
~~~~

#### Resultado
~~~json
/* 1 */
{
    "_id" : ObjectId("5eaabf3d294ec351098c9e64"),
    "name" : "Mike",
    "species" : "Cachorro"
}
~~~
