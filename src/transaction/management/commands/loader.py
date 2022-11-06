from pathlib import Path

from django.core.management.base import BaseCommand

from transaction.loader import Loader


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("file", type=Path)

    def handle(self, *args, **options):
        Loader(Path(options["file"]))
