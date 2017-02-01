# django-fatec
Projeto exemplo para curso de **Django**


#### Se alguém tiver alguma problema em relação ao banco de dados, apague o arquivo *db.sqlite3* de dentro do projeto e execute novamente os comandos:

`python manage.py makemigrations`

`python manage.py migrate`

#### Para criar um novo usuário no seu banco de dados (já migrado pelos comandos acima) execute o comando:

`python manage.py createsuperuser`

Isso iniciará o processo de criação do usuário, baste digitar as informações pedidas e concluir o cadastro.

#### Para iniciar o servidor do **Django** digite o comando a seguir, de dentro do diretório do projeto:

`python manage.py runserver`
