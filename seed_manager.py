from django_seed import Seed
from Firm_structure.models import *
import random
seeder = Seed.seeder(locale='it_IT')


def populate_models():
    seeder.add_entity(Head, 10, {
        'name': lambda x: seeder.faker.first_name(),
        'surname': lambda x: seeder.faker.last_name()
    })
    seeder.add_entity(Position, 10, {
        'position': lambda x: seeder.faker.job()
    })
    seeder.add_entity(Employees, 10, {
        'first_name': lambda x: seeder.faker.first_name(),
        'middle_name': lambda x: seeder.faker.first_name(),
        'last_name': lambda x: seeder.faker.last_name(),
        'employment_date': lambda x: seeder.faker.date_this_month(),
        'salary': lambda x: random.randint(0, 500),
        'total_salary_paid': lambda x: random.randint(501, 1000),
    })


    inserted_pks = seeder.execute()