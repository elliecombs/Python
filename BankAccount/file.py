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
        print(f" Balance: $ {self.account_balance}")
        return self
    
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts:
            print(account.account_balance)

account1 = BankAccount(.05,1000)
account2 = BankAccount(.25,2000)
print(account1.account_balance)
print(account2.account_balance)

account1.make_deposit(200).make_deposit(100).make_deposit(100).make_withdrawal(50).yield_interest().display_account_info()

account2.make_deposit(500).make_deposit(500).make_withdrawal(50).make_withdrawal(30).make_withdrawal(40).make_withdrawal(10).yield_interest().display_account_info()

BankAccount.print_all_accounts()
