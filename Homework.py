class Dog:

    age = 10

    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

Alec = Dog("Alec", "Golden Retreiver")
Jonathan = Dog("Jonathan", "Labrador")

print("Jonathan and Alec's age is ", (Alec.age) )
print("{} is the {} breed".format(Alec.name, Alec.breed))
print("{} is the {} breed".format(Jonathan.name, Jonathan.breed))

        