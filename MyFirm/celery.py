import os
from celery import Celery
from celery.schedules import crontab



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'MyFirm.settings')

app = Celery('MyFirm')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'chenge-total-salary-every-120-minutes': {
        'task': 'Firm_structure.tasks.add_salary',
        'schedule': crontab(minute='*/120'),
    },
}