#Classes and Objects: Python allows you to define classes, which serve as blueprints for creating objects. Objects are instances of classes.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

person1 = Person("Alice", 30)
person2 = Person("Bob", 25)


#------------------------------------------------------------------------------------------------------------------------------------------------
#Inheritance: Python supports single and multiple inheritance, allowing a class to inherit attributes and methods from one or more parent classes.

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id


#---------------------------------------------------------------------------------------------------------------------------------------------------
#Encapsulation: Python uses public, protected, and private access modifiers through naming conventions (_ and __) to control access to class members.

class MyClass:
    def __init__(self):
        self._protected_var = 10  # Protected variable
        self.__private_var = 20  # Private variable

    def get_private_var(self):
        return self.__private_var


#---------------------------------------------------------------------------------------------------------------------------------------
#Polymorphism: Python supports polymorphism, allowing different classes to have methods with the same name but different implementations.

class Cat:
    def speak(self):
        return "Meow!"

class Dog:
    def speak(self):
        return "Woof!"

def animal_speak(animal):
    return animal.speak()

cat = Cat()
dog = Dog()
print(animal_speak(cat))  # "Meow!"
print(animal_speak(dog))  # "Woof!"


#---------------------------------------------------------------------------------------------------------------------------------------------
#Abstraction: Python allows you to define abstract base classes using the abc module, enforcing that derived classes implement certain methods.

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


#--------------------------------------------------------------------------------------
#Class in detail
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_age(self):
        return self.age

    def set_age(self, age):
        if age >= 0:
            self.age = age
        else:
            print("Age cannot be negative.")

    def introduce(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an instance of the Person class
person1 = Person("Alice", 30)

# Accessing and modifying attributes using methods
print("Initial Information:")
person1.introduce()

person1.set_name("Saif")
person1.set_age(22)

print("\nUpdated Information:")
person1.introduce()

# Attempting to set a negative age (will print an error message)
person1.set_age(-5)

