OPE2
====================

Campanhas TradeMkt

.. image:: https://img.shields.io/badge/built%20with-Cookiecutter%20Django-ff69b4.svg?logo=cookiecutter
     :target: https://github.com/pydanny/cookiecutter-django/
     :alt: Built with Cookiecutter Django
.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
     :target: https://github.com/ambv/black
     :alt: Black code style


Settings
--------

Moved to settings_.

.. _settings: http://cookiecutter-django.readthedocs.io/en/latest/settings.html

Basic Commands
--------------

Setting Up Your Users
^^^^^^^^^^^^^^^^^^^^^

* To create a **normal user account**, just go to Sign Up and fill out the form. Once you submit it, you'll see a "Verify Your E-mail Address" page. Go to your console to see a simulated email verification message. Copy the link into your browser. Now the user's email should be verified and ready to go.

* To create an **superuser account**, use this command::

    $ python manage.py createsuperuser

For convenience, you can keep your normal user logged in on Chrome and your superuser logged in on Firefox (or similar), so that you can see how the site behaves for both kinds of users.

Type checks
^^^^^^^^^^^

Running type checks with mypy:

::

  $ mypy leitor

Test coverage
^^^^^^^^^^^^^

To run the tests, check your test coverage, and generate an HTML coverage report::

    $ coverage run -m pytest
    $ coverage html
    $ open htmlcov/index.html

Running tests with py.test
~~~~~~~~~~~~~~~~~~~~~~~~~~

::

  $ pytest

Live reloading and Sass CSS compilation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Moved to `Live reloading and SASS compilation`_.

.. _`Live reloading and SASS compilation`: http://cookiecutter-django.readthedocs.io/en/latest/live-reloading-and-sass-compilation.html





Sentry
^^^^^^

Sentry is an error logging aggregator service. You can sign up for a free account at  https://sentry.io/signup/?code=cookiecutter  or download and host it yourself.
The system is setup with reasonable defaults, including 404 logging and integration with the WSGI application.

You must set the DSN url in production.


Deployment
----------

The following details how to deploy this application.



Docker
^^^^^^

See detailed `cookiecutter-django Docker documentation`_.

.. _`cookiecutter-django Docker documentation`: http://cookiecutter-django.readthedocs.io/en/latest/deployment-with-docker.html

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
