# python
import os

from django.core import management
from django.core.management.base import BaseCommand
from django.utils import timezone


class Command(BaseCommand):
    help = "Show all available styles"

    def add_arguments(self, parser):
        parser.add_argument(
            "--app_name",
            "--app_name",
            type=str,
            help="Indicates the app name to create specific fixture",
        )

    def handle(self, *args, **kwargs):

        inicio = timezone.localtime(timezone.now()).strftime("%X")

        self.stdout.write(self.style.ERROR("\n\n\n| VirtualSoft Rocks!"))
        self.stdout.write(self.style.ERROR("\n| @virtualsoft"))

        self.stdout.write("\n\n- - - - -")
        self.stdout.write(
            self.style.NOTICE(
                "\nimportacao das fixtures do projeto | inicio: %s" % inicio
            )
        )

        app_name = kwargs["app_name"] if "app_name" in kwargs else None

        # users
        if app_name is None or app_name == "users":
            self.stdout.write(self.style.HTTP_NOT_MODIFIED("\nprocesssando app: users"))

            diretorio_fixtures = "backend/users/fixtures/"
            fixtures = sorted(os.listdir(diretorio_fixtures))

            for fixture in fixtures:
                if fixture != "data.json":
                    self.stdout.write(self.style.SQL_KEYWORD("\nmodel: " + fixture))
                    management.call_command("loaddata", diretorio_fixtures + fixture)

            self.stdout.write(self.style.SUCCESS("\nimportado com sucesso\n"))

        # core
        # if app_name is None or app_name == "core":
        #     self.stdout.write(self.style.HTTP_NOT_MODIFIED("\nprocesssando app: core"))
        #
        #     diretorio_fixtures = "backend/core/fixtures/"
        #     fixtures = sorted(os.listdir(diretorio_fixtures))
        #
        #     for fixture in fixtures:
        #         if fixture != "data.json":
        #             self.stdout.write(self.style.SQL_KEYWORD("\nmodel: " + fixture))
        #             management.call_command("loaddata", diretorio_fixtures + fixture)
        #
        #     self.stdout.write(self.style.SUCCESS("\nimportado com sucesso\n"))
