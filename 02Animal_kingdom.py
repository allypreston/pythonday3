class Animal:

    animal_kind = "Cow"

    def speak(self):  # this is inside a class hence it is a method
        return 'what????????'

    def eat():
        return "yum yum yum"

    def drink(self):  # this is inside a class hence it is a method
        return 'slurp'

dog1 = Animal()  # now I have an object of type animal
cat = Animal()  # new animal

# how does do relate to other members
print(dog1.speak()) # object dog know's this because of having self
print(dog1.eat()) # object dog does not know this because of not having self

# print(Animal.speak()) # animal does not know this cause it doesn't have self
print(Animal.eat()) # animal does know this cause it does not have self



# print(dog1.animal_kind)
# dog1.animal_kind = "I'm a dog"
# print(dog1.animal_kind)
# print(Animal.animal_kind)
# Animal.animal_kind = "Mouse"
# print(dog1.animal_kind)
# dog3 = Animal()# other animal
# print(dog3.animal_kind)
# print(dog3.speak())
# print(Animal.speak())
