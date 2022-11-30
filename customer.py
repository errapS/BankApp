from account import Account
import uuid

class Customer:

    def __init__(self, name: str, ssn: str, cust_ids: list):
        self.name = name
        self.ssn = ssn
        self.accounts = []

        id = uuid.uuid4().hex

        while id in cust_ids:
            id = uuid.uuid4().hex

        self.id = id

    def getId(self):
        return self.id
    
    def setName(self, name: str):
        self.name = name
        
    def getName(self):
        return self.name

    def getSsn(self):
        return self.ssn
    
    def getAccounts(self):
        return self.accounts
    
    def setAccount(self, account_type: str, balance: float):
        self.accounts.append(Account(account_type, balance))
    
    def printAccounts(self, accounts: list, start_date: str, end_date: str):
        print(f'Name: {self.name}  | SSN: {self.ssn}  | Customer id: {self.id}')
        for acc in accounts:
            acc.printAccount()
            acc.printTransactions(start_date, end_date)
    

    def removeAccount(self, account: str):
        for acc in self.accounts:
            if acc.getAccountNumber() == account:
                self.accounts.remove(acc)

    