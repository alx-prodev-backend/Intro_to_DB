# bank_account.py

class BankAccount:
    """A simple bank account class with deposit, withdraw, and balance display."""

    def __init__(self, initial_balance=0):
        """Initialize the bank account with an optional balance."""
        self.account_balance = float(initial_balance)

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw a positive amount if sufficient funds exist.

        Returns:
            True if withdrawal succeeds,
            False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """Print the current balance in the required format."""
        print(f"Current Balance: ${self.account_balance:.2f}")
