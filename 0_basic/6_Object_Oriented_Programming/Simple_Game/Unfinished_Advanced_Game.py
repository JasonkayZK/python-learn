# Create by Jasonkay

"""
Info:	The example from:
        	Python / OOP / 8: A Simple Game

History:	Jasonkay	2018/07/25	Second Release

File_Name:	Advanced_Game.py

Patch_1:
	Extended list of commands:
		"say": Let the character to say a sentence
		"examine": examine the Object in the Game, return the description of the given object while True
		"hit": Hit a monster in the game
		"quest": Quest a NPC

	Extended list of objects:
		"goblin":
		"orc":
		"human":
	
	Extended the UI:
		Now the terminal could show the player's command with number

For example:
>>> 
	say hi\n
	examine goblin\n
	hit goblin\n
	examine human\n
	quest human\n
	hit human\n

Warning:
		Please input the command form like:		verb noun

"""


## SUPERCLASS
class GameObject:
    class_name = ""  # Subclass name
    desc = ""  # Description of the subclass
    objects = {}  # Void dictionary for store all the Subclass name

    def __init__(self, name):
        self.name = name
        GameObject.objects[self.class_name] = self

    def get_desc(self):
        return self.class_name + ": " + self.desc


## Define a subclass named Goblin
class Goblin(GameObject):
    def __init__(self, name):
        self.class_name = "goblin"
        self.health = 3
        self._desc = "A foul creature"
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 3:
            return self._desc
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


## Define a subclass named Orc
class Orc(GameObject):
    def __init__(self, name):
        self.class_name = "orc"
        self.health = 5
        self._desc = "A powerful evil creature."
        super().__init__(name)

    @property
    def desc(self):
        if self.health >= 5:
            return self._desc
        elif self.health == 4:
            health_line = "Not even a scratch."
        elif self.health == 3:
            health_line = "You have broken its shield."
        elif self.health == 2:
            health_line = "It has a wound on its knee."
        elif self.health == 1:
            health_line = "Its left arm has been cut off!"
        elif self.health <= 0:
            health_line = "It is dead."
        return self._desc + "\n" + health_line

    @desc.setter
    def desc(self, value):
        self._desc = value


## Define a subclass named Human
class Human(GameObject):
    def __init__(self, name):
        self.class_name = "human"
        self._desc = "Just a regular human person like you."
        super().__init__(name)

    @property
    def desc(self):
        return self._desc

    @desc.setter
    def desc(self, value):
        self._desc = value


## Input function to interpret the list of commands
def get_input():
    user_input = ""
    # while True:
    # 	try:
    # user_input = user_input +
