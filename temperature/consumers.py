from channels.generic.websocket import AsyncJsonWebsocketConsumer
from channels.db import database_sync_to_async
from temperature.models import Temperatura
from django.core import serializers


class TemperatureConsumer(AsyncJsonWebsocketConsumer):
    async def connect(self):
        await self.accept()

    async def disconnect(self, close_code):
        pass

    async def receive_json(self, content):
        message = await self.get_all_temperatures()
        await self.send_json(content=message)

    @database_sync_to_async
    def get_current_temperature(self):
        return serializers.serialize('json', [Temperatura.objects.last()])
