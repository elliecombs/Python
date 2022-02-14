class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email
        self.account_balance = 15000
    
    def make_withdrawal(self, amount):
        if (self.account_balance - amount) >= 0 :
            self.account_balance -= amount
            print(self.account_balance)
        else:
            print("NO WITHDRAWS")
        return self
        
    def make_deposit(self, amount):
        self.account_balance += amount 
        return self 
    
    def transfer_money(self,amount, user):
        if (self.account_balance - amount) >= 0 :
            self.account_balance = amount
            user.account_balance += amount
            print(self.username,self.account_balance)
            print(user.username, user.account_balance)
            print(self.username,"Sent",user.username,"$",amount)
        else:
            print("YOU HAVE NO MONEY")   
        return self
    
    def display_user_balance(self):
        print(f"User: {self.username}, Balance: {self.account_balance}")
        return self
    
ellie = User("ellie","e.c@gmail.com")
sam = User("Sam", "sam.g@gmail.com")
mohammad = User("mohammad","m.a@gmail.com")

print("************")
print("Ellie's Account:",ellie.account_balance)
print("************")
print("Sam's Account:",sam.account_balance)
print("************")
print("Mohammad's Account:",mohammad.account_balance)
print("************")
print(sam.username,sam.email,sam.account_balance)
print("************")
print(ellie.username, ellie.email, ellie.account_balance)
print("************")
print(mohammad.username, mohammad.email, mohammad.account_balance)
print("************")

ellie.make_deposit(1000)
ellie.make_deposit(1000)
ellie.make_deposit(1000)
ellie.make_withdrawal(50)
ellie.display_user_balance()

sam.make_deposit(1000)
sam.make_deposit(2000)
sam.make_withdrawal(20)
sam.make_withdrawal(30)
sam.display_user_balance()

mohammad.make_deposit(5000)
mohammad.make_withdrawal(60)
mohammad.make_withdrawal(70)
mohammad.make_withdrawal(20)
mohammad.display_user_balance()

ellie.transfer_money(100,sam).display_user_balance


