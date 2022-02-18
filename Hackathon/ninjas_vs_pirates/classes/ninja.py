class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.speed >= 10:#Attack if Speed is greater than or equal 10 then the
            pirate.health -= (self.strength * 2)
            self.speed = 5 #Check speed for next attack 
        else:  #regular attack
            self.speed += 5
            pirate.health -= self.strength
        if pirate.health <= 0: #Evaluates the health status after the attacks
            pirate.health = 0
            print(f"{self.name} Finito Jack Sparrow!")
        return self