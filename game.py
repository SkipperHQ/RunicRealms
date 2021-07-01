### PROJECT NAME: Adventure Game
### DATE STARTED: 4/21/2020
### AUTHOR: SkipperHQ

import random
import os
import sys

####### Preparatory Settings #######

# Hero Classes
class knight(object):
    health = 100
    attack = 10
    defence = 5
    magic = 0
    gold = 0

class tank(object):
    health = 100
    attack = 5
    defence = 10
    magic = 0
    gold = 0

class sage(object):
    health = 100
    attack = 2
    defence = 5
    magic = 10
    gold = 0

# Enemy Monsters
class imp(object):
    name = "Imp"
    health = 10
    attack = 3
    defence = 3
    loot = random.randint(0,2)

class goblin(object):
    name = "Goblin"
    health = 10
    attack = 4
    defence = 4
    loot = random.randint(0,2)

class wolf(object):
    name = "Wolf"
    health = 20
    attack = 5
    defence = 5
    loot = random.randint(0,3)

class skeleton(object):
    name = "Skeleton"
    health = 20
    attack = 7
    defence = 6
    loot = random.randint(0,2)

###################################

def main():
    print("1) New Game\n2) Load Game\n3) Option\n4) Exit Game\n")
    option = input("> ")
    if option == "1":
        global character
        character = heroSelect()
    elif option == "2":
        # Load Game Function
        pass
    elif option == "3":
        # Option Function
        pass
    elif option == "4":
        sys.exit()
        pass
    else:
        print("Character Unavailable!\nOnly Use Characters: 1, 2, 3, or 4.\n")
        main()
        
def heroSelect():
    print("What is your name, adventurer?")
    global characterName
    characterName = input("> ")
    if len(characterName) < 3:
        print("Name is too Short (3 or more Characters)")
        heroSelect()
    else:
        print("Welcome to this magical world, " + characterName.title() + "!\n")
        print("Select your Hero's Class!\n1) Knight\n2) Tank\n3) Sage\n")
        option = input("> ")
        if option == "1":
            character = knight
            print("You have selected the Knight Class!\nThese are your Stats:")
            print("Health -", character.health)
            print("Attack -", character.attack)
            print("Defence -", character.defence)
            print("Magic -", character.magic)
            print("Starting Gold -", character.gold)
            return character

        elif option == "2":
            character = tank
            print("You have selected the Tank Class!\nThese are your Stats:")
            print("Health -", character.health)
            print("Attack -", character.attack)
            print("Defence -", character.defence)
            print("Magic -", character.magic)
            print("Starting Gold -", character.gold)
            adventureMenu()

        elif option == "3":
            character = sage
            print("You have selected the Sage Class!\nThese are your Stats:")
            print("Health -", character.health)
            print("Attack -", character.attack)
            print("Defence -", character.defence)
            print("Magic -", character.magic)
            print("Starting Gold -", character.gold)
            adventureMenu()

        else:
            print("Invalid Character!\nPlease enter either 1, 2, or 3.")
            heroSelect()

def adventureMenu():
    print("Adventure Menu!\n\nType a Number to Navigate:\n1) Fight\n2) Bag\n3) Shop\n4) Journal\n5) Options\n6) Exit Game\n\n")
    option = input("> ")
    
    if option == "1":
        battleState()
    elif option == "2":
        lootManager.bag(self)
    elif option == "3":
        #Shop
        pass
    elif option == "4":
        #Journal
        pass
    elif option == "5":
        #Options
        pass
    elif option == "6":
        sys.exit()
    else:
        print("Character Unavailable!\nPlease only use characters: 1, 2, 3, 4, 5, or 6.")
        adventureMenu()
        
def enemySelect(imp,goblin,wolf,skeleton):
    enemyList = [imp, goblin, wolf, skeleton]
    enemyChance = random.randint(0,3)
    enemy = enemyList[enemyChance]
    return enemy

class lootManager:

    global rng
    
    def __init__(self):
        self.lootDrop = 0
        self.playerInventory = []
        self.bagSize = 6

    def rng():
        loot = ['Sword', 'Shield', 'Potion of Life', 'Minor Potion of Life', 'Major Potion of Life']
        lootChance = random.randint(0,4)
        self.lootDrop = loot[lootChance]
        return self.lootDrop

    def lootToBag(self):
        # Currently this doesn't work as intended, self.bagSize starts counting at 0, meaning that currently, the bagSize has a cap of 7.
        if len(self.playerInventory) > self.bagSize:
            print("Inventory Full! Item has been dropped!\nUpgrade your Bag to solve this.")
        else: 
            print(self.playerInventory)
            self.playerInventory.append(self.lootDrop)
            print(self.playerInventory)
        

    def bag(self):
        print("Bag & Character Menu:")
        print("")
        
        print("Character Information:")
        print("Character Name -", characterName.title())
        print("Health Points -", int(character.health), "\nAttack -", character.attack, "\nDefence -", character.defence, "\nMagic -", character.magic, "\n")

        print("\nInventory:\nGold Pieces -", character.gold)
        print("Bag Size:", self.bagSize)

        if len(self.playerInventory) <= 0:
            print("No Items In Inventory")
        else:
            for item in self.playerInventory:
                print("-", item)
        
self = lootManager()

def battleState():
    # Enemy is selected.
    enemy = enemySelect(imp,goblin,wolf,skeleton)
    print("A", enemy.name, "has leapt toward you from a bush nearby.")
    #Gives player a choice of which action they'd like to take.
    print("What do you do?\nSelect a Character:\n\n1) Melee Attack\n2) Magic Attack\n3) Bag\n4) Journal\n5) Exit Game\n")
    while enemy.health > 0:
        option = input("> ")
        # Melee Attack
        if option == "1":
            print("You swing your sword toward the " + enemy.name + "!")
            if enemy.health > 0:
                character.health = character.health - (enemy.attack / character.attack)
                print("The", enemy.name, "takes a swing, it hits you leaving", int(character.health), "remaining health points.")
            # Beginning of hitChance, decides whether or not player's hit connects or they stagger and miss.
            hitChance = random.randint(0,4)
            if hitChance < 1:
                print("")
                print("You stagger, your sword slips from your hand and you lose your balance.")
                print("You struggle to, but finally regain your balance.")
                print("You look toward the", enemy.name, "and notice that it's charging toward you at a fast speed.")
                      
                # Beginning of staggerChance, decides whether or not the player gets hit following their stagger.
                staggerChance = random.randint(0,2)
                if staggerChance < 2:
                    print("You try to pull your sword up to block the attack, but don't have the time to do so.")
                    print("The", enemy.name, "hits you for full damage.")
                    character.health = character.health - (enemy.attack / character.defence)
                    print("Following the " + enemy.name + "'s attack, you are left with", int(character.health), "points of life remaining.")
                    print("\n1) Melee Attack,\n2) Magic Attack\n3) Bag\n4) Journal\n5) Exit Game\n")

                # Should staggerChance return with 0 or 1, the following code will execute.
                else:
                    print("You pull your sword up to meet the " + enemy.name + "'s sword, as they connect, a loud clang calls out.")
                    print("\n1) Melee Attack,\n2) Magic Attack\n3) Bag\n4) Journal\n5) Exit Game\n")
                    
            # If hitChance returns with 1, 2, 3, or 4, the code below will execute and launch an attack on the enemy.
            else:
                print("The sword connects with the " + enemy.name + "'s flesh, as you hit it, it unleashes a scream in its agony.")
                enemy.health = enemy.health - (character.attack - enemy.defence)
                print("The", enemy.name, "is left with", int(enemy.health), "life points.")
                print("\n1) Melee Attack,\n2) Magic Attack\n3) Bag\n4) Journal\n5) Exit Game\n")

                if enemy.health <= 0:
                    print("You have killed the", enemy.name)
                    print("You move the " + enemy.name + "'s lifeless carcass aside looking for loot.")
                    self.lootDrop = rng()
                    lootPossibility = random.randint(0,1)
                    
                    if lootPossibility == 0:
                        print("Underneith the carcass, you find a", self.lootDrop, "you tuck it away into your bag.")
                        lootManager.lootToBag(self)
                        print("")
                        
                    else:
                        print("Unfortunately, you found nothing of value.")
                        print("")
                        
                    #goldDrop here
                    if enemy.name == "Imp":
                        enemy.health = 10
                        adventureMenu()
                    elif enemy.name == "Goblin":
                        enemy.health = 10
                        adventureMenu()
                    elif enemy.name == "Wolf":
                        enemy.health = 20
                        adventureMenu()
                    elif enemy.name == "Skeleton":
                        enemy.health = 20
                        adventureMenu()
                    else:
                        print("ERROR GRAB: Enemy health replenishment not specified in battleState()")

        elif option == "2":
            pass
            # Magic Attack
            
        elif option == "3":
            # Bag
            lootManager.bag()

        elif option == "4":
            # Journal
            pass

        elif option == "5":
            # Exit Game
            sys.exit()

main()
adventureMenu()
