class BankAccount:
	ROI = 10.5

	def __init__(self, holderName, accountBalance):
		self.Name = holderName
		self.balance = accountBalance

	def display(self):
		print(f"Account holder name is : {self.Name} and curent balance is : {self.balance}")

	def deposit(self,amount):
		self.balance = self.balance + amount
		return self.balance

	def withdraw(self,amount):
		if(amount < self.balance):
			self.balance = self.balance - amount
			return self.balance
		else:
			print("Insufficient balance")

	def calculateinterest(self):
		interest =  (self.balance * BankAccount.ROI) / 100
		return interest

obj1  = BankAccount("Amruta", 100)
obj1.display()
obj1.deposit(100)
obj1.display()
obj1.withdraw(110)
obj1.display()
interest = obj1.calculateinterest()
print("Interest for you is : ",interest)