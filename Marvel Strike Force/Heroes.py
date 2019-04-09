"""

 Ersegun Omer EROL represents..
 "Personal Implementations" Series
 TOPIC	: 	Games
 GAME	:	Marvel Strike Force
 CHAPTER:	Intersection of Traits

 ALL RIGHTS RESERVED...

"""

import sys

# TRAITS AS TUPLES
HERO = ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones", "Punisher", "Deadpool", "Captain America", "Night Nurse", "Spider-Man", "Wolverine", "Ms. Marvel", 
	"SHIELD Medic", "SHIELD Assault", "Hulk", "Captain Marvel", "Cable", "Hawkeye", "Drax", "Storm", "SHIELD Operative", "SHIELD Security", "Vision", "Quake", 
	"SHIELD Trooper", "Rocket Raccoon", "Groot", "Black Widow", "War Machine", "Gamora", "Doctor Strange", "Spider-Man [Miles]", "Ant-Man", "Scarlet Witch", "Wasp", 
	"Mantis", "Black Panther", "Iron Man", "M'Baku", "Nick Fury", "Star-Lord", "Thor")
VILLAIN = ("Crossbones", "Elektra", "Hand Sorceress", "Yondu", "Hand Sentry", "Mordo", "Bullseye", "Hydra Sniper", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", 
	"Korath The Pursuer", "Kree Noble", "Pyro", "Mercenary Sniper", "Hand Archer", "Hand Assassin", "Hydra Scientist", "Mercenary Soldier", "Nebula", "Ravager Boomer", 
	"Ravager Bruiser", "Hand Blademaster", "Kingpin", "Killmonger", "Minn-Erva", "Kree Oracle", "Mercenary Riot Guard", "Kree Reaper", "AIM Researcher", "Kree Royal Guard", 
	"Mercenary Lieutenant", "Hydra Armored Guard", "Ronan The Accuser", "Scientist Supreme", "Venom", "AIM Monstrosity", "Kree Cyborg", "Winter Soldier", "AIM Infector", 
	"Mystique", "Sabretooth", "Hydra Grenadier", "AIM Assaulter", "Green Goblin", "Loki", "Nobu", "Carnage", "Juggernaut", "Magneto", "Thanos", "Ultimus", "Ultron")

CITY = ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones", "Punisher", "Elektra", "Hand Sorceress", "Hand Sentry", "Night Nurse", "Spider-Man", "Ms. Marvel", 
	"Bullseye", "Mercenary Sniper", "Hand Archer", "Hand Assassin", "Mercenary Soldier", "Hand Blademaster", "Kingpin", "Mercenary Riot Guard", "Mercenary Lieutenant", 
	"Venom", "Spider-Man [Miles]", "Green Goblin", "Nobu", "Carnage")
GLOBAL = ("Deadpool", "Captain America", "Crossbones", "Wolverine", "SHIELD Medic", "Hydra Sniper", "SHIELD Assault", "Hydra Rifle Trooper", "Hulk", "AIM Security", "Hawkeye", 
	"Pyro", "Hydra Scientist", "Killmonger", "Storm", "SHIELD Operative", "SHIELD Security", "Vision", "AIM Researcher", "Quake", "SHIELD Trooper", "Hydra Armored Guard", 
	"Black Widow", "War Machine", "Scientist Supreme", "AIM Monstrosity", "Winter Soldier", "AIM Infector", "Ant-Man", "Mystique", "Sabretooth", "Hydra Grenadier", 
	"Scarlet Witch", "AIM Assaulter", "Wasp", "Black Panther", "Iron Man", "Juggernaut", "Magneto", "M'Baku", "Nick Fury", "Ultron")
COSMIC = ("Yondu", "Mordo", "Ravager Stitcher", "Captain Marvel", "Cable", "Korath The Pursuer", "Kree Noble", "Nebula", "Ravager Boomer", "Ravager Bruiser", "Minn-Erva", 
	"Drax", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Rocket Raccoon", "Groot", "Ronan The Accuser", "Gamora", "Doctor Strange", "Kree Cyborg", "Mantis", "Loki", 
	"Star-Lord", "Thanos", "Thor", "Ultimus")

TECH = ("Crossbones", "Hydra Sniper", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", "Korath The Pursuer", "Mercenary Sniper", "Nebula", "Ravager Boomer", 
	"Minn-Erva", "Kree Oracle", "Vision", "Mercenary Lieutenant", "Rocket Raccoon", "Hydra Armored Guard", "War Machine", "Scientist Supreme", "Kree Cyborg", "Ant-Man", 
	"Hydra Grenadier", "AIM Assaulter", "Wasp", "Iron Man", "Star-Lord", "Ultron")
BIO = ("Daredevil", "Luke Cage", "Jessica Jones", "Captain America", "Spider-Man", "Ms. Marvel", "Hulk", "Captain Marvel", "Kree Noble", "Ravager Bruiser", "Drax", 
	"Kree Reaper", "Kree Royal Guard", "Quake", "Groot", "Venom", "AIM Monstrosity", "Spider-Man [Miles]", "Winter Soldier", "AIM Infector", "Mantis", "Green Goblin", 
	"Carnage")
MYSTIC = ("Iron Fist", "Elektra", "Hand Sorceress", "Yondu", "Hand Sentry", "Mordo", "Hand Assassin", "Ronan The Accuser", "Doctor Strange", "Scarlet Witch", "Loki", 
	"Black Panther", "Nobu", "Juggernaut", "M'Baku", "Thanos", "Thor", "Ultimus")
SKILL = ("Punisher", "Night Nurse", "SHIELD Medic", "Bullseye", "SHIELD Assault", "Hawkeye", "Hand Archer", "Hydra Scientist", "Mercenary Soldier", "Hand Blademaster", 
	"Kingpin", "Killmonger", "Mercenary Riot Guard", "SHIELD Operative", "SHIELD Security", "AIM Researcher", "SHIELD Trooper", "Black Widow", "Gamora", "Nick Fury")
MUTANT = ("Deadpool", "Wolverine", "Cable", "Pyro", "Storm", "Mystique", "Sabretooth", "Magneto")

BLASTER = ("Punisher", "Bullseye", "Hydra Sniper", "SHIELD Assault", "Hydra Rifle Trooper", "Cable", "Korath The Pursuer", "Pyro", "Mercenary Sniper", "Hand Archer", 
	"Mercenary Soldier", "Ravager Boomer", "Killmonger", "SHIELD Trooper", "Rocket Raccoon", "War Machine", "Kree Cyborg", "Winter Soldier", "Hydra Grenadier", 
	"AIM Assaulter", "Wasp", "Green Goblin", "Iron Man", "Thor", "Ultron")
BRAWLER = ("Daredevil", "Iron Fist", "Deadpool", "Elektra", "Spider-Man", "Wolverine", "Ms. Marvel", "Captain Marvel", "Nebula", "Hand Blademaster", "Kree Reaper", "Gamora", 
	"AIM Monstrosity", "Spider-Man [Miles]", "Sabretooth", "Black Panther", "Carnage", "Ultimus")
CONTROLLER = ("Jessica Jones", "Mordo", "Hawkeye", "Kree Noble", "Hand Assassin", "Storm", "Vision", "Quake", "Black Widow", "Ronan The Accuser", "Venom", "AIM Infector", 
	"Ant-Man", "Mystique", "Scarlet Witch", "Mantis", "Loki", "Nobu", "Magneto", "Star-Lord")
PROTECTOR = ("Luke Cage", "Captain America", "Crossbones", "Hand Sentry", "Hulk", "AIM Security", "Ravager Bruiser", "Kingpin", "Drax", "Mercenary Riot Guard", 
	"SHIELD Security", "Kree Royal Guard", "Hydra Armored Guard", "Juggernaut", "M'Baku", "Thanos")
SUPPORT = ("Hand Sorceress", "Yondu", "Night Nurse", "SHIELD Medic", "Ravager Stitcher", "Hydra Scientist", "Minn-Erva", "Kree Oracle", "SHIELD Operative", "AIM Researcher", 
	"Mercenary Lieutenant", "Groot", "Scientist Supreme", "Doctor Strange", "Nick Fury")

AIM = ("AIM Security", "AIM Researcher", "Scientist Supreme", "AIM Monstrosity", "AIM Infector", "AIM Assaulter")
ASGARDIAN = ("Loki", "Thor")
AVENGER = ("Captain America", "Hulk", "Hawkeye", "Vision", "Black Widow", "War Machine", "Ant-Man", "Scarlet Witch", "Black Panther", "Iron Man", "Nick Fury", "Thor")
BROTHERHOOD = ("Pyro", "Mystique", "Sabretooth", "Juggernaut", "Magneto")
DEFENDER = ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones")
GUARDIAN = ("Drax", "Rocket Raccoon", "Groot", "Gamora", "Mantis", "Star-Lord")
HAND = ("Elektra", "Hand Sorceress", "Hand Sentry", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Nobu")
HYDRA = ("Crossbones", "Hydra Sniper", "Hydra Rifle Trooper", "Hydra Scientist", "Hydra Armored Guard", "Winter Soldier", "Hydra Grenadier")
KREE = ("Captain Marvel", "Korath The Pursuer", "Kree Noble", "Minn-Erva", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Ronan The Accuser", "Kree Cyborg", "Ultimus")
MERCENARY = ("Deadpool", "Bullseye", "Korath The Pursuer", "Mercenary Sniper", "Mercenary Soldier", "Killmonger", "Mercenary Riot Guard", "Mercenary Lieutenant")
MILITARY = ("Captain America", "Captain Marvel", "War Machine", "Winter Soldier")
RAVAGER = ("Yondu", "Ravager Stitcher", "Ravager Boomer", "Ravager Bruiser")
SHIELD = ("Captain America", "SHIELD Medic", "SHIELD Assault", "Hawkeye", "SHIELD Operative", "SHIELD Security", "Quake", "SHIELD Trooper", "Black Widow", "Nick Fury")
SPIDERVERSE = ("Spider-Man", "Venom", "Spider-Man [Miles]", "Green Goblin", "Carnage")
WAKANDAN = ("Killmonger", "Black Panther", "M'Baku")
XMEN = ("Wolverine", "Storm")
XFORCE = ("Deadpool", "Cable")

MINION = ("Hand Sorceress", "Hand Sentry", "SHIELD Medic", "Hydra Sniper", "SHIELD Assault", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", "Kree Noble", 
	"Mercenary Sniper", "Hand Archer", "Hand Assassin", "Hydra Scientist", "Mercenary Soldier", "Ravager Boomer", "Ravager Bruiser", "Hand Blademaster", "Kree Oracle", 
	"Mercenary Riot Guard", "SHIELD Operative", "SHIELD Security", "Kree Reaper", "AIM Researcher", "Kree Royal Guard", "Mercenary Lieutenant", "SHIELD Trooper", 
	"Hydra Armored Guard", "AIM Monstrosity", "Kree Cyborg", "AIM Infector", "Hydra Grenadier", "AIM Assaulter")
INHUMAN = ("Ms. Marvel", "Quake")
ETERNAL = ("Thanos", "Ultimus")
MARTIALARTIST = ("Daredevil", "Iron Fist", "Elektra", "Hand Sorceress", "Hand Sentry", "Mordo", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Nobu")

# Helper variables
wantToContinue = False
#writtenOnce = False

def findIntersection(traits):
	if len(traits) == 1: return set(traits[0])
	return set(traits[0]) & findIntersection(traits[1:])

def mainScreenInfo():
	print("  Welcome to \"Marvel Strike Force - Characters' Traits\"")
	print(" Here you can find common heroes of any traits")
	print("==========")

def informingAboutFormat():
	print("  Please don't use the \"-\" symbol or any spaces, just write as a whole and in upper-case, otherwise the program will terminate!")
	print(" Invalid Inputs: \"X-MEN\", \"MARTIAL ARTIST\", \"Hero\", \"hand\", ...")
	print(" Valid Inputs:   \"XMEN\",  \"MARTIALARTIST\",  \"HERO\", \"HAND\", ...")

def tuplesToTraits(traitsAsTuples): # If tuples are modified, all those modifications should also be done here in this function!!!
	resultList = []
	for i in range(len(traitsAsTuples)):
		if traitsAsTuples[i] == ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones", "Punisher", "Deadpool", "Captain America", "Night Nurse", "Spider-Man", "Wolverine", "Ms. Marvel", 
								"SHIELD Medic", "SHIELD Assault", "Hulk", "Captain Marvel", "Cable", "Hawkeye", "Drax", "Storm", "SHIELD Operative", "SHIELD Security", "Vision", "Quake", 
								"SHIELD Trooper", "Rocket Raccoon", "Groot", "Black Widow", "War Machine", "Gamora", "Doctor Strange", "Spider-Man [Miles]", "Ant-Man", "Scarlet Witch", "Wasp", 
								"Mantis", "Black Panther", "Iron Man", "M'Baku", "Nick Fury", "Star-Lord", "Thor"):
			resultList.append("HERO")
		elif traitsAsTuples[i] == ("Crossbones", "Elektra", "Hand Sorceress", "Yondu", "Hand Sentry", "Mordo", "Bullseye", "Hydra Sniper", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", 
								"Korath The Pursuer", "Kree Noble", "Pyro", "Mercenary Sniper", "Hand Archer", "Hand Assassin", "Hydra Scientist", "Mercenary Soldier", "Nebula", "Ravager Boomer", 
								"Ravager Bruiser", "Hand Blademaster", "Kingpin", "Killmonger", "Minn-Erva", "Kree Oracle", "Mercenary Riot Guard", "Kree Reaper", "AIM Researcher", "Kree Royal Guard", 
								"Mercenary Lieutenant", "Hydra Armored Guard", "Ronan The Accuser", "Scientist Supreme", "Venom", "AIM Monstrosity", "Kree Cyborg", "Winter Soldier", "AIM Infector", 
								"Mystique", "Sabretooth", "Hydra Grenadier", "AIM Assaulter", "Green Goblin", "Loki", "Nobu", "Carnage", "Juggernaut", "Magneto", "Thanos", "Ultimus", "Ultron"):
			resultList.append("VILLAIN")
		elif traitsAsTuples[i] == ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones", "Punisher", "Elektra", "Hand Sorceress", "Hand Sentry", "Night Nurse", "Spider-Man", "Ms. Marvel", 
								"Bullseye", "Mercenary Sniper", "Hand Archer", "Hand Assassin", "Mercenary Soldier", "Hand Blademaster", "Kingpin", "Mercenary Riot Guard", "Mercenary Lieutenant", 
								"Venom", "Spider-Man [Miles]", "Green Goblin", "Nobu", "Carnage"):
			resultList.append("CITY")
		elif traitsAsTuples[i] == ("Deadpool", "Captain America", "Crossbones", "Wolverine", "SHIELD Medic", "Hydra Sniper", "SHIELD Assault", "Hydra Rifle Trooper", "Hulk", "AIM Security", "Hawkeye", 
								"Pyro", "Hydra Scientist", "Killmonger", "Storm", "SHIELD Operative", "SHIELD Security", "Vision", "AIM Researcher", "Quake", "SHIELD Trooper", "Hydra Armored Guard", 
								"Black Widow", "War Machine", "Scientist Supreme", "AIM Monstrosity", "Winter Soldier", "AIM Infector", "Ant-Man", "Mystique", "Sabretooth", "Hydra Grenadier", 
								"Scarlet Witch", "AIM Assaulter", "Wasp", "Black Panther", "Iron Man", "Juggernaut", "Magneto", "M'Baku", "Nick Fury", "Ultron"):
			resultList.append("GLOBAL")
		elif traitsAsTuples[i] == ("Yondu", "Mordo", "Ravager Stitcher", "Captain Marvel", "Cable", "Korath The Pursuer", "Kree Noble", "Nebula", "Ravager Boomer", "Ravager Bruiser", "Minn-Erva", 
								"Drax", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Rocket Raccoon", "Groot", "Ronan The Accuser", "Gamora", "Doctor Strange", "Kree Cyborg", "Mantis", "Loki", 
								"Star-Lord", "Thanos", "Thor", "Ultimus"):
			resultList.append("COSMIC")
		elif traitsAsTuples[i] == ("Crossbones", "Hydra Sniper", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", "Korath The Pursuer", "Mercenary Sniper", "Nebula", "Ravager Boomer", 
								"Minn-Erva", "Kree Oracle", "Vision", "Mercenary Lieutenant", "Rocket Raccoon", "Hydra Armored Guard", "War Machine", "Scientist Supreme", "Kree Cyborg", "Ant-Man", 
								"Hydra Grenadier", "AIM Assaulter", "Wasp", "Iron Man", "Star-Lord", "Ultron"):
			resultList.append("TECH")
		elif traitsAsTuples[i] == ("Daredevil", "Luke Cage", "Jessica Jones", "Captain America", "Spider-Man", "Ms. Marvel", "Hulk", "Captain Marvel", "Kree Noble", "Ravager Bruiser", "Drax", 
								"Kree Reaper", "Kree Royal Guard", "Quake", "Groot", "Venom", "AIM Monstrosity", "Spider-Man [Miles]", "Winter Soldier", "AIM Infector", "Mantis", "Green Goblin", 
								"Carnage"):
			resultList.append("BIO")
		elif traitsAsTuples[i] == ("Iron Fist", "Elektra", "Hand Sorceress", "Yondu", "Hand Sentry", "Mordo", "Hand Assassin", "Ronan The Accuser", "Doctor Strange", "Scarlet Witch", "Loki", 
								"Black Panther", "Nobu", "Juggernaut", "M'Baku", "Thanos", "Thor", "Ultimus"):
			resultList.append("MYSTIC")
		elif traitsAsTuples[i] == ("Punisher", "Night Nurse", "SHIELD Medic", "Bullseye", "SHIELD Assault", "Hawkeye", "Hand Archer", "Hydra Scientist", "Mercenary Soldier", "Hand Blademaster", 
								"Kingpin", "Killmonger", "Mercenary Riot Guard", "SHIELD Operative", "SHIELD Security", "AIM Researcher", "SHIELD Trooper", "Black Widow", "Gamora", "Nick Fury"):
			resultList.append("SKILL")
		elif traitsAsTuples[i] == ("Deadpool", "Wolverine", "Cable", "Pyro", "Storm", "Mystique", "Sabretooth", "Magneto"):
			resultList.append("MUTANT")
		elif traitsAsTuples[i] == ("Punisher", "Bullseye", "Hydra Sniper", "SHIELD Assault", "Hydra Rifle Trooper", "Cable", "Korath The Pursuer", "Pyro", "Mercenary Sniper", "Hand Archer", 
								"Mercenary Soldier", "Ravager Boomer", "Killmonger", "SHIELD Trooper", "Rocket Raccoon", "War Machine", "Kree Cyborg", "Winter Soldier", "Hydra Grenadier", 
								"AIM Assaulter", "Wasp", "Green Goblin", "Iron Man", "Thor", "Ultron"):
			resultList.append("BLASTER")
		elif traitsAsTuples[i] == ("Daredevil", "Iron Fist", "Deadpool", "Elektra", "Spider-Man", "Wolverine", "Ms. Marvel", "Captain Marvel", "Nebula", "Hand Blademaster", "Kree Reaper", "Gamora", 
								"AIM Monstrosity", "Spider-Man [Miles]", "Sabretooth", "Black Panther", "Carnage", "Ultimus"):
			resultList.append("BRAWLER")
		elif traitsAsTuples[i] == ("Jessica Jones", "Mordo", "Hawkeye", "Kree Noble", "Hand Assassin", "Storm", "Vision", "Quake", "Black Widow", "Ronan The Accuser", "Venom", "AIM Infector", 
								"Ant-Man", "Mystique", "Scarlet Witch", "Mantis", "Loki", "Nobu", "Magneto", "Star-Lord"):
			resultList.append("CONTROLLER")
		elif traitsAsTuples[i] == ("Luke Cage", "Captain America", "Crossbones", "Hand Sentry", "Hulk", "AIM Security", "Ravager Bruiser", "Kingpin", "Drax", "Mercenary Riot Guard", 
								"SHIELD Security", "Kree Royal Guard", "Hydra Armored Guard", "Juggernaut", "M'Baku", "Thanos"):
			resultList.append("PROTECTOR")
		elif traitsAsTuples[i] == ("Hand Sorceress", "Yondu", "Night Nurse", "SHIELD Medic", "Ravager Stitcher", "Hydra Scientist", "Minn-Erva", "Kree Oracle", "SHIELD Operative", "AIM Researcher", 
								"Mercenary Lieutenant", "Groot", "Scientist Supreme", "Doctor Strange", "Nick Fury"):
			resultList.append("SUPPORT")
		elif traitsAsTuples[i] == ("AIM Security", "AIM Researcher", "Scientist Supreme", "AIM Monstrosity", "AIM Infector", "AIM Assaulter"):
			resultList.append("AIM")
		elif traitsAsTuples[i] == ("Loki", "Thor"):
			resultList.append("ASGARDIAN")
		elif traitsAsTuples[i] == ("Captain America", "Hulk", "Hawkeye", "Vision", "Black Widow", "War Machine", "Ant-Man", "Scarlet Witch", "Black Panther", "Iron Man", "Nick Fury", "Thor"):
			resultList.append("AVENGER")
		elif traitsAsTuples[i] == ("Pyro", "Mystique", "Sabretooth", "Juggernaut", "Magneto"):
			resultList.append("BROTHERHOOD")
		elif traitsAsTuples[i] == ("Daredevil", "Iron Fist", "Luke Cage", "Jessica Jones"):
			resultList.append("DEFENDER")
		elif traitsAsTuples[i] == ("Drax", "Rocket Raccoon", "Groot", "Gamora", "Mantis", "Star-Lord"):
			resultList.append("GUARDIAN")
		elif traitsAsTuples[i] == ("Elektra", "Hand Sorceress", "Hand Sentry", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Nobu"):
			resultList.append("HAND")
		elif traitsAsTuples[i] == ("Crossbones", "Hydra Sniper", "Hydra Rifle Trooper", "Hydra Scientist", "Hydra Armored Guard", "Winter Soldier", "Hydra Grenadier"):
			resultList.append("HYDRA")
		elif traitsAsTuples[i] == ("Captain Marvel", "Korath The Pursuer", "Kree Noble", "Minn-Erva", "Kree Oracle", "Kree Reaper", "Kree Royal Guard", "Ronan The Accuser", "Kree Cyborg", "Ultimus"):
			resultList.append("KREE")
		elif traitsAsTuples[i] == ("Deadpool", "Bullseye", "Korath The Pursuer", "Mercenary Sniper", "Mercenary Soldier", "Killmonger", "Mercenary Riot Guard", "Mercenary Lieutenant"):
			resultList.append("MERCENARY")
		elif traitsAsTuples[i] == ("Captain America", "Captain Marvel", "War Machine", "Winter Soldier"):
			resultList.append("MILITARY")
		elif traitsAsTuples[i] == ("Yondu", "Ravager Stitcher", "Ravager Boomer", "Ravager Bruiser"):
			resultList.append("RAVAGER")
		elif traitsAsTuples[i] == ("Captain America", "SHIELD Medic", "SHIELD Assault", "Hawkeye", "SHIELD Operative", "SHIELD Security", "Quake", "SHIELD Trooper", "Black Widow", "Nick Fury"):
			resultList.append("SHIELD")
		elif traitsAsTuples[i] == ("Spider-Man", "Venom", "Spider-Man [Miles]", "Green Goblin", "Carnage"):
			resultList.append("SPIDERVERSE")
		elif traitsAsTuples[i] == ("Killmonger", "Black Panther", "M'Baku"):
			resultList.append("WAKANDAN")
		elif traitsAsTuples[i] == ("Wolverine", "Storm"):
			resultList.append("XMEN")
		elif traitsAsTuples[i] == ("Deadpool", "Cable"):
			resultList.append("XFORCE")
		elif traitsAsTuples[i] == ("Hand Sorceress", "Hand Sentry", "SHIELD Medic", "Hydra Sniper", "SHIELD Assault", "Ravager Stitcher", "Hydra Rifle Trooper", "AIM Security", "Kree Noble", 
								"Mercenary Sniper", "Hand Archer", "Hand Assassin", "Hydra Scientist", "Mercenary Soldier", "Ravager Boomer", "Ravager Bruiser", "Hand Blademaster", "Kree Oracle", 
								"Mercenary Riot Guard", "SHIELD Operative", "SHIELD Security", "Kree Reaper", "AIM Researcher", "Kree Royal Guard", "Mercenary Lieutenant", "SHIELD Trooper", 
								"Hydra Armored Guard", "AIM Monstrosity", "Kree Cyborg", "AIM Infector", "Hydra Grenadier", "AIM Assaulter"):
			resultList.append("MINION")
		elif traitsAsTuples[i] == ("Ms. Marvel", "Quake"):
			resultList.append("INHUMAN")
		elif traitsAsTuples[i] == ("Thanos", "Ultimus"):
			resultList.append("ETERNAL")
		elif traitsAsTuples[i] == ("Daredevil", "Iron Fist", "Elektra", "Hand Sorceress", "Hand Sentry", "Mordo", "Hand Archer", "Hand Assassin", "Hand Blademaster", "Nobu"):
			resultList.append("MARTIALARTIST")
	return resultList

# Function to test anything:
def testerFunction():
	global HERO, VILLAIN
	print(len(HERO) + len(VILLAIN))

def main():
	# Importing global variables:
	global HERO, VILLAIN, CITY, GLOBAL, COSMIC, TECH, BIO, MYSTIC, SKILL, MUTANT, BLASTER, BRAWLER, SUPPORT, CONTROLLER, PROTECTOR, SUPPORT, MINION, INHUMAN, MARTIALARTIST
	global AIM, ASGARDIAN, AVENGER, BROTHERHOOD, DEFENDER, GUARDIAN, HAND, HYDRA, KREE, MERCENARY, MILITARY, RAVAGER, SHIELD, SPIDERVERSE, WAKANDAN, XMEN, XFORCE, ETERNAL
	global wantToContinue#, writtenOnce

	print("==========") # Used through the code to make the output more readible, by seperating the parts.
	if not wantToContinue: #  If the user run the program once and then decides to continue at the end of the first run, "wantToContinue" variable will be set as true
						   # and thus this "Main screen informations" part will be skipped.
		# Main screen informations:
		mainScreenInfo()

	try:
		# Taking the number of traits that user wants to intersect and giving it to the "howManyTraits" variable:
		howManyTraits = int(input(" How many traits will you intersect?: "))
	except:
		print(" !!! INVALID INPUT !!! ONLY NUMBER INPUTS ARE ALLOWED !!!")
		sys.exit()

	if not wantToContinue: #  Again if the user run the program once and then decides to continue at the end of the first run, "wantToContinue" variable will be set as true
						   # and thus this "Informing about format" part will be skipped.
		# Informing about format:
		informingAboutFormat()
		print("==========")

	try:
		# Now we will take the traits from user and append them to the "traitsAsTuples" list:
		#  Additionally when we take the inputs as "XMEN" etc. then evaluate it with "eval" (in order to be able to compare with our pre-defined traits' tuples)
		# the program sees it as tuples, so we name this variable like this. We will use "tuplesToTraits" function later in order to get their matched traits.
		traitsAsTuples = []
		for i in range(howManyTraits):
			trait = eval(input(" Type the trait, please: "))
			traitsAsTuples.append(trait)
	except:
		print(" !!! INVALID INPUT !!! PLEASE FOLLOW THE FORMAT RULES ABOVE !!!")
		sys.exit()

	try:
		print("==========")
		#  By sending our "traitsAsTuples" list (actually a list of tuples) to the function "findIntersection" we find out the intersected characters of the traits' tuples.
		# The function returns us a set, so we transform it into a list first, then sort, then assign it to the variable "heroesAsASortedList". Actually by this step we
		# find the very final and wanted list of characters.
		heroesAsASortedList = sorted(list(findIntersection(traitsAsTuples)))

		# Now we will get the actual trait names of the tuples by the help of "traitsAsTuples" function:
		willBePrinted = tuplesToTraits(traitsAsTuples)
		
		# If there is no intersection between wanted traits, do the followings:
		if heroesAsASortedList == []:
			file = open("result.txt", "w")
			file.write("There are no such characters!")
			file.close()
			print("	There are no such characters!")
			print(" Press \"C\" to keep discovering or any key to exit...")
			check = input()
			if check == "C" or check == "c":
				wantToContinue = True
				main()
			else: sys.exit()

		# We are making the following modifications in order to make the output more meaningful and to be able to write it to the "result.txt" file:

		willBePrinted.insert(0, "List of \"")
		willBePrinted.append("\" characters:")
		wantedTraitsAsAString = " ".join(willBePrinted)
		
		file = open("result.txt", "w")
		#if writtenOnce: file.write("\n\n")
		file.writelines(wantedTraitsAsAString)
		print(wantedTraitsAsAString)
		
		for i in range(len(heroesAsASortedList)):
			file.write("\n")
			file.write("	")
			file.write(heroesAsASortedList[i])
			print("	", heroesAsASortedList[i])
		
		#writtenOnce = True
		file.close()
		print("==========")
		
		print(" Press \"C\" to keep discovering or any key to exit...")
		check = input()
		
		if check == "C" or check == "c":
			wantToContinue = True
			main()
	except Exception as e:
		print(e)
		sys.exit()

if __name__ == '__main__':
	main()
