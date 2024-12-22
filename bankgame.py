class BankAccount:
	def __init__(self, balance: 0, owner: 'name'):
		self.balance = balance
		self.owner = owner

	def deposit(self, amount):
		self.balance += amount
		print(f'deposit {self.balance} to {self.owner}')
		return self.balance

	def withdraw(self, amount):
		if self.balance >= amount:
			self.balance -= amount
			print(f'снятие {amount} со счета {self.owner}')
			return self.balance
		else:
			print('на счете недостаточно средств!!')
			return self.balance

	def get_balance(self):
		return print('ваш баланс: ' + str(self.balance))

bank1 = BankAccount(10000, 'Ivan')
b = bank1
b.get_balance()
b.deposit(100)
b.withdraw(10200)
b.deposit(100)
b.withdraw(10200)
b.get_balance()