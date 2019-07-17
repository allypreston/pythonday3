class Dog:
    animal_kind = "Canine"

    def __init__(self, name):
        self.name = name

    def speak(self):
        return "woof"


dog1 = Dog("Charlie")
dog2 = Dog("Don")

print(dog1.name)
print(dog2.name)

# constructor - a method that is used automatically when a
# object is created to assign a variable property
