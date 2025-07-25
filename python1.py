import asyncio
import random
import string
from telethon import TelegramClient, functions, types, events
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.functions.channels import CreateChannelRequest, DeleteChannelRequest
from telethon.tl.functions.account import UpdateUsernameRequest
from telethon.tl.functions.messages import ImportChatInviteRequest, CheckChatInviteRequest
from telethon.errors.rpcerrorlist import UsernameNotOccupiedError
from itertools import cycle
from telethon.tl.functions.messages import GetHistoryRequest


api_id = 26056141
api_hash = '33a38c574c7934ef996294401e2b10b0'

default_reply = "Привет! слова-тригер:\nпрайс\nинфо\nжди докс"
special_keywords = {
    "прайс": "прайс находиться в https://t.me/pricvseniki",
    "инфо": "я кодер",
    "жди докс": "пошел нахуй сын свиньи<3"
}

client = TelegramClient('session', api_id, api_hash)

async def has_existing_chat(user_id):
    history = await client(GetHistoryRequest(
        peer=user_id,
        limit=2,
        offset_date=None,
        offset_id=0,
        max_id=0,
        min_id=0,
        add_offset=0,
        hash=0
    ))
    return len(history.messages) > 1

@client.on(events.NewMessage(incoming=True))
async def handler(event):
    if not event.is_private:
        return

    sender = await event.get_sender()
    user_id = sender.id
    message_text = event.raw_text.lower()

    for keyword, response in special_keywords.items():
        if keyword in message_text:
            print(f"Сообщение от @{sender.username or sender.first_name} — ответ: {response}")
            await event.reply(response)
            return

    already_chatted = await has_existing_chat(user_id)
    if not already_chatted:
        print(f"Новое сообщение от @{sender.username or sender.first_name}")
        await event.reply(default_reply)
    else:
        print(f"Сообщение от @{sender.username or sender.first_name}")

async def main():
    await client.start()
    print("Ага")
    await client.run_until_disconnected()

asyncio.run(main())