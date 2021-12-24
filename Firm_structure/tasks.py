from Firm_structure.models import Employees
from MyFirm.celery import app


@app.task
def add_salary(salary):
    total_salary = salary+100
    total_salary.save()
    return total_salary