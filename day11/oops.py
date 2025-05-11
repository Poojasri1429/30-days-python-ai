# class Dog:
#     def bark(self):
#         print("Woof! Woof!")

# my_dog = Dog()      # Creating an object
# my_dog.bark()       # Calling method


# class Dog:
#     def __init__(self, name):
#         self.name = name

#     def bark(self):
#         print(f"{self.name} says Woof!")

# my_dog = Dog("Bruno")
# my_dog.bark()


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show_details(self):
        print(f"Name: {self.name}, Age: {self.age}")

s1 = Student("Tara", 21)
s1.show_details()