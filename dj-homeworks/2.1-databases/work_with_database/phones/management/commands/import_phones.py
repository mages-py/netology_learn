import csv

from django.core.management.base import BaseCommand
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        try:
            for phone in phones:
                new_phone = Phone.objects.create(**phone)
                print(f'Create a new phone. ID: {new_phone.id}')
            print('Done')
        except Exception as e: 
            print(f'Error: {e}')
                
