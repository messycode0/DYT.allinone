import discord
from datetime import datetime

from rich.console import Console
from rich.panel import Panel
from rich.prompt import Confirm

import log

console = Console()
log.clear_log()

# data file

# token handler
try:
    token_file = open("src/token.txt", "r")
    bot_token = token_file.readline()
    token_file.close()
except:
    console.print(Panel("Could not Find src/token.txt", title="Error"))
    #console.print("Want to create the token file? (make sure to have to token ready)")
    
    if Confirm.ask("Want to create the token file? (make sure to have to token ready)"):
        try:
            token_file_create_file_var = open("src/token.txt", "x")
            token_file_create_file_var.close()
        except:
            console.print("Token file already exist? internal error, try again. if it continues to do so, check the \"src/token.txt\"")
            exit(3)

        token_var = str(input("enter a vaild discord-bot token >>"))
        #token_file_write = open("src/token.txt", "w")
        with open("src/token.txt", "w") as token_file_write:
            token_file_write.writelines(token_var)

    else:
        console.print("exiting. the Bot wont work, without the token file, with a vaild token")
    exit(2)


# Data Parser
def data_parser():
    console.log("Starting data parsing analyse")
    with open("src/data/ALLINONE-001.PBD", "r") as Pushback_001_file:
        global IMMACULATA_BANNED_NAMES_SPLIT
        IMMACULATA_BANNED_NAMES_SPLIT = Pushback_001_file.read().split("::")
        print(IMMACULATA_BANNED_NAMES_SPLIT)



def status_return():
    status_file = open("src/status.txt", "r")
    status_value = status_file.readline()
    status_file.close()
    return status_value

def allinone_pushback_log(pushback_num):
    match pushback_num:
        case "001":
            console.print("detected MACKIE. ALLINONE001", style="red bold i u on white")
            log.file_log("ALLINONE001 detection", "pushback")
        case _:
            console.log(f"Not a valid pushback number: {pushback_num}")

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
        console.print(f"Logged in [green]successfully[/green] as [i blink]{self.user}")
        log.file_log("logged in")

        await client.change_presence(activity=discord.Game(name=status_return()))

    async def on_message(self, message):
        console.print(f'Message from {message.author}: [i]{message.content}[/i]', style="white")
        try:
            log.file_log(f'Message from {message.author}: {message.content}', "message")
        except UnicodeEncodeError:
            log.file_log(f'Message from {message.author}: {message.content}', "message_EMO")
            pass
        
        if message.author == client.user:
            return
        
        # check each word
        #!!! THIS IS SUCH SUCH SUCH BAD CODE MAN
        # START.1
        inputed_message_split = message.content.split()
        g = 0
        h = 0
        for word in inputed_message_split:
            # check for ALLINONE PUSHBACK 001
            # Pushback_001_file = open("src/data/ALLINONE-001.PBD", "r")         
            print(f"{g}: {word}")
            for line in IMMACULATA_BANNED_NAMES_SPLIT:
                # await message.channel.send(line)
                if word == line:
                    allinone_pushback_log("001")
                    await message.channel.send(f"Its Immaculata, not {word}")
                    await message.channel.send(f"get it right {message.author}")
                    await message.delete()

                    h = g

                    appended_return_sentence = ""
                    for i in range(len(inputed_message_split)):
                        if i != h:
                            wordf = inputed_message_split[i]
                        else:
                            wordf = "Immaculata"
                        appended_return_sentence = f"{appended_return_sentence} {wordf}"

                    await message.channel.send(f"{message.author} said: {appended_return_sentence}")
            g += 1
            # if word == "mackie":
            #     allinone_pushback_log("001")
            #     await message.channel.send(f"Its Immaculata, not {word}")
        # END.1

        # rest of commands here
        if message.content == ".end":
            await message.channel.send(f"good-day {message.author}")
            await message.channel.send(f"killed at {datetime.now()}")

            log.file_log("logged out and endded connection", "status")
            exit(0)
        
        if message.content == ".statusReload":
            await message.channel.send(f"gotcha...\nThe read file has \n```\n{status_return()}\n```")
            await client.change_presence(activity=discord.Game(name=status_return()))
            log.file_log(f"changed status too {status_return()}")


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

try:
    data_parser()
except Exception as E:
    print(E)

try:
    client.run(bot_token)
except:
    console.log(f"Could not log in with token [{bot_token}]")
    log.file_log(f"Could not log in with token [{bot_token}]", "internal")
    log.file_log(f"Could not log in with token [{bot_token}] and further changes", "internal")
