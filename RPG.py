#  File: RPG.py
#  Description:
#  Student's Name: Logan Hashmi
#  Student's UT EID: Sah4334
#  Course Name: CS 313E
#  Unique Number: 51465
#  Date Created: 9/15/17
#  Date Last Modified: 9/20/17


# initiated Weapon class which updates weapon and weapondamage based on the type of weapon
class Weapon():
    def __init__(self, weapon):
        if weapon == "dagger":
            self.weapon = weapon
            self.weapondamage = 4
        elif weapon == "axe":
            self.weapon = weapon
            self.weapondamage = 6
        elif weapon == "staff":
            self.weapon = weapon
            self.weapondamage = 6
        elif weapon == "sword":
            self.weapon = weapon
            self.weapondamage = 10
        elif weapon == "none":
            self.weapon = weapon
            self.weapondamage = 1

    # returns the name of the weapon instead of the address whenever the print function is called
    def __str__(self):
        return self.weapon


# initiated a Armor class which updates the players armor and armor class based on the type of armor
class Armor():
    def __init__(self, armor_type):
        if armor_type == "plate":
            self.armor = armor_type
            self.AC = 2
        elif armor_type == "chain":
            self.armor = armor_type
            self.AC = 5
        elif armor_type == "leather":
            self.armor = armor_type
            self.AC = 8
        elif armor_type == "none":
            self.armor = armor_type
            self.AC = 10

    # returns the name of the armor instead of the address whenever the print function is called
    def __str__(self):
        return self.armor


# create a main class which initiates players at the start of the game
class RPGCharacters():
    # all players created will have these features
    def __init__(self, name):
        self.name = name
        self.weapon = "none"
        self.armor = "none"
        self.AC = 10
        self.weapondamage = 1

    # this fight method takes an object(opponent) and initiates a fight
    def fight(self, opponent):
        print("{} attacks {} with a(n) {}".format(self.name, opponent.name, self.weapon))

        # updates the health of the opponent after the attack
        opponent.health -= self.weapondamage

        # prints out the results of the attack
        print("{} does {} damage to {}".format(self.name, self.weapondamage, opponent.name))
        print("{} is now down to {} health".format(opponent.name, opponent.health))

        # checks to see if the opponents health is down to zero
        self.checkForDefeat(opponent)

    # this methods takes a weapon object and equips players with the weapon to fight with
    def wield(self, weapon):
        # assigns the player with the weapon called and how much damage it can cause
        if self.wield_weapon:
            self.weapon = weapon
            self.weapondamage = weapon.weapondamage

            # prints out what the player is wielding
            print("{} is now wielding a(n) {}".format(self.name, self.weapon))

        # this if statement checks to see if the player is a wizard because wizards have some restrictions
        elif self.charactertype == "Wizard":

            # checks to see if the weapons are only a staff or dagger before assigning it to the player
            if weapon.weapon == "staff" or weapon.weapon == "dagger":
                self.weapon = weapon
                self.weapondamage = weapon.weapondamage

                print("{} is now wielding a(n) {}".format(self.name, self.weapon))
            else:
                # if it is anything other than those two weapons the player is not allowed to wield it
                print("Weapon not allowed for this character class.")

    # removes the weapon held be the player and sets default settings
    def unwield(self):
        self.weapon = "none"
        self.weapondamage = 1
        print("{} is no longer wielding anything.".format(self.name))

    # this method checks to see if the players health is high enough to continue the battle
    def checkForDefeat(self, opponent):
        # if it's less than 0 then the player is defeated and game ends
        if opponent.health <= 0:
            print("{} has been defeated!".format(opponent.name))

    # prints out the players status in a particular format
    def __str__(self):
        return (str(self.name) + "\n" + "  Current Health: " + str(self.health) + "\n"
                + "  Current Spell Points: " + str(self.spell) + "\n"
                + "  Wielding: " + str(self.weapon) + "\n" + "  Wearing: " + str(self.armor) + "\n" +
                "  Armor Class: " + str(self.AC))


# this is a subclass of the RPGCharacters which are for Fighters
class Fighter(RPGCharacters):
    # default settings for fighters
    health = 40
    spell = 0
    allow_armor = True
    wield_weapon = True
    use_magic = False
    charactertype = "Fighter"

    # this method checks to see if the player is a fighter and assigns it the armor
    def putOnArmor(self, new_armor):
        if self.charactertype == "Fighter":
            self.armor = new_armor
            self.AC = new_armor.AC
            print("{} is now wearing {}".format(self.name, self.armor))
        else:
            print("Armor not allowed for this character class.")

    # removes the armor from the fighter and sets default setting
    def takeOffArmor(self):
        self.armor = "none"
        self.AC = 10
        print("{} is no longer wearing anything.".format(self.name))


# this subclass is created for wizard type players
class Wizard(RPGCharacters):
    # default settings
    allowed_armor = False
    wield_weapon = False
    health = 16
    spell = 20
    charactertype = "Wizard"

    # this method detects which spell was cast and update the players status
    def castSpell(self, spell, opponent):
        print("{} cast {} at {}".format(self.name, spell, opponent.name))

        # checks to see which spell was cast and deducts points from the opponent
        if spell == "Fireball":
            # checks if the wizard has enough spellcast points to perform this spell
            if self.spell < 3:
                print("Insufficient spell points.")
            else:
                # subtracts damage from the oppoints health and wizards spellcast
                self.spell -= 3
                opponent.health -= 5

                # prints out the results
                print("{} does 5 damage to {}".format(self.name, opponent.name))
                print("{} is now down to {} health".format(opponent.name, opponent.health))

                self.checkForDefeat(opponent)
        elif spell == "Lightning Bolt":
            if self.spell < 10:
                print("Insufficient spell points.")
            else:
                self.spell -= 10
                opponent.health -= 10

                print("{} does 10 damage to {}".format(self.name, opponent.name))

                print("{} is now down to {} health".format(opponent.name, opponent.health))

                self.checkForDefeat(opponent)

        elif spell == "Heal":
            if self.spell < 6:
                print("Insufficient spell points.")
            else:
                # prevents the oppoant's health from surpassing the default settings
                if opponent.health + 6 > 16 or opponent.health + 6 > 40:
                    pass
                else:
                    # adds health points and deducts spellcast points and prints out the results
                    self.spell -= 6
                    opponent.health += 6
                    print("{} heals {} for 6 health points".format(self.name, opponent.name))
                    print("{} is now at {} health".format(opponent.name, opponent.health))
        else:
            # does nothing if a random spells was casts
            print("Unknown spell name. Spell failed")


def main():
    plateMail = Armor("plate")
    chainMail = Armor("chain")
    sword = Weapon("sword")
    staff = Weapon("staff")
    axe = Weapon("axe")
    dagger = Weapon("dagger")

    gandalf = Wizard("Gandalf the Grey")
    gandalf.wield(staff)

    aragorn = Fighter("Aragorn")
    aragorn.putOnArmor(plateMail)
    aragorn.wield(axe)

    print()
    print(gandalf)

    print()
    print(aragorn)
    print()

    gandalf.castSpell("Fireball", aragorn)
    aragorn.fight(gandalf)

    print()
    print(gandalf)

    print()
    print(aragorn)
    print()
    gandalf.castSpell("Lightning Bolt", aragorn)
    aragorn.wield(sword)
    print()

    print(gandalf)
    print()
    print(aragorn)

    print()

    gandalf.castSpell("Heal", gandalf)
    aragorn.fight(gandalf)

    gandalf.fight(aragorn)
    aragorn.fight(gandalf)
    print()
    print(gandalf)
    print()
    print(aragorn)


main()
