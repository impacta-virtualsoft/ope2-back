ope2-back
====================

Install Docker in your Machine
^^^^^^^^^^^^^^^^^^^^^
* WINDOWS SEE DOCUMENTATION:
    https://www.docker.com/products/docker-desktop

* LINUX SEE DOCUMENTATION:
    https://docs.docker.com/engine/install/ubuntu/


Build and Start Application
^^^^^^^^^^^^^^^^^^^^^
Build Docker Application
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml build

Start Docker Application
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml up

* Whenever the application starts all pending migrations will run automatically.

Stop Docker Application
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml down


Populate Fixtures
~~~~~~~~~~~~~~~~~~~~
You need to Stop Docker Application !

    $ docker-compose -f local.yml run --rm django python manage.py populate_db

* Populate Fixtures to insertion of entries in the database.

Reset Database(Postgres)
^^^^^^^^^^^^^^^^^^^^^
1 - Stop Application
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml down
2 - Remove Postgres Container
~~~~~~~~~~~~~~~~~~~~
    $ docker rm backend_postgres
3 - Remove Backups Volume Postgres
~~~~~~~~~~~~~~~~~~~~
    $ docker volume rm ope2-back_local_postgres_data_backups
4 - Remove Data Volume Postgres
~~~~~~~~~~~~~~~~~~~~
    $ docker volume rm ope2-back_local_postgres_data


Work in Project
^^^^^^^^^^^^^^^^^^^^^

Super User Pattern
~~~~~~~~~~~~~~~~~~~~
If you populate fixtures, acess http://localhost:8000/admin or http://0.0.0.0:8000/admin

Usuario: admin

Senha: admin@admin

If you want to create a super user run:

    $ docker-compose -f local.yml run --rm django python manage.py createsuperuser

Create New Migrations
~~~~~~~~~~~~~~~~~~~~
You nedd to stop the application.

    $ docker-compose -f local.yml run --rm django python manage.py makemigrations

Apply Migrations
~~~~~~~~~~~~~~~~~~~~
You nedd to stop the application.

    $ docker-compose -f local.yml run --rm django python manage.py migrate

Delete all migrations
~~~~~~~~~~~~~~~~~~~~
You nedd to stop the application.

    $ find . -path "*/migrations/*.py" -not -name "__init__.py" -not -path "*/sites/*" -delete
    $ find . -path "*/migrations/*.pyc"  -delete

Generate Project Fixtures
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml run --rm django python manage.py dumpdata APP --indent 4 > ./backend/APP/fixtures/NUMBER_MODEL.json

Docker Useful Commands
^^^^^^^^^^^^^^^^^^^^^
List host images:
~~~~~~~~~~~~
    $ docker images

List host containers:
~~~~~~~~~~~~
    $ docker ps -a

List host volumes:
~~~~~~~~~~~~
    $ docker volume ls

Remove images that are not used:
~~~~~~~~~~~~
    $ docker rmi (id ou nome da imagem)

Remove unused containers:
~~~~~~~~~~~~
    $ docker rm (id ou nome da imagem)

Remove unused volumes:
~~~~~~~~~~~~
    $ docker volume rm (id ou nome da imagem)

Remove all containers and images at once:
~~~~~~~~~~~~
    $ docker rm -f $(docker ps -qa)

Remove all volumes at once:
~~~~~~~~~~~~
    $ docker volume prune -f

Remove all images:
~~~~~~~~~~~~
    $ docker rmi -f $(docker images -q)



Git Workflow
^^^^^^^^^^^^^^^^^^^^^

Whenever starting a feature the developer needs to start a new branch.

Whenever you finish, if you don't have the file watchers for black, flake8 and iSort, it is recommended to run the command below:

    $ pre-commit run --all-files

When all steps are 'Passed' push and generate a PR.

PRs can be merged or rebased and we should always remove the branch in Github.
