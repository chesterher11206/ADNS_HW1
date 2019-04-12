from django.apps import AppConfig
import threading


class BoardConfig(AppConfig):
    name = 'board'

    def ready(self):
        t = threading.Thread(target=mqtt_thread, args=(), kwargs={})
        t.setDaemon(True)
        t.start()

def mqtt_thread():
    from .mqtt import client
    while True:
        client.loop_start()
