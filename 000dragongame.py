import shutil
import pygame
import YouDied
columns = shutil.get_terminal_size().columns
money = 0
exp = 0
heromaxhp = 20
currentherohp = 20
dragonhp = 1000
mobdamage = 0
mobhp = 0
weapondamage = 2
blankcounter = 1
bankedgold = 0 
goldearned = 0
expearned = 0
counter = 1

if currentherohp <= 0:
	YouDied.music()

if blankcounter in range(1,4):
	blank = "Green Slime"
elif blankcounter in range(4,7):
	blank = "Blue Slime"
elif blankcounter in range(7,10):
	blank = "Black Slime"
elif blankcounter in range(10,11):
	blank = "King Slime"

elif blankcounter in range(11,16):
	blank = "Skeleton Fighter"
elif blankcounter in range (16,21):
	blank = "Skeleton Warrior"

elif blankcounter in range (21,24):
	blank = "Troll"
elif blankcounter in range (24,27):
	blank = "Enraged Troll"
elif blankcounter in range (27,30):
	blank = "Troll Arson"
elif blankcounter in range (30,31):	
	blank = "Troll Wizard"

elif blankcounter in range (31,36):
	blank = "Mermaid"
elif blankcounter in range (36,41):
	blank = "Land Shark"

elif blankcounter in range (41,44):
	blank = "Giant Crab"
elif blankcounter in range (44,47):
	blank = "Sandsman Archer"
elif blankcounter in range (47,40):
	blank = "Sandsman Sorceror"
elif blankcounter in range (40,41):
	blank = "Sandsman King"

elif blankcounter in range (51,56):
	blank = "Baby Drake"
elif blankcounter in range (56,61):
	blank = "Horned Drake"

elif blankcounter in range (61,64):
	blank = "Ogre Wizard"
elif blankcounter in range (64,67):
	blank = "Ogre Warrior"
elif blankcounter in range (67,60):
	blank = "Ogre Mage"
elif blankcounter in range (60,61):
	blank = "Ogre King"

elif blankcounter in range (71,76):
	blank = "Ghost God"
elif blankcounter in range (76,80):
	blank = "Snake God"

elif blankcounter in range (81,84):
	blank = "Crystal Prisoner's Steeds"
elif blankcounter in range (84,87):
	blank = "Crystal Prisoner"
elif blankcounter in range (87,90):
	blank = "Lucky Dijinn"
elif blankcounter in range (90,91):
	blank = "Lucky Ent"

elif blankcounter in range (91,96):
	blank = "Leviathan"
elif blankcounter in range (96,101):
	blank = "White Demon"

'''
konamicode = input("__,_,____,____,____,_____,____,_____,_,_,_____  ".center(columns))
if konamicode == ("Up,Up,Down,Down,Left,Right,Left,Right,B,A,Start"):
	print("Good try but im too lazy to make it actually function".center(columns))
print("Would you like a tutorial to teach you how to play?(Enter Y for yes and N for no)".center(columns))
tutorial = input(">")
while tutorial != ("Y") and tutorial != ("N"):
	print("That's not an option, how about retrying?".center(columns))
	tutorial = input(">")
if tutorial == ("Y"):
	print("The goal of this game is to defeat the dragon(duh), you start out with 20 hp and the dragon gets 1000, must farm monsters to get exp to level up and gold to buy equipment that makes your character more powerful in the shop(You can use regular attacks and items during battle, or you could flee to live another day. Once you think you are ready to face the dragon, you can challenge it but if you die during any fight, you will lose all the progress you have made and the game will start over.".center(columns))
	print("")
	print("")
else:
	print("")
	print("")
	
print("Welcome to Dragon Simulator".center(columns))
print("".center(columns))
print("".center(columns))
print("Hey you, traveler passing by.".center(columns))
print("Will you help us defeat the dragon harassing our town?(Enter Yes or No)".center(columns))
yslashn = input(">")
while yslashn != "Yes" and yslashn != "yes" and yslashn != "No" and yslashn != "no" and yslashn != "NO" and yslashn != "YES" and yslashn != "yEs" and yslashn != "nO" and yslashn != "yeS" and yslashn != "YEs" and yslashn != "YeS" and yslashn != "yES":
	print("That's not a yes or no...".center(columns))
	print("Will you or will you not?".center(columns))
	yslashn = input(">")
if yslashn == "NO":
	print("We didn't want your help anyways...".center(columns))
elif yslashn == "No":
	print("We didn't want your help anyways...".center(columns))
elif yslashn == "nO":
	print("We didn't want your help anyways...".center(columns))
elif yslashn == "no":
	print("We didn't want your help anyways...").center(columns)
else:
	print("Get on your way then!".center(columns))
if yslashn == ("no"):
	raise SystemExit(0)
elif yslashn == ("NO"):
	raise SystemExit(0)
elif yslashn == ("No"):
	raise SystemExit(0)
elif yslashn == ("nO"):
	raise SystemExit(0)
else:
'''
while True:
	print("Would you like to like to Shop, Farm monsters, Heal, or Fight the dragon?(Enter S to shop, F to farm monsters, H to heal, and D to fight the dragon;if you fight the dragon before you are ready you will lose all your progress!".center(columns))
	option = input(">")
	if option != "S" and option != "F" and option != "H":
		print("Sorry but it appears that that isn't an option")
		continue
	else:
		break
while option == "S" or option == "F" or option == "H":
	if option == "S":
		print("Welcome traveler, Would you like to buy anything?(Y to buy or N to exit)".center(columns))
		buying = input(">")
		break
	elif option == "F":
		print("A",blank,"has appeared!")
		blankcounter += 1 
		break
	elif option == "H":
		print("Hello traveler, would you be in need of any healing? My rate is 2 Gold per hp point.(Y to heal or N to Exit)".center(columns))
		healing = input(">")
		break
		
if option == "S":		
	while buying != "Y" and buying != "N":
		print("That's not a yes or no...".center(columns))
		print("Now would you like to buy our wares?(Y or N)".center(columns))
		buying = input(">")
		if buying == "Y":
			print("We are currently selling:".center(columns))
		elif buying == "N":
			print("What in the hell are you doing in my shop then?".center(columns))
		else:
			pass
			
if option == "H":
	while healing != "Y" and healing != "N":
		print("It was a yes or no question...".center(columns))
		print("Give me an answer".center(columns))
		healing = input(">")
		if healing == "Y":
			print("I will heal you to full hp for".center(columns))
		elif healing == "N":
			print("You came just to see me? You're so sweet.".center(columns))
		else:
			pass
while option == "D":
	while action == None:
		if dragonhp > 0:
			print("Would you like to Attack(A), Use an Item(I), or Run away(R)?".center(columns))
			action = input(">")
			break
while option == "D" and (dragonhp) > 0:
	if action == "A":
		dragonhp = dragonhp - weapondamage
		print("You did {} damage!".center(columns).format(weapondamage))
		action = None
	elif action == "I":
		print("What action would you like to use?")
	elif action == "R":
		print("You try to run but you are snatched back by the dragon!")
		

