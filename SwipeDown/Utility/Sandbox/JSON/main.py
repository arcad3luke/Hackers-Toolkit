# This file is from a YT tutorial @ https://www.youtube.com/watch?v=jABj-SEhtBc.
# This is more of a template than anything in case I get lost with JSON things.

import json


class Person:
    def __init__(self, name, age, weight):  # set the variables for json keys
        self.name = name
        self.age = age
        self.weight = weight

    def print_info(self):  # prints info
        print(self.name, self.age, self.weight)

    def get_older(self, years):  # Age incrementation
        self.age += years

    def save_to_json(self, filename):  # Save function
        person_dict = {'name': self.name, 'age': self.age, 'weight': self.weight}
        with open(filename, 'w') as f:
            f.write(json.dumps(person_dict, indent=2))

    def load_from_json(self, filename):  # Load function
        with open(filename, 'r') as f:
            data = json.loads(f.read())

            self.name = data['name']
            self.age = data['age']
            self.weight = data['weight']


# Call everything we need
p2 = Person(None, None, None)
p2.load_from_json('mike.json')
p2.print_info()
