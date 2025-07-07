class BankAccount:
    balance = 0

    def add_money(self, amount):
        self.balance = self.balance + amount
        return self.balance

    def subtract_money(self, amount):
        self.balance = self.balance - amount
        return self.balance


class SavingsAccount(BankAccount):
    def __init__(self, min_balance):
        self.min_balance = min_balance

    def subtract_money(self,amount):
        future_amount = self.balance - amount
        print('future_amount', future_amount)
        if future_amount >= self.min_balance: 
            return super().subtract_money(amount)
        else:
            print('No se puede hacer la operacion ya que quedaría con menos del saldo minimo')


bankAccount = BankAccount()
print('Balance inicial $',bankAccount.balance)
print('Account addition $',bankAccount.add_money(100000))
print('Balance total $',bankAccount.balance)

savingsAccount =  SavingsAccount(30000)
savingsAccount.add_money(70000)
print('Saving account: ',savingsAccount.balance)
print('\n')

savingsAccount.subtract_money(45000)
print(savingsAccount.balance,'\n')

savingsAccount.subtract_money(70000)
print(savingsAccount.balance,'\n')

savingsAccount.subtract_money(40000)
print(savingsAccount.balance,'\n')