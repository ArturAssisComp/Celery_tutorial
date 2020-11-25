from celery import Celery
from datetime import datetime
app = Celery('tasks', broker='pyamqp://guest@localhost//')
app.config_from_object('celeryconfig')
@app.task
def teste():
    print("Test message: {}".format(datetime.now()))
