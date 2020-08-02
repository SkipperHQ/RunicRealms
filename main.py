####################################
# AUTHOR NAME: SkipperHQ
# PROJECT NAME: RunicRealms
# PROJECT STARTED: 29/07/2020
# PROJECT DESCRIPTION: RunicRealms is a text-based adventure RPG set in a medieval fantasy world, explore different areas, battle monsters, collect loot and craft different items with your monster drops.
####################################


###### Preparatory Settings ######

import random
import time
import os
import sys

# Hero Classes

class warrior(object):
    name = "Warrior"
    health = 25
    attack = 4
    defence = 2
    magic = 0

class tank(object):
    name = "Tank"
    health = 25
    attack = 2
    defence = 4
    magic = 0

class sage(object):
    name = "Sage"
    health = 20
    attack = 2
    defence = 2
    magic = 4

# Enemy Classes

class rabbit(object):
    name = "Rabbit"
    description = "You catch a glimpse of a rabbit hopping around in a nearby field"
    health = 4
    attack = 1
    defence = 0

class chicken(object):
    name = "Chicken"
    description = "A chicken runs out from behind a nearby tree"
    health = 4
    attack = 1
    defence = 0

class boar(object):
    name = "Boar"
    description = "A boar starts running toward you from a nearby tree"
    health = 6
    attack = 3
    defence = 1

class goblin(object):
    name = "Goblin"
    description = "A goblin tries to ambush you from a nearby rock"
    health = 8
    attack = 4
    defence = 1

class slime(object):
    name = "Slime"
    description = "A slime jumps down from the cave's rooftop infront of you"
    health = 6
    attack = 1
    defence = 3

class kobold(object):
    name = "Kobold"
    description = "You look ahead into a narrow cave system and see a kobold"
    health = 6
    attack = 3
    defence = 2
    

##### End of Preparatory Settings #####

def main():
    print("""
    
    ##############################################
    ###                                        ###
    ###     Welcome to                         ###
    ###                                        ###
    ###           RunicRealms                  ###
    ###                                        ###
    ### ====================================== ###
    ###      A Text-Based Adventure RPG        ###
    ##############################################
    
    """)

    print("Welcome to RunicRealms.!\nPlease use the numbers to the left of their respective options to navigate.\n1. New Game\n2. Load Game\n3. Options\n4. Exit Game")
    option = input("> ")
    if option == "1" or option.title() == "New":
        name()
    elif option == "2" or option.title() == "Load":
        # Load Game
        pass
    elif option == "3" or option.title() == "Options":
        # Options
        pass
    elif option == "4" or option.title() == "Exit" or option.title() == "Quit":
        sys.exit()
    else:
        print("Invalid selection, please use the characters 1, 2, 3, or 4 to navigate to their respective menus.")

def name():
    print("What is your name, adventurer? ")
    global characterName
    characterName = input("> ")
    if len(characterName) < 3:
        print("Invalid name, please use at least three characters.\n")
        name()

    else:
        print("Welcome to this magical world,", characterName.title(), "\n")
        classSelection()

def classSelection():
    global character
    print("Please select your class from those listed below:\n1. Warrior - High offense with medium defence and no magic.\n2. Tank - High defence with medium offense and no magic.\n3. Sage - High magic offense with medium defence and no melee offense.\nSelect your choice by typing the name of the class or '1', '2', or '3' respectively.\n")
    classSelectionInput = input("> ")
    if classSelectionInput == "1" or classSelectionInput.title() == "Warrior":
        character = warrior
        print("You have chosen the class 'Warrior', your starting attributes are: \nName:", characterName.title(), "\nClass:", character.name, "\nHealth:", character.health, "\nAttack:", character.attack, "\nDefence:", character.defence, "\nMagic:", character.magic, "\nDo you confirm this selection? (Y/N)")
        classSelectionInputConfirmation = input("> ")
        if classSelectionInputConfirmation.title() == "Y":
            print("You've chosen the Warrior Class, enjoy!")
            adventureMenu()
        elif classSelectionInputConfirmation.title() == "N":
            classSelection()
        else:
            print("Not a valid selection, returning to class selection.")
            classSelection()

        
    elif classSelectionInput == "2" or classSelectionInput.title() == "Tank":
        character = tank
        print("You have chosen the class 'Tank', your starting attributes are: \nName:", characterName.title(), "\nClass:", character.name, "\nHealth:", character.health, "\nAttack:", character.attack, "\nDefence:", character.defence, "\nMagic:", character.magic, "\nDo you confirm this selection? (Y/N)")
        classSelectionInputConfirmation = input("> ")
        if classSelectionInputConfirmation.title() == "Y":
            print("You've chosen the Tank Class, enjoy!")
            adventureMenu()
        elif classSelectionInputConfirmation.title() == "N":
            classSelection()
        else:
            print("Not a valid selection, returning to class selection.")
            classSelection()
        
    elif classSelectionInput == "3" or classSelectionInput.title() == "Sage":
        character = sage
        print("You have chosen the class 'Sage', your starting attributes are: \nName:", characterName.title(), "\nClass:", character.name, "\nHealth:", character.health, "\nAttack:", character.attack, "nDefence:", character.defence, "\nMagic:", character.magic, "\nDo you confirm this selection? (Y/N)")
        classSelectionInputConfirmation = input("> ")
        if classSelectionInputConfirmation.title() == "Y":
            print("You've chosen the Sage Class, enjoy!")
            adventureMenu()
        elif classSelectionInputConfirmation.title() == "N":
            classSelection()
        else:
            print("Not a valid selection, returning to class selection.\n")
            classSelection()

def adventureMenu():

    print("\nAdventure Menu: \nPlease navigate using the number to the left of the respective navigation option.\n1. Explore\n2. Bag\n3. Shop\n4. Journal\n5. Options\n6. Exit Game\n\n")
    adventureMenuInput = input("> ")
    if adventureMenuInput == "1" or adventureMenuInput.title() == "Explore":
        explore.exploreMenu(self)
    elif adventureMenuInput == "2" or adventureMenuInput.title() == "Bag":
        bag()
    elif adventureMenuInput == "3" or adventureMenuInput.title() == "Shop":
        pass
    elif adventureMenuInput == "4" or adventureMenuInput.title() == "Journal":
        pass
    elif adventureMenuInput == "5" or adventureMenuInput.title() == "Options":
        pass
    elif adventureMenuInput == "6" or adventureMenuInput.title() == "Exit":
        sys.exit()
    else:
        print("Invalid selection, please navigate using a number to the left of the respective navigation option.")
        adventureMenu()


class explore:

    def __init__(self):
        self.exploring = False
    
    def exploreMenu(self):
        print("Exploration Menu:\nChoose which location you'd like to explore from the list:\n1. Forest\n2. Cave\n")
        exploreMenuInput = input("> ")
        if exploreMenuInput == "1" or exploreMenuInput.title() == "Forest":
            self.exploring = 1
            self.exploreLocations(self)

        elif exploreMenuInput == "2" or exploreMenuInput.title() == "Cave":
            self.exploring = 2
            self.exploreLocations(self)

        else:
            print("Invalid Selection, please navigate using the number to the left of the respective navigation option.")
            exploreMenu(self)

    def exploreLocations(self):
        if self.exploring is not False:
            if self.exploring == 1:
                print("Forest.......")
                enemy = enemySelect()
                battleState()

            elif self.exploring == 2:
                print("Cave.......")
                enemy = enemySelect()
                battleState()

            else:
                print("Error exploreLocations")
        else:
            print("Error, exploreLocations.")


self = explore

def enemySelect():
    enemyList = []
    enemySelectionForest = [rabbit,chicken,boar]
    enemySelectionCave = [goblin,kobold,slime]
    if self.exploring == 1:
        enemyList = enemySelectionForest

    elif self.exploring == 2:
        enemyList = enemySelectionCave

    else:
        print("Error, see enemySelect(enemySelection)\nPress Enter to Continue...")
        input("> ")
        name()
        
    enemy = random.choice(enemyList)
    # enemy = enemyList[enemyChance]
    return enemy

def battleState():
    # Start of battleState's preparatory functions.
    def enemyKilled():
        if enemy.health <= 0:
            print("You have killed the", enemy.name, "you lift the corpse expectantly...")
            time.sleep(2)

            # enemy drop gold here

            lootChance = random.randint(0, 6)
            if lootChance == 0:
                # This is where the loot drops will go.
                pass
            else:
                print("Unfortunately, you found no loot under the corpse.\nWould you like to continue exploring or not?")

                if enemy.name == "Chicken" or enemy.name == "Rabbit":
                    enemy.health = 4
                elif enemy.name == "Boar" or enemy.name == "Kobold" or enemy.name == "Slime":
                    enemy.health = 6
                elif enemy.name == "Goblin":
                    enemy.health = 8

                option = input("> ")
                if option == "1" or option.title() == "Continue":
                    battleState()
                else:
                    adventureMenu()

    def gameOver():
        if character.health <= 0:
            print("Unfortunately, your health has fallen to zero, you are now dead.\nGame over, thank you for playing.")
            time.sleep(5)
            main()

    def combatAction():
        print("\nWhat do you do?\nSelect a following option to continue:\n1. Melee Attack\n2. Magic Attack (WIP)\n3. Run\n4. Bag\n5. Journal\n6. Options\n7. Exit Game")

    # End of battleState's preparatory functions.

    # Start of battleState
    # assigns enemy to the enemySelect() function.
    enemy = enemySelect()
    print(enemy.description)
    combatAction()

    while character.health > 0:
        userAction = input("> ")
        if userAction == "1" or userAction.title() == "Melee":
            if enemy.health > 0:
                character.health = character.health - (enemy.attack / character.defence)
                print("The", enemy.name, "attacks you, dealing damage to you.\nYou are now left with", int(character.health), "life points remaining.")
                print("You swing your weapon toward the", enemy.name)
                missChance = random.randint(0,10)
                if missChance <= 2:
                    print("You completely miss the " + enemy.name + ", you regain your balance.")
                    combatAction()
                else:
                    enemy.health = enemy.health - (character.attack - enemy.defence)
                    print("You attack the " + enemy.name + ", the "+ enemy.name + " is left with", int(enemy.health), "health points.")
                    combatAction()
                    enemyKilled()
            else:
                enemyKilled()


        else:
            print("Either incorrect selection or selection is not yet implemented.\nPress Enter to Continue...")
            input("> ")
            adventureMenu()

main()
