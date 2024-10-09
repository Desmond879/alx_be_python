# bank_account.py

class BankAccount:
    """A class representing a bank account with basic operations like deposit, withdraw, and balance display."""

    def __init__(self, initial_balance=0):
        """
        Initialize a new BankAccount with an optional initial balance.
        :param initial_balance: Initial balance to set for the account, default is 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Deposit the given amount into the account.
        :param amount: Amount to be deposited.
        """
        if amount > 0:
            self.account_balance += amount
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """
        Withdraw the given amount from the account if sufficient funds are available.
        :param amount: Amount to be withdrawn.
        :return: True if the withdrawal was successful, False if insufficient funds.
        """
        if amount > 0:
            if amount <= self.account_balance:
                self.account_balance -= amount
                return True
            else:
                return False
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")
