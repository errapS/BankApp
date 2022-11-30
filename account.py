
from datetime import date
import uuid

class Account:

    def __init__(self, type: str, balance: float):
        self.balance = balance
        self.type = type

        id = uuid.uuid4().hex

        self.transactions = []
        self.accNum = id
        if balance != 0:
            d = date.today().strftime("%d/%m/%Y")
            self.transactions = [[d, self.accNum, self.accNum, balance]]
        

    def getType(self):
        return self.type

    def getBalance(self):
        return self.balance
    
    def setBalance(self, amount: float, sender: str, reciever: str, trans_date: str):
        self.balance += amount
        self.addTransaction(amount, sender, reciever, trans_date)

    def getAccountNumber(self):
        return self.accNum

    def printAccount(self):
        print('==========================================================')
        print('{:<20}  {:^2}'.format('Account number:', self.accNum))
        print('{:<20}  {:^2}'.format('Account type:', self.type))
        print('{:<20}  {:^2}'.format('Account balance:', self.balance))
        print('========================================================== \n')
    
    def getTransactions(self):
        return self.transactions
        
    def printTransactions(self, start_date: str, end_date: str):
        print(f'Account number: {self.accNum}')
        print('==============================================================================================================')
        print('{:<10}  {:^15} {:^50} {:^25}'.format('DATE', 'FROM', 'TO', 'AMOUNT'))
        print('--------------------------------------------------------------------------------------------------------------')
        print_state = False
        
        self.transactions.sort()
        for trans in reversed(self.transactions):
            if start_date == None and start_date == None:
                print('{:<15}  {:5} {:^36} {:^9}'.format(trans[0], trans[1], trans[2], trans[3]))
            elif end_date != start_date:
                if trans[0] == end_date:
                    print_state = True
                elif trans[0] == start_date:
                    print_state = False

                if print_state == True:
                    print('{:<15}  {:5} {:^36} {:^9}'.format(trans[0], trans[1], trans[2], trans[3]))

            elif trans[0] == start_date:
                print('{:<15}  {:5} {:^36} {:^9}'.format(trans[0], trans[1], trans[2], trans[3]))
                

            
        print('============================================================================================================== \n')

    def addTransaction(self, amount: float, sender: str, reciever: str, trans_date: str):
        if trans_date == None: #Check format
            date_today = date.today().strftime("%d/%m/%Y")
        else:
            date_today = trans_date

        self.transactions.append([date_today, sender, reciever, amount])


     

   


