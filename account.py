class BankAccount(object):
    """ Bank accounts have thefollowing properties:

    Attributes:
        
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self,balance=0.0):
        
        self.status = true
        self.balance = balance
    def active(self)
        self.status = true
    def get_balance(self):
        if self.status == False:
            raise ValueError('closed account')
        return self.balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        if amount < 0:
            raise ValueError('wrong entry')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        if self.status == False:
            raise ValueError('account closed')
        if amount < 0:
            raise ValueError('wrong value')
        self.balance += amount
        return self.balance
    def close(self):
        self.status = False
