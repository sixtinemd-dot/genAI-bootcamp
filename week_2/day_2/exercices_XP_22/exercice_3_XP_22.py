from week_2.day_2.exercices_XP_22.exercices_XP import Dog 
import random

class PetDog(Dog):
    def __init__(self, name, age, weight):
        super().__init__(name, age, weight)
        self.trained = False

    def train(self):
        print(self.bark())
        self.trained = True

    def play(self, *dogs):
        names =[self.name]
        for dog in dogs:
            names.append(dog.name)
        names_str = ", ".join(names)
        print(f"{names_str} all play together")

    def do_a_trick(self):
         if self.trained:
            tricks = ["does a barrel roll", "stands on his back legs", "shakes your hand", "plays dead"]
            print(f"{self.name} {random.choice(tricks)}")
         else:
            print(f"{self.name} isn't trained... ")


dog1 = PetDog("Jazz", 14, 60)
dog2 = PetDog("Ginger", 9, 87)
dog3 = PetDog("Farofa", 3, 20)

dog1.train()
dog2.play(dog1, dog3)
dog3.do_a_trick()
dog1.do_a_trick()

