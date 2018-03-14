import discord
import random
import linecache
import re
import shelve
from random import *
from codenames import *

client = discord.Client()
busyChannels = []


@client.event
async def on_message(message):
	if message.author == client.user:			# we do not want the bot to reply to itself
		return
		
	if message.content.startswith('!hello'):
		msg = 'Hello {0.author.mention}'.format(message)
		await client.send_message(message.channel, msg)
	
	if message.content.startswith('!codenames'):
		if message.channel in busyChannels:
			await client.send_message(message.channel, "Channel busy with another activity.")
		else:
			busyChannels.append(message.channel)
			await client.send_message(message.channel, "Starting **Codenames** in `#"+message.channel.name+"`...")
			await run(client, message)
			busyChannels.remove(message.channel)
			
	if message.content.startswith('!score'):
		await scoreboard(client, message)

	if message.content.startswith('!help'):
		await client.send_message(message.author, 'Please visit https://cameronleong.github.io/avalon to find out more.')


		
@client.event
async def on_ready():
	print('Connected!')
	print('Username: ' + client.user.name)
	print('ID: ' + client.user.id)
	#await client.change_status(game)
	

client.run('YOUR TOKEN HERE')
