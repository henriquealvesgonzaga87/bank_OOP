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
