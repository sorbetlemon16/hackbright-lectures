class Animal:
    """ A living creature. """
    species = 'dog'

    def __init__(self, animal_name, animal_tail_length):
        self.name = animal_name
        self.tail_length = animal_tail_length

    def speak(self):
        print(self.name)
        #print(f'Woof! I am {self.name} the {self.species}')

    def graduate(self):
        self.name = f'Dr. {self.name}'
        self.speak()

fido = Animal('Fido', 'long')