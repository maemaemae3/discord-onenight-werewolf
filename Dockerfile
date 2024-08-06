FROM python:3.12.4

RUN pip install -U pip
RUN pip install -U discord.py

ENTRYPOINT python run.py
