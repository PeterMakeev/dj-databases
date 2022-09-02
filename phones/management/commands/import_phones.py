import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open("phones.csv") as csvfile:
            phone_reader = csv.DictReader(csvfile, delimiter=';')
            for phone in phone_reader:
                id, name, image, price, release_date, lte_exists, slug = phone.values()
                slug = slugify(name)
                phone = Phone(id=id, name=name, image=image, price=price, release_date=release_date,
                              lte_exists=lte_exists, slug=slug)
                phone.save()