from .models import User, Activity
import random
from datetime import date, timedelta
from django.core.management.base import BaseCommand
from django.db.models.base import ObjectDoesNotExist
from django.contrib.auth.models import User
from faker import Faker

faker = Faker()

def updatedb():
    for _ in range 10:
        user = User(faker.name(),faker.phone_number(), fake.pytimezone())
        user.save()

    for _ in range 10:
        activity = Activity(fake.date_this_century(), fake.date_this_century())
        activity.save()


class Command(BaseCommand):
    help = 'Populate glucose table with random dummy data.'
    args = 'no arguments'

    def handle(self, **options):
        updatedb()
