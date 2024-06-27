#consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import *   
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async



class UpdateConsumer(AsyncWebsocketConsumer):
  

    async def connect(self):
        self.room_group_name = 'updates'

        self.id = self.scope['url_route']['kwargs']['id']

        await self.channel_layer.group_add(
            'updates',
            self.channel_name
        )
 
        await self.accept()
 

    async def disconnect(self, close_code):
         

        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
        self.close()

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        message = text_data_json['message']
        id = text_data_json['id']
        if message == 'statusOnlinePing':
            status = text_data_json['status']
            await self.send(text_data=json.dumps({
                'message': 'pong',
                'status': status,
                'id': id
            }))
            return

        contact_id = text_data_json['contact_id']
        coversation_id = text_data_json['conversation_id']

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'id': id,
                'contact_id': contact_id,
                'conversation_id': coversation_id
            }
        )

    async def handle_empty_message(self, event):
        message = event['message']
        status = event['status']
        id = event['id']
        await self.send(text_data=json.dumps({
            'message': message,
            'status': status,
            'id': id
        }))

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        id = event['id']
        contact_id = event['contact_id']
        coversation_id = event['conversation_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'message': message,
            'id': id,
            'contact_id': contact_id,
            'conversation_id': coversation_id
        }))



class ChannelSocket(AsyncWebsocketConsumer):
    @database_sync_to_async
    def save_message(self,message, id,  channel_id):
        ChannelMessage.objects.create(cmContent=message, cmSender=id,  chID=channel_id).save()

    async def connect(self):
        self.room_group_name = 'channel'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']
        id = text_data_json['id']
        profile = text_data_json['profile']
        username = text_data_json['username']
        channel_id = text_data_json['channel_id']
        #save message to database here 
        await  self.save_message(message, id, channel_id)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'id': id,
                "username": username,
                "profile": profile
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        message = event['message']
        id = event['id']
        profile = event['profile']
        username = event['username']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'cmContent': message,
            'id': id,
            'profilepic': profile,
            'username': username
        }))

    