import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirm.settings')
django.setup()

import random

from Firm_structure.models import *
from faker import Faker




fake = Faker('ru_RU')

#
# def add_level():
#     lev = Levels.objects.get_or_create(level=random.choice(level))[0]
#     lev.save()
#     return lev


def add_head():
    head_d = Head.objects.get_or_create(name=fake.first_name(), surname=fake.last_name())[0]
    head_d.save()
    print(head_d)
    return head_d


def add_position():
    position = Position.objects.get_or_create(position=fake.job())[0]
    position.save()
    return position


def create_data(N):

    for _ in range(N):
        # level = add_level()
        head_d = add_head()
        position = add_position()

        employee = Employees.objects.get_or_create(
            first_name=fake.first_name(), last_name=fake.last_name(), middle_name=fake.middle_name(), position=position,
            employment_date=fake.date(), salary=fake.pyint(), total_salary=fake.pyint()*5)


if __name__ == '__main__':
    print('Creating employees. Wait')
    create_data(5)
    print('Creating complete')
