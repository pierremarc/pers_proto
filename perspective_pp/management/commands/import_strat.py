import re
from pathlib import Path
from csv import DictReader
from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User

from perspective_pp.models.project import Project, ContactRef
from perspective_pp.models.types import *

FIELDS = [
    'Secteurs',
    'Id',
    'Projet ou nom du site par défaut ',
    'Occupant et / ou exploitant / acteurs prospectés',
    'Propriétaire et /ou promoteur',
    'Intentions connues',
    'Actuel',
    'projeté',
    'Horizon  conception Horizon réalisation Horizon installation',
    'Contacts (nom et tel)',
    'Contacts (mails)',
    'Site: n° rue',
    'dernière MAJ',
]

SECTEUR = FIELDS[0]
ID = FIELDS[1]
NOM = FIELDS[2]
OCCUPANT = FIELDS[3]
PROPRIO = FIELDS[4]
INTENTION = FIELDS[5]
ACTUEL = FIELDS[6]
PROJETE = FIELDS[7]
HORIZON = FIELDS[8]
CONTACT_NOM = FIELDS[9]
CONTACT_EMAIL = FIELDS[10]
SITE = FIELDS[11]
MAJ = FIELDS[12]

HORI_RE = re.compile('\\D*([0-9]+)')


def horizon(row):
    s = row[HORIZON]
    try:
        gs = HORI_RE.match(s).groups()
        return int(gs[0])
    except Exception:
        return 0


class Command(BaseCommand):
    help = """Import Projects From 'Strategie'
    """

    output_transaction = True

    def add_arguments(self, parser):
        parser.add_argument('csv_file')
        parser.add_argument('username')

    def handle(self, *args, **options):
        csv_file_path = Path(options['csv_file'])
        self.user = User.objects.get(username=options['username'])

        with open(csv_file_path.as_posix()) as f:
            for row in DictReader(f):
                self.process_row(row)

    def process_row(self, row):
        p = Project.objects.create()
        o = ContactRef.objects.create(name=row[OCCUPANT])
        c = ContactRef.objects.create(name=row[CONTACT_NOM])

        ProjectName.objects.create(user=self.user, value=row[NOM], project=p)
        Occupying.objects.create(user=self.user, value=o, project=p)
        Intent.objects.create(user=self.user, value=row[INTENTION], project=p)
        PresentState.objects.create(
            user=self.user, value=row[ACTUEL], project=p)
        ProjectedState.objects.create(
            user=self.user, value=row[PROJETE], project=p)
        HorizonDesign.objects.create(
            user=self.user, value=horizon(row), project=p)
        Contact.objects.create(user=self.user, value=c, project=p)

        self.stdout.write('Imported ' + self.style.SUCCESS(row[ID]))
