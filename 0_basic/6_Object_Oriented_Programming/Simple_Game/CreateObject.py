class GameObject:
	class_name = "" # Subclass name
	desc = "" # Description of the subclass
	objects = {} # Void dictionary for store all the Subclass name

	def __init__(self, name):
		self.name = name
		GameObject.objects[self.class_name] = self

	def get_desc(self):
		return self.class_name + "\n" + self.desc

class Goblin(GameObject): # Define a subclass in the GameObject named Goblin
	class_name = "goblin"
	desc = "A foul creature"

goblin = Goblin("Gobbly")

def examine(noun): # For testing whether the Object is in the GameObject, return Description if it is True
	if noun in GameObject.objects:
		return GameObject.objects[noun].get_desc()
	else:
		return "There is no {} here.".format(noun)

def say(noun):
	return 'You said "{}"'.format(noun)

verb_dict = {
		"say": say,
		"examine": examine,
		}

def get_input():
	command = input(": ").split()
	verb_word = command[0]
	if verb_word in verb_dict:
		verb = verb_dict[verb_word]
	else:
		print("Unknown verb {}".format(verb_word))
		return 
	
	if len(command) >= 2:
		noun_word = command[1]
		print(verb(noun_word))
	else:
		print(verb("nothing"))

while True:
	get_input()


