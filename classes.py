class Dog:
    kind = 'canine'         # class variable shared by all instances
    # you don't need an __init__ method, but it is common for stuff that runs at instantiaion

    def __init__(self, breed, age):
        self.breed = breed  # instance variable unique to each instance
        self.age = age
        self.tricks = []

    def addTrick(self, trick):
        self.tricks.append(trick)

    def bark(self):
        return 'arf'

Crosby = Dog("Golden", 8)
Charley = Dog("Pit Bull", 12)
Crosby.addTrick("roll over")
Charley.addTrick("sit")

print(Crosby.breed)
print(Crosby.age)
print(Charley.breed)
print(Charley.age)
print(Crosby.tricks)
print(Charley.tricks)

Charley.age += 1
Charley.weight = 70

print(Charley.age)
print(Charley.weight)
print(Charley.bark())