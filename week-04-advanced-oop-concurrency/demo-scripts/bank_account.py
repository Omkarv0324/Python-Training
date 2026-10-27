"""Session 4.1 demo — @property for validation + class vs instance attributes.

A BankAccount models state (balance) + behavior (deposit/withdraw), and uses
@property to validate the balance without changing how callers read it.
"""


class BankAccount:
    # CLASS attribute — shared by every account.
    currency = "USD"

    def __init__(self, owner, balance=0):
        self.owner = owner          # instance attribute
        self._balance = balance     # "_" = treat as internal

    @property
    def balance(self):
        """Read balance like a normal attribute: account.balance"""
        return self._balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise ValueError("insufficient funds")
        self._balance -= amount
        return self._balance

    @classmethod
    def joint(cls, owner_a, owner_b):
        """Alternative constructor (classmethod) for a joint account."""
        return cls(f"{owner_a} & {owner_b}")

    @staticmethod
    def is_valid_amount(amount):
        """Related helper that needs no instance."""
        return amount > 0


acc = BankAccount("Ada", 100)
acc.deposit(50)
acc.withdraw(30)
print(f"{acc.owner}: {acc.balance} {BankAccount.currency}")   # 120

joint = BankAccount.joint("Ada", "Alan")
print("Joint owner:", joint.owner)
print("Valid amount?", BankAccount.is_valid_amount(-5))

# Validation kicks in automatically:
try:
    acc.withdraw(10_000)
except ValueError as e:
    print("Blocked:", e)
