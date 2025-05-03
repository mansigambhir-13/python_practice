# # # # class dog :
# # # #     species = "canine"

# # # #     def __init__(self, name, age) :
# # # #         self.name = name
# # # #         self.age = age

# # # # #create an object from the class
# # # # dog1 = dog()
# # # # print(dog1.sound)   


# # # # class Dog:
# # # #     species = "Canine"  # Class attribute

# # # #     def __init__(self, name, age):
# # # #         self.name = name  # Instance attribute
# # # #         self.age = age  # Instance attribute


# # # # class Dog:
# # # #     species = "Canine"  # Class attribute

# # # #     def __init__(self, name, age):
# # # #         self.name = name  # Instance attribute
# # # #         self.age = age  # Instance attribute

# # # # # Creating an object of the Dog class
# # # # dog1 = Dog("Buddy", 3)

# # # # print(dog1.name)  # Output: Buddy
# # # # print(dog1.species)  # Output: Canine
# # # # print(dog1.age)  # Output: 3


# # # # class Dog:
# # # #     def __init__(self, name, age):  
# # # #         self.name = name 
# # # #         self.age = age

# # # #     def bark(self): 
# # # #         print(f"{self.name} is barking!")

# # # # # Creating an instance of Dog
# # # # dog1 = Dog("Buddy", 3)
# # # # dog1.bark() 


# # # # # Creating another instance of Dog
# # # # dog2 = Dog("Max", 5)    



# # # class dog :
# # #     species = "canine"

# # #     def __init__(self, name, age) :
# # #         self.name = name
# # #         self.age = age

# # #     def __str__(self) :
# # #         return f"{self.name} is {self.age} years old."  
    
# # #     dog1=Dog("dog1", 2) 
# # #     dog2=Dog("dog2", 3)


# # #     print(dog1)
# # #     print(dog2) 


# # # class Dog:
# # #     # Class variable
# # #     species = "Canine"

# # #     def __init__(self, name, age):
# # #         # Instance variables
# # #         self.name = name
# # #         self.age = age

# # # # Create objects
# # # dog1 = Dog("Buddy", 3)
# # # dog2 = Dog("Charlie", 5)

# # # # Access class and instance variables
# # # print(dog1.species)  # (Class variable)
# # # print(dog1.name)     # (Instance variable)
# # # print(dog2.name)     # (Instance variable)

# # # # Modify instance variables
# # # dog1.name = "Max"
# # # print(dog1.name)     # (Updated instance variable)

# # # # Modify class variable
# # # Dog.species = "Feline"
# # # print(dog1.species)  # (Updated class variable)
# # # print(dog2.species)  



# # # class complex:
# # #     def __init__(self, real, imag):
# # #         self.real = real
# # #         self.imag = imag

# # #     def __str__(self):
# # #         return f"{self.real} + {self.imag}i" 
# # #     print("Complex number:", c1)  # Output: Complex number: 3 + 4i
# # #     print("Complex number:", c2)  # Output: Complex number: 5 + 6i   


# # # 

# # # Single Inheritance
# # class Dog:
# #     def __init__(self, name):
# #         self.name = name

# #     def display_name(self):
# #         print(f"Dog's Name: {self.name}")

# # class Labrador(Dog):  # Single Inheritance
# #     def sound(self):
# #         print("Labrador woofs")

# # # Multilevel Inheritance
# # class GuideDog(Labrador):  # Multilevel Inheritance
# #     def guide(self):
# #         print(f"{self.name}Guides the way!")

# # # Multiple Inheritance
# # class Friendly:
# #     def greet(self):
# #         print("Friendly!")

# # class GoldenRetriever(Dog, Friendly):  # Multiple Inheritance
# #     def sound(self):
# #         print("Golden Retriever Barks")

# # # Example Usage
# # lab = Labrador("Buddy")
# # lab.display_name()
# # lab.sound()

# # guide_dog = GuideDog("Max")
# # guide_dog.display_name()
# # guide_dog.guide()

# # retriever = GoldenRetriever("Charlie")
# # retriever.display_name()
# # retriever.greet()
# # retriever.sound()

# class Dog:
#     def __init__(self, name, breed, age):
#         self.name = name  # Public attribute
#         self._breed = breed  # Protected attribute
#         self.__age = age  # Private attribute

#     # Public method
#     def get_info(self):
#         return f"Name: {self.name}, Breed: {self._breed}, Age: {self.__age}"

#     # Getter and Setter for private attribute
#     def get_age(self):
#         return self.__age

#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Invalid age!")

# # Example Usage
# dog = Dog("Buddy", "Labrador", 3)

# # Accessing public member
# print(dog.name)  # Accessible

# # Accessing protected member
# print(dog._breed)  # Accessible but discouraged outside the class

# # Accessing private member using getter
# print(dog.get_age())

# # Modifying private member using setter
# dog.set_age(5)
# print(dog.get_info())


class Counter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

    def get_count(self):
        return self.count

# using the Counter class
counter = Counter()
counter.increment()
counter.increment()
counter.decrement()
print(counter.get_count())
