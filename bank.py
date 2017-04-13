import os
class BankAccount:
  def __init__(self, name='', balance = 0, acctNumber = -1):
    self.name = name
    self.balance = balance
    self.acctNumber = acctNumber
  def __del__(self):
    os.remove(str(self.account) + '.txt')
    print('Account Number ' + str(self.acctNumber) + ' is now closed.')
  def __str__(self):
    return ("Account Number: " + str(self.acctNumber) + '\n'
            +"Name: " + str(self.name) + '\n'
            +"Balance: " + str(self.balance)
           )
  def deposit(self, amount):
    self.balance += amount
  def withdraw(self, amount):
    self.balance -= amount
  def transfer(self, account, amount):
    account.balance += amount
    self.balance -= amount
  def getbalance(self):
    return self.balance
  def setbalance(self):
    self.balance = 0
    
  def total(self, accounts): # add up all the balances from an array of Bank Accounts
    totalB = 0
    for account in accounts:
      totalB += account.balance
    return totalB
  def __lt__(self, account): # use the balance as the criteria
    return self.balance < account.balance
  def __gt__(self, account): # use the balance as the criteria
    return self.balance > account.balance
  def __eq__(self, account): # use the balance as the criteria
    return not self.balance < account.balance and not self.balance > account.balance
  def __add__(self, account): # add two balances
    return self.balance + account.balance
  # probably part of Bank application side of the project
  def sort(self, accounts): # sor the array by name
    pass
  def history(self, event):
    hist = str(self.account)
    with open(hist + '.txt', 'a') as f:
      f.write(event + ':') # to do write details of what the account did (i.e. balance, withdrawl, etc.)
    
    
