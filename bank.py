class Account:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.deposits = []
        self.withdrawals = []
        self.loan_balance = 0

    def check_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount
        self.deposits.append({"amount": amount, "narration": "deposit"})

    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.withdrawals.append({"amount": amount, "narration": "withdrawal"})
            return True
        else:
            return False

    def print_statement(self):
        transactions = self.deposits + self.withdrawals
        for transaction in transactions:
            print(transaction["narration"], "-", transaction["amount"])

    def borrow_loan(self, amount):
      if self.loan_balance > 0:
        
        return "There is an outstanding loan balance on the account"
      elif amount <= 100:
        # 
        return "Loan amount requested is not more than 100"
      elif len(self.deposits) < 10:
        # 
        return "Customer has not made at least 10 deposits"
      elif amount > sum([transaction["amount"] for transaction in self.deposits])/3:
        # 
        return "Amount requested is greater than 1/3 of their total sum of all deposits"
      else:
         "All conditions are satisfied, increase the loan balance and return True"
         self.loan_balance += amount
         self.balance += amount
         return True

    def repay_loan(self, amount):
        if amount >= self.loan_balance:
            self.balance += (amount -self.loan_balance)
            self.loan_balance = 0
        else:
            self.loan_balance -= amount
            self.balance += amount

    def transfer(self, amount, account):
        if self.balance >= amount:
            self.balance -= amount
            account.deposit(amount)
            return True
        else:
            return False







            
        