class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack ( self , ninja ):
        if self.speed >= 10: #Attack if Speed is greater than or equal 10 then the 
            ninja.health -= (self.strength * 2)
            self.speed = 3 #Check speed for next attack 
        else: #regular attack
            self.speed += 3
            ninja.health -= self.strength
        if ninja.health <= 0: #Evaluates the health status after the attacks
            ninja.health = 0
            print(f"{self.name} Finito Ninja!")
        return self
