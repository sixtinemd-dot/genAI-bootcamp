""" Daily challenge: Old MacDonald’s Farm

Instructions: Old MacDonald’s Farm
You are given example code and output. Your task is to create a Farm class that produces the same output. """

class Farm:
    def __init__(self, farm_name):
        self.name = farm_name
        self.animals = {}

    def add_animal(self, animal_type, count = 1):
        if animal_type in self.animals:
            self.animals[animal_type] += count
        else:
            self.animals[animal_type] = count

    def get_info(self):
        info = self.name + "\n\n"
        for animal_type,count in self.animals.items():
            info += f"{animal_type} : {count}\n"
        info += "\nE-I-E-I-O!"
        return info
    
    # Bonus: Expand The Farm
""" 
    def get_animal_type(self): 
        return sorted(list(self.animals.keys()))

    def get_short_info(self):
        self.get_animal_type()
        animal_list = []
        for animal_type in self.get_animal_type():
            if  > 1:
                animal_type +="s"
            else:
                pass
            
        print(f"{self.name}'s farm has")
         """


macdonald = Farm("McDonald")
macdonald.add_animal('cow', 5)
macdonald.add_animal('sheep')
macdonald.add_animal('sheep')
macdonald.add_animal('goat', 12)
print(macdonald.get_info())

# Bonus: Expand The Farm

""" macdonald.get_animal_type()
macdonald.get_short_info() """



    