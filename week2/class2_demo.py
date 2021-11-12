class Animal:
    hunger = 50

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self, greeting="Hey"):
        print(f"{greeting}, I'm {self.name} the {self.species}")


class Cat(Animal):
    hunger = 70
    max_purr_vol = 10 
    species = 'cat'

    def __init__(self, name):
        super().__init__(name, 'cat')

    def purr(self):
        print(f'{self.name} enfurs you!')
    
    def speak(self):
        super().speak("Meow")

doggo = Animal("doge", "dog")
cato = Cat("cato")
animals = [doggo, cato]
for animal in animals:
    animal.speak()