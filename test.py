# Codenames - github.com/cameronleong - 14/03/2018 #
import discord
import random
import linecache
import re
import shelve
import copy
from random import shuffle, randint
from datetime import datetime
from beautifultable import BeautifulTable

redTeam = [] 				#list of players in the game
blueTeam = []
redSpymaster = 0
blueSpymaster = 0
redScore = 0
blueScore = 0
nounList = []
key = []
blueFirstKey = [0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3]
redFirstKey = [0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,3]
gamestate = 0
wordlistlines = 4554					#number of lines in the wordlist you're using

for x in range(0,25):
	linenumber = random.randint(0, wordlistlines)		#pick a random line number
	answer = linecache.getline('nounlist.txt',linenumber)	#linecache allows you to pull a single line instead of the entire file
	answer = answer.replace('\n','')			#strip line breaks
	nounList.append(answer)

wordtable = BeautifulTable()
wordtable.append_row([nounList[0],nounList[1],nounList[2],nounList[3],nounList[4]])
wordtable.append_row([nounList[5],nounList[6],nounList[7],nounList[8],nounList[9]])
wordtable.append_row([nounList[10],nounList[11],nounList[12],nounList[13],nounList[14]])
wordtable.append_row([nounList[15],nounList[16],nounList[17],nounList[18],nounList[19]])
wordtable.append_row([nounList[20],nounList[21],nounList[22],nounList[23],nounList[24]])	
print (wordtable)

key = blueFirstKey
shuffle(key)

keytable = BeautifulTable()
keytable.append_row([key[0],key[1],key[2],key[3],key[4]])
keytable.append_row([key[5],key[6],key[7],key[8],key[9]])
keytable.append_row([key[10],key[11],key[12],key[13],key[14]])
keytable.append_row([key[15],key[16],key[17],key[18],key[19]])
keytable.append_row([key[20],key[21],key[22],key[23],key[24]])	
print (keytable)
