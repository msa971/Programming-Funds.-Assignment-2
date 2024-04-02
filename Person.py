from enum import Enum

class Gender(Enum):
    female = 'female'
    male = 'male'

class Person:
    """class to represent a person"""

    #constructor:
    def __init__(self, name, id, age, gender):
        #the attributes are private because not everyone needs to know this information about a person. Only the gender is public.
        self.__name = name
        self.__id = id
        self.__age = age
        self.gender = gender

    #setter getter functions:
    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def get_id(self):
        return self.__id

    def set_age(self, age):
        self.__age = age

    def get_age(self):
        return self.__age

    def set_gender(self, gender):
        self.gender = gender

    def get_gender(self):
        return self.gender