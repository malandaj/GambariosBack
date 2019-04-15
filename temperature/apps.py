from django.apps import AppConfig


class TemperatureConfig(AppConfig):
    name = 'temperature'

    def ready(self):
        from temperature.mqtt import mqtt
        mqtt.setup_mqtt()
