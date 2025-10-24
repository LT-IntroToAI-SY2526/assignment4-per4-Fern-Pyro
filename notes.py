# object oriented programming

# (define-struct dog [fur_color name age favorite_food])

class Dog:
    """
    A simple Dog class to learn object oriented proggrammming (OOP) conepts

    Attributes:
        breed - the breed of the god
        fur_color - the fur color of the dog
        name - the name of the dog
        age - the age of the dog
    """
    def __init__(self, breed = "Dog", fur_color = "black", name = "no name", age = 1): #methods every class have, even if you don't define it
        """Intitialize a new Dog with breed, fur_color, name, and age"""
        self.breed = breed 
        self.fur_color = fur_color
        self.name = name
        self.age = age

    def __str__(self):
        """String representaion of a dog"""
        return f"{self.name} is a {self.age} year old {self.fur_color} {self.breed}"
    
    def bark(self):
        return f"{self.name} says: Woof, Woof"
    
    def birthday(self):
        """Celebrate the dog's birthday"""
        self.age += 1
        print(f"{self.name} is celebrating their {self.age} birthday!")

    def paint_dog(self, new_color):
        """Changes the fur_color of the dog"""
        old_color = self.fur_color
        self.fur_color = new_color
        print(f"{self.name} changed their fur color from {old_color} to {self.fur_color}")

if __name__ == "__main__":
    berg_dog = Dog("labrador", "black", "logan", 9)
    aidan_dog = Dog("lab pitt mix", "grey", "cubby", 9)
    default_dog = Dog()
    mattew_dog = Dog(breed = "labrador", name = "bella", age = 1)
    print(berg_dog)
    print(aidan_dog)
    print(default_dog)
    print(mattew_dog)
    
    print(berg_dog.bark())
    mattew_dog.birthday()
    berg_dog.paint_dog("neon green")

    print(berg_dog)