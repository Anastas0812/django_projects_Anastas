import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    help = 'Import phones from CSV'

    def handle(self, *args, **options):
        file_path = 'phones.csv'

        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file, delimiter=';')
            for row in reader:
                try:
                    phone = Phone(
                        id=row['id'],
                        name=row['name'],
                        image=row['image'],
                        price=row['price'],
                        release_date=row['release_date'],
                        lte_exists=row['lte_exists']
                    )
                    phone.save()
                except KeyError:
                    print('проблемы с айдишниками')
        self.stdout.write(self.style.SUCCESS('all is ok'))
