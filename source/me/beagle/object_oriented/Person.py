from me.beagle.object_oriented.Gender import Gender

class Person:
    name = ''
    age = 0
    gender = Gender.male

    def __init__(self, _name, _age, _gender=Gender):
        self.name = _name
        self.age = _age
        self.gender = _gender

