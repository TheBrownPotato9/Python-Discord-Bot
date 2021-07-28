from keep_alive import keep_alive
import discord
import sys
import io
import os


def run_code_func(String_to_run):
  str1 = String_to_run.replace("```python", "")
  str2 = str1.replace("```","")
  #print(String_to_run)
  #print(String_to_run)
  exec(str2)
client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith("```python"):
    run_code = message.content
    old_stdout = sys.stdout
    new_stdout = io.StringIO()
    sys.stdout = new_stdout
    run_code_func(run_code)
    output = new_stdout.getvalue()
    sys.stdout = old_stdout
    await message.channel.send("```" + output + "```")



    






    

keep_alive()
token = "this is supposed to be token pls don't hack me"
client.run(token)
client.run("this is also supposed to be token")

