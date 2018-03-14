# Codenames - github.com/cameronleong - 14/03/2018 #
import discord
import random
import linecache
import re
import shelve
import copy
from random import shuffle, randint
from datetime import datetime


async def run(client, message):				#main loop

	#Declarations
	redTeam = [] 				#list of players in the game
	blueTeam = []
	redSpymaster = 0
	blueSpymaster = 0
	nounList = []
	key = []
	gamestate = 0

	wordlistlines = 52794					#number of lines in the wordlist you're using
	linenumber = random.randint(0, wordlistlines)		#pick a random line number
	answer = linecache.getline('nounList.txt',linenumber)	#linecache allows you to pull a single line instead of the entire file
	answer = answer.replace('\n','')			#strip line breaks
	
		

	if gamestate[0] == 0: await login(client,message,playerlist,gamestate,rules,roles)
	if gamestate[0] == 2: await night(client,message,playerlist,gamestate,rules,roles,canreject,cantreject)
	#gamestate[1] = randint(0,len(playerlist)-1)	#leadercounter
	#gamestate[2] = 1				#questcounter
	#gamestate[3] = 5				#passcounter
	#gamestate[4] = 0 				#successcount
	#gamestate[5] = 0 				#failcount #failcounter is 6
	names = []
	while gamestate[0] == 3 or gamestate[0] == 4 or gamestate[0] == 5:
		if gamestate[0] == 3: await quest(client,message,playerlist,gamestate,rules,roles,boardstate,names)
		if gamestate[0] == 4: await teamvote(client,message,playerlist,gamestate,rules,roles,boardstate,names)
		if gamestate[0] == 5: await privatevote(client,message,playerlist,gamestate,rules,roles,boardstate,names,canreject)
	if gamestate[0] == 6: await gameover(client,message,playerlist,gamestate,rules,roles,boardstate,names,canreject,cantreject)
