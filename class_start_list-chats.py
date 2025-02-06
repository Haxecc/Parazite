from telethon import TelegramClient

class User:
    def __init__(self, api_id, api_hash, session_name):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.active_chat = None

    async def start(self):
        await self.client.start()

    async def list_chats(self):
        dialogs = await self.client.get_dialogs()
        if not dialogs:
            return
        print("The list of chats: ")
        for d in dialogs: 
            name = getattr(d.entity, 'title', None) or getattr(d.entity, 'first_name')
            print(f"(--'{name}'--) --> id: {d.id}")
