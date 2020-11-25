# Celery_tutorial
Repositório com execução do tutorial apresentado em: https://docs.celeryproject.org/en/stable/getting-started/first-steps-with-celery.html

Os passos para a execução de tasks de maneira assíncrona são:
- Abrir o ambiente virtual;
- Abrir o worker --> celery -A tasks worker --loglevel=INFO
- Executar as tarefas por meio de um terminal python, por exemplo. Como exemplo, execução de tarefa agendada para executar daqui 30 segundos:

Python


\>\>\> teste.apply_async(countdown=30)
