async def switch_chat(self, chat_id, limit_m=15):
    async with self.client:
        try:
            self.active_chat = await self.client.get_entity(chat_id)
        except:
            print(f"\nError in getting the entity.")
            return
        
        chat_name = getattr(self.active_chat, 'title', None) or getattr(self.active_chat, 'first_name')
        print(f"\nSwitching in dialog: {chat_name}")

        try:
            messages = await self.client.get_messages(self.active_chat, limit = limit_m)
            if not messages:
                print(f"\nNo messages in this dialog.")
                return

            for message in messages:
                if message.out:
                    sender = "Me"
                else:
                    sender = "Partner"
                print(f"\n-{sender}-"
                      f"--> {message.text}")
        except:
            print()