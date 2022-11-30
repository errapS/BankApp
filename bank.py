from datasource import DataSource
from customer import Customer


class Bank:

    def __init__(self):
        self.customers = []
        self.acc_ids = []
        self.cust_ids = []

    def _load(self, path):
        data_source = DataSource()
        status = data_source.dataSourceConn(path)
        data = data_source.getData()
        dup_counter = 0
        if status[3] == '.csv':
            for index, row in data.iterrows():
            
                if index == 0:
                    continue

                elif self.addCustomer(row[0],str(row[1]), self.cust_ids) == False:
                    dup_counter += 1
                    for cust in self.customers:
                        if cust.getName() == row[0]:
                            cust.setAccount(row[2],float(row[3]))
                            break
                else:
                    
                    self.addCustomer(row[0],str(row[1]), self.cust_ids)
                    self.customers[index-1-dup_counter].setAccount(row[2],float(row[3]))
                    
        else:
            for index, row in data.iterrows():
                if self.addCustomer(row[0],str(row[1]), self.cust_ids) == False:
                    dup_counter += 1
                    for cust in self.customers:
                        if cust.getName() == row[0]:
                            cust.setAccount(row[2],float(row[3]))
                            break
                else:
                    self.addCustomer(row[0],str(row[1]), self.cust_ids)
                    self.customers[index-dup_counter].setAccount(row[2],float(row[3]))


    def getCustomers(self):
        return self.customers

    def addCustomer(self, name: str, ssn: str, cust_ids: list):

        for cust in self.customers:
            if name == cust.getName() and ssn == cust.getSsn():
                return False

        cust = Customer(name, ssn, cust_ids)
        self.customers.append(cust)
        self.cust_ids.append(cust.getId())
        return True


    def get_customer(self, ssn: str):
        c = 0
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                return self.customers[c]
            c +=1

        #'Customer not found!'
        return -1

    def getAllCustomers(self):
        all_customers = [['NAME','SSN', 'CUSTOMER_ID']]
        for cust in self.customers:
            all_customers.append([cust.getName(), cust.getSsn(), cust.getId()])
        return all_customers


    def changeCustomerName(self, new_name: str, ssn: str):
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                state = True
                cust.setName(new_name)
                return True

        return False


    def removeCustomer(self, ssn: str):
        del_customer = []
        c = 0
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                del_customer.append([self.customers[c].getName(), self.customers[c].getSsn(), self.customers[c].getId(),
                                [(acc.getAccountNumber(), acc.getBalance()) for acc in self.customers[c].getAccounts()]])
                del self.customers[c]
                return del_customer
            c += 1

        return -1

    def addAccount(self, ssn: str, balance: float):
        id = -1
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                cust.setAccount('Debit', balance)
                self.acc_ids = cust.getAccounts()
                id = self.acc_ids[-1]

        return id

    def getAccount(self, ssn: str, acc_id: str):
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                for acc in cust.getAccounts():
                    if acc == acc_id:
                        return acc.getAccountNumber(), acc.getBalance(), acc.getType()
        return False

    def deposit(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str):
        if sender != reciever:
            return False

        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                for acc in cust.getAccounts():
                    if acc.getAccountNumber() == reciever:
                        acc.setBalance(amount, sender, reciever, trans_date)
                        return True

        return False

    def withdraw(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str):
        if sender != reciever:
            return False

        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                for acc in cust.getAccounts():
                    if acc.getAccountNumber() == sender:
                        if acc.getBalance() > amount:
                            acc.setBalance(-amount, sender, reciever, trans_date)
                            return True
                        else:
                            raise Exception("Not enough funds to cover this transaction!")

        return False

    def send(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str):
        for cust_sender in self.getCustomers():
            if  ssn == cust_sender.getSsn():
                for acc_sender in cust_sender.getAccounts():
                    if acc_sender.getAccountNumber() == sender:
                        if acc_sender.getBalance() > amount:
                            acc_sender.setBalance(-amount, sender, reciever, trans_date)
                        else:
                            raise Exception("Not enough funds to cover this transaction!")

        for cust_reciever in self.getCustomers():
            for acc_reciever in cust_reciever.getAccounts():
                if acc_reciever.getAccountNumber() == reciever:
                    acc_reciever.setBalance(amount, sender, reciever, trans_date)
                    return True

        return False

    def closeAccount(self, ssn: str, account_number: str):
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                for acc in cust.getAccounts():
                    if acc.getAccountNumber() == account_number:
                        balance = acc.getBalance()
                        acc_number = account_number
                        cust.removeAccount(account_number)
                        print('\n **********CLOSING ACCOUNT**********')
                        print(f'ACCOUNT NUMBER: {acc_number} \nBALANCE: {balance}')
                        print('**********CLOSING ACCOUNT**********\n')
                        return balance, acc_number

        return False

    def getAllTransactionsBySSN(self, ssn: str, acc_id ):
        for cust in self.getCustomers():
            if  ssn == cust.getSsn():
                for acc in cust.getAccounts():
                    if acc.getAccountNumber() == acc_id:
                        return acc.getTransactions()

        return -1