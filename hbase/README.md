# Exercicios HBASE

## Execicio 1

* Dentro da imagem faça os seguintes procedimentos:
	1. Crie a tabela com 2 famílias de colunas:
		a. personal-data
		b. professional-data
		
	#### Comando
	~~~shell
	Took 0.0034 seconds
	hbase(main):001:0> create 'italians', 'personal-data', 'professional-data'
	Created table italians
	Took 1.1883 seconds
	=> Hbase::Table - italians
	hbase(main):002:0>
	~~~	
	2. Importe o arquivo via linha de comando

	#### Resultado
	~~~shell
		hbase(main):081:0> put 'italians', '9', 'professional-data:role',  'Marketing'
		talians', '9', 'Took 0.0043 seconds

		hbase(main):082:0> put 'italians', '9', 'professional-data:salary',  '9919'
		Took 0.0038 seconds
		', '10', 'personal-data:name',  hbase(main):083:0> put 'italians', '10', 'personal-data:name',  'Giovanna Caputo'
		Took 0.0024 seconds
		, '10', 'personahbase(main):084:0> put 'italians', '10', 'personal-data:city',  'Milan'
		ians', '10', 'prTook 0.0047 seconds

		hbase(main):085:0> put 'italians', '10', 'professional-data:role',  'Comunicacao Institucional'
		Took 0.0032 seconds
		s', '10', 'profehbase(main):086:0> put 'italians', '10', 'professional-data:salary',  '9470'
		Took 0.0033 seconds
	~~~

* Agora execute as seguintes operações:
	1. Adicione mais 2 italianos mantendo adicionando informações como data de nascimento nas informações pessoais e um atributo de anos de
	experiência nas informações profissionais;  
	
	#### Comando
	~~~shell
		put 'italians', '11', 'personal-data:name',  'Luigi Bongiorno'
		put 'italians', '11', 'personal-data:city',  'Veneza'
		put 'italians', '11', 'personal-data:data-nascimento',  '28/03/1958'
		put 'italians', '11', 'professional-data:role',  'Comunicacao Institucional'
		put 'italians', '11', 'professional-data:salary',  '9470'
		put 'italians', '11', 'professional-data:anos-experiencia',  '41'

		put 'italians', '12', 'personal-data:name',  'Robert De Niro'
		put 'italians', '12', 'personal-data:city',  'Genova'
		put 'italians', '12', 'personal-data:data-nascimento',  '17/08/1953'
		put 'italians', '12', 'professional-data:role',  'Produtor'
		put 'italians', '12', 'professional-data:salary',  '12345'
		put 'italians', '12', 'professional-data:anos-experiencia',  '43'
	~~~
	
	2. Adicione o controle de 5 versões na tabela de dados pessoais.
	
	#### Comando
	~~~shell
		alter ‘italians′, NAME => ‘personal-data′, VERSIONS => 5		
	~~~
	#### resultado
	~~~shell
		hbase(main):104:0*                                                            
		hbase(main):105:0* alter 'italians' , NAME=>'personal-data', VERSIONS=>5      
		Updating all regions with the new schema...                                   
		1/1 regions updated.                                                          
		Done.                                                                         
		Took 2.0528 seconds                                                           		
		hbase(main):106:0>                                                            
	~~~
	
	3. Faça 5 alterações em um dos italianos;
	
	#### Comando
	~~~shell
		put 'italians', '11', 'personal-data:name',  'Luigi Bongiorno Agostini'
		put 'italians', '11', 'personal-data:city',  'Florenca'
		put 'italians', '11', 'personal-data:data-nascimento',  '27/03/1958'
		put 'italians', '11', 'professional-data:role',  'Comunicacao Audiovisual'
		put 'italians', '11', 'professional-data:salary',  '12457'
		put 'italians', '11', 'professional-data:anos-experiencia',  '42'

	~~~

	4. Com o operador get, verifique como o HBase armazenou o histórico.
		
	#### Comando
	~~~shell
		get 'italians', '11', {COLUMN => 'personal-data:name', VERSIONS => 2}
	~~~
	#### resultado
	~~~shell
		Took 0.0058 seconds                                                                                                                                                     
		hbase(main):001:0> get 'italians', '11', {COLUMN => 'personal-data:name', VERSIONS => 2}                                                                                
		COLUMN                                                       CELL                                                                                                       
		 personal-data:name                                          timestamp=1588341532036, value=Luigi Bongiorno Agostini                                                    
		 personal-data:name                                          timestamp=1588340781344, value=Luigi Bongiorno                                                             
		1 row(s)                                                                                                                                                                
		Took 0.5066 seconds                                                                                                                                                     
		hbase(main):002:0>   
	~~~
	
	5. Utilize o scan para mostrar apenas o nome e profissão dos italianos.
		
	#### Comando
	~~~shell
		scan 'italians', {COLUMN => 'personal-data:name', COLUMN => 'professional-data:role'}
	~~~
	#### resultado
	~~~shell
		hbase(main):005:0> scan 'italians', {COLUMN => 'personal-data:name', COLUMN => 'professional-data:role'}                                                          
		ROW                                                          COLUMN+CELL                                                                                          
		 1                                                           column=professional-data:role, timestamp=1588340065249, value=Gestao Comercial                       
		 10                                                          column=professional-data:role, timestamp=1588340066732, value=Comunicacao Institucional              
		 11                                                          column=professional-data:role, timestamp=1588341532164, value=Comunicacao Audiovisual                
		 12                                                          column=professional-data:role, timestamp=1588340969040, value=Produtor                               
		 2                                                           column=professional-data:role, timestamp=1588340065424, value=Psicopedagogia                         
		 3                                                           column=professional-data:role, timestamp=1588340065574, value=Optometria                             
		 4                                                           column=professional-data:role, timestamp=1588340065743, value=Engenharia Industrial Madeireira       
		 5                                                           column=professional-data:role, timestamp=1588340065901, value=Mecatronica Industrial                 
		 6                                                           column=professional-data:role, timestamp=1588340066078, value=Biotecnologia e Bioquimica             
		 7                                                           column=professional-data:role, timestamp=1588340066275, value=Libras                                 
		 8                                                           column=professional-data:role, timestamp=1588340066402, value=Engenharia de Minas                    
		 9                                                           column=professional-data:role, timestamp=1588340066559, value=Marketing                              
		12 row(s)                                                                                                                                                         
		Took 0.0707 seconds                                                                                                                                               
		hbase(main):006:0>  		
	~~~
	
	6. Apague os italianos com row id ímpar
		
	#### Comando
	~~~shell
		deleteall 'italians', '1'
		deleteall 'italians', '3'
		deleteall 'italians', '5'
		deleteall 'italians', '7'
		deleteall 'italians', '9'
		deleteall 'italians', '11'
	~~~
	
	7. Crie um contador de idade 55 para o italiano de row id 5
		
	#### Comando
	~~~shell
		put 'italians', '5', 'personal-data:contador' , 55
	~~~
	#### resultado
	~~~shell
		Took 0.0027 seconds
		hbase(main):017:0> put 'italians', '5', 'personal-data:contador' , 55
		Took 0.0243 seconds
		hbase(main):018:0>
	~~~
	
	8. Incremente a idade do italiano em 1
		
	#### Comando
	~~~shell
		incr 'italians', '5', 'personal-data:contador' 
	~~~

	