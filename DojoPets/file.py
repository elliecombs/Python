from pet import Pet

class Ninja:
    def __init__(self,first_name,last_name,pet,treats):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet 
        self.treats = treats 
        self.pet_food = 80 

    def walk (self):
        self.pet.play()
        return self
    
    def feed (self):
        if (self.pet_food > 0):
            self.pet_food -= 50 
            self.pet.eat() 
        else:
            print("Sorry no food for now")
        return 
    
    def bathe(self):
        self.pet.noises()
        return self

Dusk = Pet("Dusk","cat","all tricks","meow")
print(Dusk.name)
ellie = Ninja("Ellie","Combs",Dusk,"Friskys")

ellie.bathe()
print(Dusk.health)
print(Dusk.energy)

ellie.feed()
print(Dusk.health)
print(Dusk.energy)

ellie.walk()
print(Dusk.health)
print(Dusk.energy)