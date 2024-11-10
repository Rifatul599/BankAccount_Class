class BankAccount:
    def __init__(self,account_holder,account_number):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=0.0
        self.transaction_history=[]

    def deposit(self,amount):
        self.balance += amount
        self.transaction_history.append(f"Deposited: {amount}")
        print(f"{amount} deposited.New balance {self.balance}")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient funds")
            self.transaction_history.append(f"Withdrawn: {amount}")
        else:
            self.balance -= amount
            self.transaction_history.append(f"withdraw: {amount}")
            print(f"{amount} withdrawn.New balance: {self.balance}")

    def get_balance(self):
        print(f"Current balance: {self.balance}")
        return self.balance

    def transfer_fund(self,another_account,amount):
        if amount>self.balance:
            print("Insufficient funds for transfer")
            self.transaction_history.append(f"Failed transfer attempt to {another_account.account_number}: {amount}")
        else:
            self.withdraw(amount)
            another_account.deposit(amount)
            self.transaction_history.append(f"Transferred: {amount} to account {another_account.account_number}")
            print(f"transferred {amount} to account {another_account.account_number}")
                  
    def view_transaction_history(self):
        print("Transaction history")
        for transaction in self.transaction_history:
            print(transaction)

    def get_account_details(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

Account1=BankAccount("Rifat",222333445)
Account2=BankAccount("Ammu",34567689)
Account1.deposit(2000)
Account1.withdraw(2000)
Account1.transfer_fund(Account2,1000)
Account1.view_transaction_history()
Account1.get_account_details()