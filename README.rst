leitor
====================



Git Workflow
~~~~~~~~~~~~

Sempre que iniciar uma feature o desenvolvedor precisa inicar uma nova branch.

Sempre que finalizar, caso não tenha os file watchers para black, flake8 e iSort é recomendavel rodar o commando abaixo


::

    pre-commit run --all-files

Quando todas as etapas tiverem 'Passed' fazer o push e gerar um PR.

Os PRs podem ser mergeados ou rebased e sempre devemos remover a branch no Github.
