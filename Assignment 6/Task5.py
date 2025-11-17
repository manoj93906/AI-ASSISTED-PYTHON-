class BankAccount:
    """
    Represents a bank account with functionalities to deposit, withdraw, and check the balance.
    """

    def __init__(self, initial_balance=0.0):
        """
        Initializes a BankAccount object.

        Args:
            initial_balance (float or int): The starting balance. Must be non-negative.

        Raises:
            ValueError: If the initial_balance is negative or not a number.
        """
        # Validate that the initial_balance is a non-negative number (integer or float).
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        # The underscore prefix on `_balance` indicates it's intended for internal use.
        self._balance = float(initial_balance)  # Store balance as a float for consistency.

    def deposit(self, amount):
        """
        Deposits a given amount into the account.

        Args:
            amount (float or int): The amount to deposit. Must be a positive number.

        Returns:
            str: A message indicating the outcome of the deposit.
        """
        # The deposit amount must be a number greater than zero.
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Error: Deposit amount must be a positive number."
        # Add the amount to the current balance.
        self._balance += float(amount)
        return f"Successfully deposited ${amount:.2f}."

    def withdraw(self, amount):
        """
        Withdraws a given amount from the account.

        Args:
            amount (float or int): The amount to withdraw. Must be a positive number.

        Returns:
            str: A message indicating the outcome of the withdrawal.
        """
        # The withdrawal amount must be a number greater than zero.
        if not isinstance(amount, (int, float)) or amount <= 0:
            return "Error: Withdrawal amount must be a positive number."
        # Check for sufficient funds before allowing the withdrawal.
        if amount > self._balance:
            return "Error: Insufficient funds for this withdrawal."
        # Subtract the amount from the current balance.
        self._balance -= float(amount)
        return f"Successfully withdrew ${amount:.2f}."

    def get_balance(self):
        """
        Returns the current balance of the account.

        Returns:
            float: The current account balance.
        """
        # This method provides controlled access to the account's balance.
        return self._balance

# This block demonstrates how to use the BankAccount class.
# The `if __name__ == "__main__":` construct ensures this code only runs
# when the script is executed directly (not when imported as a module).
if __name__ == "__main__":
    print("--- Bank Account Operations ---")
    
    # Create a new account instance with an initial balance of $500.00.
    my_account = BankAccount(500.0)
    print(f"Account created. Current balance: ${my_account.get_balance():.2f}")
    
    # --- Test Deposit ---
    # Deposit a valid amount and check the new balance.
    print(my_account.deposit(150.50))
    print(f"Current balance after deposit: ${my_account.get_balance():.2f}\n")
    
    # --- Test Successful Withdrawal ---
    # Withdraw a valid amount and check the new balance.
    print(my_account.withdraw(75))
    print(f"Current balance after withdrawal: ${my_account.get_balance():.2f}\n")
    
    # --- Test Insufficient Funds ---
    # Attempt to withdraw more money than is available in the account.
    print(my_account.withdraw(1000))
    print(f"Final balance: ${my_account.get_balance():.2f}")
