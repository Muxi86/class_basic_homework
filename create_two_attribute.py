#Create a "Person" class

#that has a name("name") and a age("age")
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        return f'Name:{self.name}, Age:{self.age}'