from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
# from django.forms import Input
# from telethon import TelegramClient
# from home.management.commands.functions_file.function_msg import pyrogram_authorization
from home.models import user_details

class Command(BaseCommand):
    help = 'Create random users'

    def add_arguments(self, parser):
        parser.add_argument('number', type=str, help='Phone number of New user')
        # parser.add_argument('api_id', type=str, help='api_id of New user')
        # parser.add_argument('api_hash', type=str, help='api_hash of New user')
        # # parser.add_argument('username', type=str, help='username of New user')
        # parser.add_argument('emulator', type=str, help='emulator of New user')

    def handle(self, *args, **kwargs):
        ...