async def switch_chat(self, chat_id, limit_m=15):
    async with self.client:
        try:
            self.active_chat = await self.client.get_entity(chat_id)
        except:
            print(f"\nError in getting the entity. (error of 'switch_chat' class method...)")
            return
        
        chat_name = getattr(self.active_chat, 'title', None) or getattr(self.active_chat, 'first_name', None)
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
                data = message.data.strftime("%Y-%m-%d %H:%M")
                print(f"\n-{sender}-"
                      f"({data}) --> {message.text}")
        except:
            print("\nError in getting messages. (error of 'switch_chat' class method...)")
            return
