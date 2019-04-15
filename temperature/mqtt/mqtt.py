import paho.mqtt.client as mqtt
from temperature.models import Temperatura


def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("/gambarios/temperatura")


def on_message(client, userdata, msg):
    t = Temperatura.objects.create_temperatura(msg.payload, 1)
    t.save()

def setup_mqtt():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect("iot.eclipse.org", 1883, 60)
    client.loop_start()
