OPE2 - BACKEND
====================
Getting Start
--------
Install Docker in your Machine
^^^^^^^^^^^^^^^^^^^^^
* WINDOWS SEE DOCUMENTATION:
    $ https://www.docker.com/products/docker-desktop

* LINUX SEE DOCUMENTATION:
    $ https://docs.docker.com/engine/install/ubuntu/

Build Docker Aplication
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml build

Start Docker Aplication
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml build

building a aplicação
~~~~~~~~~~~~~~~~~~~~

::

    docker-compose -f local.yml build

iniciando a aplicação
~~~~~~~~~~~~~~~~~~~~~

::

    docker-compose -f local.yml up

ps.: sempre que a aplicação for iniciada todas as migrations pendentes
serão executadas automaticamente.


Reset Postgres
~~~~~~~~~~~~~~~~~~~~~

::

    docker-compose -f local.yml down

ps.: Antes de resetar e deletar as imagens do postgres, necessário usar esse comando
para parar as aplicações em execução.

::

    docker rm postgres



::

    docker volume rm leitor_local_postgres_data



::

    docker volume rm leitor_local_postgres_data_backups

Deletar migrations(Caso necessário)
~~~~~~~~~~~~~~~~~~~~~

Em ~/leitor/leitor, utilizar os seguintes comandos.

::

    find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/sites/*" -delete


::

    find . -path "*/migrations/*.pyc"  -delete


Orientações
~~~~~~~~~~~

Acesse localhost:8000 ou  Acesse localhost:8000/admin

Caso tenha rodado o populate_db_

Usuario/Email: admin

Senha: admin@102030@@


Ex.: Criar uma nova migração
^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Aplicação em funcionamento:

::

    docker-compose -f local.yml exec django python manage.py makemigrations

ps: O comando exec não funciona ver issue8_

.. _issue8: https://github.com/Clint-Tecnologia/leitor/issues/8

Aplicação desligada:

::

    docker-compose -f local.yml run --rm django python manage.py makemigrations

Trabalhando no projeto
~~~~~~~~~~~~~~~~~~~~~~

Criar as migrações no container já existente

::

    docker-compose -f local.yml run --rm django python manage.py makemigrations

Rodar as migrações na base de dados

::

    docker-compose -f local.yml run --rm django python manage.py migrate

.. _populate_db:

Rodar o script de população de fixtures

::

    docker-compose -f local.yml run --rm django python manage.py populate_db

Gerar fixtures do projeto

::

    docker-compose -f local.yml run --rm django python manage.py dumpdata nome_app.nome_model --indent 4 > nome_app/fixtures/numero_nome_model.json

Gerar fixtures, exemplo: gerando a 1a fixture que cria o superuser admin

::

    docker-compose -f local.yml run --rm django python manage.py createsuperuser
    docker-compose -f local.yml run --rm django python manage.py dumpdata users --indent 4 > leitor/users/fixtures/01_user.json

Reiniciar um container para aplicar as alterações

::

    docker-compose restart nome_container

Debugando o projeto
~~~~~~~~~~~~~~~~~~~

Para acessar o console da máquina dentro do container que está rodando a
aplicação (app):

::

    docker exec -it web bash

Para acesso o django shell dentro do container que está rodando a
aplicação:

::

    docker-compose -f local.yml run --rm django python manage.py shell_plus

Para acesso o django shell (mostrando as queries em sql):

::

    docker-compose -f local.yml run --rm django python manage.py shell_plus --print-sql

Para acessar o container que está rodando o Banco de Dados (PG):

::

    docker exec -it postgis bash

Para gerar o MER (modelo de entidade e relacionamento):

::

    docker-compose -f local.yml run --rm django python manage.py graph_models -a -g -o mer.png

Principais comandos do Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Listar as imagens do host:

::

    $ docker images

Listar os containers do host:

::

    $ docker ps -a

Listar os volumes do host:

::

    $ docker volume ls

Remover imagens que não são usadas:

::

    $ docker rmi (id ou nome da imagem)

Remover containers que não são usados:

::

    $ docker rm (id ou nome da imagem)

Remover volumes que não são usados:

::

    $ docker volume rm (id ou nome da imagem)

Remover todos os containers e imagens de uma só vez:

::

    $ docker rm -f $(docker ps -qa)

Remover todos os volumes de uma só vez:

::

    $ docker volume prune -f

Remover todas as imagens:

::

    $ docker rmi -f $(docker images -q)


Git Workflow
~~~~~~~~~~~~

Sempre que iniciar uma feature o desenvolvedor precisa inicar uma nova branch.

Sempre que finalizar, caso não tenha os file watchers para black, flake8 e iSort é recomendavel rodar o commando abaixo


::

    pre-commit run --all-files

Quando todas as etapas tiverem 'Passed' fazer o push e gerar um PR.

Os PRs podem ser mergeados ou rebased e sempre devemos remover a branch no Github.



Versão Demo
~~~~~~~~~~~~

Deve-se criar um grupo de usuários chamado Demo e inserir nele os usuários de demonstração
O número limite de tentativas de leituras é configurado ná variável MAX_ATTEMPTS do config/settings/base.py
