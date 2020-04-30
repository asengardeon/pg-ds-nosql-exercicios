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

 ## Execicio 2
 
 
1. Liste/Conte todas as pessoas que tem exatamente 99 anos. Você pode
usar um count para indicar a quantidade.

#### Comando
~~~~ javascript
 db.getCollection('italians').find({age: 99.}).count()
~~~~

#### Resultado
~~~json
0
~~~

2. Identifique quantas pessoas são elegíveis atendimento prioritário
(pessoas com mais de 65 anos)
#### Comando
~~~~ javascript
 db.getCollection('italians').find({age: {$gte: 65.0}}).count()
~~~~

#### Resultado
~~~json
1824
~~~
3. Identifique todos os jovens (pessoas entre 12 a 18 anos).
#### Comando
~~~~ javascript
 db.getCollection('italians').find({age: {$gte: 12.0}, age: {$lte: 18.0}}).count()
~~~~

#### Resultado
~~~json
2398
~~~
4. Identifique quantas pessoas tem gatos, quantas tem cachorro e quantas
não tem nenhum dos dois
#### Comando
~~~~ javascript
 db.getCollection('italians').find({"cat": {"$exists": 1}}).count()
db.getCollection('italians').find({"dog": {"$exists": 1}}).count()
db.getCollection('italians').find({"cat": {"$exists": 0}, "dog": {"$exists": 0}}).count()
~~~~

#### Resultado
~~~json
5996
3981
2428
~~~

5. Liste/Conte todas as pessoas acima de 60 anos que tenham gato
#### Comando
~~~~ javascript
 db.getCollection('italians').find({"cat": {"$exists": 1}, age: {$gt: 60.0}}).count()
~~~~

#### Resultado
~~~json
1400
~~~

6. Liste/Conte todos os jovens com cachorro
#### Comando
~~~~ javascript
  db.getCollection('italians').find({age: {$gte: 12.0}, age: {$lte: 18.0}, "dog": {"$exists": 1}}).count()
~~~~

#### Resultado
~~~json
928
~~~
7. Utilizando o $where, liste todas as pessoas que tem gato e cachorro
#### Comando
~~~~ javascript
 db.getCollection('italians').find(
{ $where: function() {
   return this.dog != null
} } 
).count()
~~~~

#### Resultado
~~~json
3981
~~~

8. Liste todas as pessoas mais novas que seus respectivos gatos.
#### Comando
~~~~ javascript
 db.getCollection('italians').find(
{ $where: function() {
   return this.cat != null && this.cat.age > this.age
} } 
).count()
~~~~

#### Resultado
~~~json
580
~~~
9. Liste as pessoas que tem o mesmo nome que seu bichano (gatou ou
cachorro)
#### Comando
~~~~ javascript
 db.getCollection('italians').find(
{ $where: function() {
   return (this.dog != null && this.dog.name == this.firstname) || (this.cat != null && this.cat.name == this.firstname)
} } 
)
~~~~

#### Resultado
~~~json
93
~~~
10. Projete apenas o nome e sobrenome das pessoas com tipo de sangue de
fator RH negativo
#### Comando
~~~~ javascript
db.getCollection('italians').find({"bloodType" : {"$in": ["A-", "B-", "O-", "AB-"]}}, {"firstname": 1, "surname": 1}).count()~~~~

#### Resultado
~~~json
5045
~~~
11. Projete apenas os animais dos italianos. Devem ser listados os animais
com nome e idade. Não mostre o identificado do mongo (ObjectId)
#### Comando
~~~~ javascript
 db.getCollection('italians').find({"$or": [{"cat": {"$exists": 1}}, {"dog": {"$exists": 1}}]}, {_id: 0, "dog.name": 1, "cat.name": 1})
~~~~

#### Resultado
~~~json
7572
~~~
12. Quais são as 5 pessoas mais velhas com sobrenome Rossi?
#### Comando
~~~~ javascript
 db.getCollection('italians').find({surname: "Rossi"}).sort({age: -1}).limit(5)
~~~~

#### Resultado
~~~json
5
~~~
13. Crie um italiano que tenha um leão como animal de estimação. Associe
um nome e idade ao bichano
#### Comando
~~~~ javascript
 db.getCollection('italians').insert(

{
    "firstname" : "Giusepe",
    "surname" : "Bongiorno",
    "username" : "user999999",
    "age" : 79.0,
    "email" : "giuorno@aol.com",
    "bloodType" : "A+",
    "id_num" : "66879999",
    "registerDate" : ISODate("1978-05-14T10:49:04.870Z"),
    "ticketNumber" : 8464.0,
    "jobs" : [ 
        "Educomunicação", 
        "Oftálmica"
    ],
    "favFruits" : [ 
        "Banana"
    ],
    "movies" : [ 
        {
            "title" : "A Felicidade Não se Compra (1946)",
            "rating" : 4.55
        }, 
        {
            "title" : "Interestelar (2014)",
            "rating" : 3.06
        }, 
        {
            "title" : "A Lista de Schindler (1993)",
            "rating" : 0.43
        }
    ],
    "lion" : {
        "name" : "Kitty",
        "age" : 13.0
    }
}
)
~~~~

#### Resultado
~~~json
Inserted 1 record(s) in 2ms

~~~
14. Infelizmente o Leão comeu o italiano. Remova essa pessoa usando o Id.
#### Comando
~~~~ javascript
 var id = db.getCollection('italians').findOne({username: "user999999"}, {id: 1})
db.getCollection('italians').remove(id)
~~~~

#### Resultado
~~~json
Removed 1 record(s) in 1ms
~~~
15. Passou um ano. Atualize a idade de todos os italianos e dos bichanos em
1.
#### Comando
~~~~ javascript
 AQUI
~~~~

#### Resultado
~~~json
AQUI
~~~
16. O Corona Vírus chegou na Itália e misteriosamente atingiu pessoas
somente com gatos e de 66 anos. Remova esses italianos.
#### Comando
~~~~ javascript
db.getCollection('italians').remove({"cat": {"$exists": 1}, "age": 66})
~~~~

#### Resultado
~~~json
AQUI
~~~
17. Utilizando o framework agregate, liste apenas as pessoas com nomes
iguais a sua respectiva mãe e que tenha gato ou cachorro.
#### Comando
~~~~ javascript
 AQUI
~~~~

#### Resultado
~~~json
AQUI
~~~
18. Utilizando aggregate framework, faça uma lista de nomes única de
nomes. Faça isso usando apenas o primeiro nome
#### Comando
~~~~ javascript
 AQUI
~~~~

#### Resultado
~~~json
AQUI
~~~
19. Agora faça a mesma lista do item acima, considerando nome completo.
#### Comando
~~~~ javascript
 AQUI
~~~~

#### Resultado
~~~json
AQUI
~~~
20. Procure pessoas que gosta de Banana ou Maçã, tenham cachorro ou gato,
mais de 20 e menos de 60 anos.
#### Comando
~~~~ javascript
 db.italians.find({ favFruits: { $elemMatch: {$in:["Banana", "Maçã"]}}, "$or": [{"cat": {"$exists": 1}}, {"dog": {"$exists": 1}}], "age": {"$gte": 20}, "age": {"$lte": 60}})
~~~~

#### Resultado
~~~json
2061
~~~