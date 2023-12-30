import discord
from datetime import datetime

# token handler
token_file = open("src/token.txt", "r")
bot_token = token_file.readline()
token_file.close()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        print(f'Message from {message.author}: {message.content}')

        if message.author == client.user:
            return
        
        # check each word
        inputed_message_split = message.content.split()
        for word in inputed_message_split:
            if word == "mackie":
                print("detected MACKIE. ALLINONE001")
                await message.channel.send(f"Its Immaculata, not {word}")
        
        # rest of commands here
        if message.content == ".end":
            await message.channel.send(f"good-day {message.author}")
            await message.channel.send(f"killed at {datetime.now()}")
            exit(0)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(bot_token)
