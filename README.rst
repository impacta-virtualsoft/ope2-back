leitor
====================


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
