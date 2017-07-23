class BankAccount(object):
  balance = 0
  def __init__(self, name):
    self.name = name
  
  def __repr__(self):
    return "Account Holder Name: %s\nBalance: %.2f" %(self.name, self.balance)
  
  def show_balance(self):
    print "Total Balance: %.2f" %(self.balance)
  
  def deposit(self, amount):
    if amount <= 0:
      print "You are not allowed to deposit bagger"
      return
    else:
      print "Your Deposit: %.2f" %(amount)
      self.balance += amount
      #print "new balance: %.2f" %(self.balance)
      self.show_balance()
      
      
  def withdraw(self, amount):
    if amount > self.balance:
      print "Your account will be empty. Your are not allowed to withdraw %.2f" %(amount)
      return
    
    else:
      print "Withdraw amount: %.2f" %(amount)
      self.balance -= amount
      self.show_balance()
        
      
      
my_account = BankAccount("Shankar")
print my_account


my_account.deposit(2000)
my_account.deposit(1000)

my_account.withdraw(1000)
print my_account
