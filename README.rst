OPE2 - BACKEND
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

Start Docker Aplication
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml up

* Whenever the application starts all pending migrations will run automatically.

Populate Fixtures
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml run --rm django python manage.py populate_db

* Populate Fixtures to insertion of entriens in the database.

Stop Docker Aplication
~~~~~~~~~~~~~~~~~~~~
    $ docker-compose -f local.yml down


Work in Project
^^^^^^^^^^^^^^^^^^^^^
Reset Database
^^^^^^^^^^^^^^^^^^^^^
 Docker Useful Commands
^^^^^^^^^^^^^^^^^^^^^
List host images:

    $ docker images

List host containers:

    $ docker ps -a

List host volumes:

    $ docker volume ls

Remove images that are not used:

    $ docker rmi (id ou nome da imagem)

Remove unused containers:

    $ docker rm (id ou nome da imagem)

Remove unused volumes:

    $ docker volume rm (id ou nome da imagem)

Remove all containers and images at once:

    $ docker rm -f $(docker ps -qa)

Remove all volumes at once:

    $ docker volume prune -f

Remove all images:

    $ docker rmi -f $(docker images -q)


Git Workflow
~~~~~~~~~~~~

Whenever starting a feature the developer needs to start a new branch.

Whenever you finish, if you don't have the file watchers for black, flake8 and iSort, it is recommended to run the command below:

    $ pre-commit run --all-files

When all steps are 'Passed' push and generate a PR.

PRs can be merged or rebased and we should always remove the branch in Github.


Git Workflow
~~~~~~~~~~~~

Sempre que iniciar uma feature o desenvolvedor precisa inicar uma nova branch.

Sempre que finalizar, caso não tenha os file watchers para black, flake8 e iSort é recomendavel rodar o commando abaixo


::

    pre-commit run --all-files

Quando todas as etapas tiverem 'Passed' fazer o push e gerar um PR.

Os PRs podem ser mergeados ou rebased e sempre devemos remover a branch no Github.
