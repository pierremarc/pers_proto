from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import (
    EventLog,
    StartTime,
    EndTime,
    Name,
    Note,
    Point,
    Polygon,
    Step,
)


def receiver_save(sender, **kwargs):
    print('receiver_save {}'.format(sender._meta.model_name))
    EventLog.objects.create(
        model=sender._meta.model_name,
        action='save'
    )

def post_save_connect(M):
    print('signals.post_save_connect {}'.format(M._meta.model_name))
    post_save.connect(receiver_save, sender=M, dispatch_uid='signal_save_{}'.format(M._meta.model_name))

def connect():
    print('signals.connect')
    for M in (StartTime, EndTime, Name, Note, Point, Polygon, Step,):
        post_save_connect(M)

