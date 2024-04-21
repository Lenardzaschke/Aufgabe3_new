import json

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def estimate_max_hr(self):
        # Add your implementation here
        pass

    def save(self):
        data = self.__dict__
        with open('person.json', 'w') as file:
            json.dump(data, file)

class Experiment:
    def __init__(self, name, duration, location):
        self.name = name
        self.duration = duration
        self.location = location

    def save(self):
        data = self.__dict__
        with open('experiment.json', 'w') as file:
            json.dump(data, file)
            