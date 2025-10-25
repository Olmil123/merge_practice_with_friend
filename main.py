class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f"{self.name} say: Gaf, has {self.age}")


anime = Animal("sasha", 16)
anime.say()
