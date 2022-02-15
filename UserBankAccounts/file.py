class BankAccount:
    
    all_accounts = []
    
    def __init__(self, int_rate = 0, account_balance = 0):
        self.account_balance = account_balance
        self.int_rate = int_rate
        BankAccount.all_accounts.append(self)
        
    def make_withdrawal(self, amount):
        if (self.account_balance - amount) >= 0 :
            self.account_balance -= amount
            print(self.account_balance)
        else:
            self.account_balance -= -5
            print("Insufficient funds!")
        return self
        
    def make_deposit(self, amount):
        self.account_balance += amount 
        return self 
    
    def yield_interest(self):
        if self.account_balance >= 0 :
           self.account_balance += (self.account_balance * self.int_rate )
        return self 
    
    def display_account_info(self):
        print(f" Balance: ${self.account_balance}")
        return f" Balance: ${self.account_balance}"
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_balance)
            
class User:
    def __int__ (self, name,email):
        self.name = name
        self.email = email
        self.account = {
            "checking": BankAccount(.15,20000),
            "savings": BankAccount(.10,10000)
        }
        
    def display_user_balance(self):
        print(f"User:{self.name}, checking Balance: {self.account['checking'].display_account_info} ")
        print(f"User:{self.name}, savings Balance:{self.account['savings'].display_account_info}")
        return self
    
ellie = User("ellie")
ellie.display_user_balance()

ellie.account['checking'].make_deposit(2000).display_account_info()
ellie.account['savings'].make_deposit(1000).display_account_info()
