class Client:
    def __init__(self, address):
        self.address = address
        self.accounts = []

    def make_transaction(self, account, transaction):
        transaction.register(account)

    def add_account(self, account):
        self.accounts.append(account)


class PrivateClient(Client):
    def __init__(self, tax_number, name, birth_date, address):
        super().__init__(address)
        self.tax_number = tax_number
        self.name = name
        self.birth_date = birth_date


class Account:
    def __init__(self, number, client):
        self._balance = 0
        self._number = number
        self._agency = '0001'
        self._client = client
        self._historic = Historic()

    @classmethod
    def new_account(cls, client, number):
        return cls(client, number)

    @property
    def balance(self):
        return self._balance

    @property
    def number(self):
        return self._number

    @property
    def agency(self):
        return self._agency

    @property
    def client(self):
        return self._client

    @property
    def historic(self):
        return self._historic

    def withdraw(self, value):
        account_balance = self._balance
        if value > account_balance:
            print("Operation denied. You don't have this amount in your account!")
        elif value <= 0:
            print('Operation denied. Needs to be a positive amount!')
        else:
            account_balance -= value
            print("Withdraw your money! Thank you")
            return True
        return False

    def deposit(self, value):
        account_balance = self._balance
        if value > 0:
            account_balance += value
            print(f"You have deposited ${value:.2f}")
        else:
            print("Operation denied! The amount informed is not valid!")
            return False
        return True


class BankAccount(Account):
    def __init__(self, number, client, limit_amount_withdraw=500, limit_quantity_withdraw=3):
        super().__init__(number, client)
        self._limit_amount_withdraw = limit_amount_withdraw
        self._limit_quantity_withdraw = limit_quantity_withdraw

    def withdraw(self, value):
        quantity_withdraw = len(i for i in self.historic.transactions if i["type"] == Withdraw.__name__)
        limit_amount_exceeded = value > self._limit_amount_withdraw
        limit_withdraw_exceede = quantity_withdraw > self._limit_quantity_withdraw

        if limit_amount_exceeded:
            print("Operation denied. The limit of $500.00 has been exceeded!")

        elif limit_withdraw_exceede:
            print("Operation denied. The limir of 3 withdraws has been exceeded!")

        else:
            super().withdraw(value)

    def __str__(self):
        return f"""\
            Agency:\t{self.agency}
            Bank Account:\t{self.number}
            Client:\t{self.client.name}
        """
