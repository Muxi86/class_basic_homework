#Create a "Person" class
#Create an attribute "name" in the "Person" class
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        return f'Name:{self.name}, Age:{self.age}'
        