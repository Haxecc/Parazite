from telethon import TelegramClient

class User:
    def __init__(self, api_id, api_hash, session_name):
        self.client = TelegramClient(session_name, api_id, api_hash)
        self.active_chat = None

    async def list_chats(self):
        async with self.client:
            dialogs = await self.client.get_dialogs()
        if not dialogs:
            return
        print("The list of chats: ")
        for dialog in dialogs: 
            name = getattr(dialog.entity, 'title', None) or getattr(dialog.entity, 'first_name')
            print(f"(--'{name}'--) --> id: {dialog.id}")


    async def send_message(self, destination, message):
        with self.client:       
            self.client.send_message(destination, message)
            print(f"(--'{message}'--) was sent to {destination}")
        


async def main(user):
    await user.list_chats()

if __name__ == "__main__":
    f = open("secret.txt")
    api_id = f.readline().strip()
    api_hash = f.readline().strip()
    session_name = "anon"
    f.close()
    
    user = User(api_id, api_hash, session_name)
    
    with user.client:
        user.client.loop.run_until_complete(main(user))
