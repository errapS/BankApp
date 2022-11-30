from datasource import DataSource
from bank import Bank
from customer import Customer
from account import Account 


def main(path):

    '''Initialize the bank and load customers from mock-data'''
    bank = Bank()
    bank._load(path)

    '''Print all customers registered in the bank'''
    for customer in bank.getCustomers():
        customer.printAccounts(customer.getAccounts(), None, None)
    # print(bank.getAllCustomers())
    
    '''Change a customers name using their SSN, returns False if customer is not found'''
    # print(bank.getAllCustomers())
    # bank.changeCustomerName('Anna Annsson','199707058301')
    # print(bank.getAllCustomers())

    '''Adds customer using their SSN '''
    # print(bank.getAllCustomers())
    # add_customer = bank.addCustomer('Jens Jensson', '195701015631', bank.cust_ids)
    # print(add_customer)
    # print(bank.getAllCustomers())

    '''Removes customer using their SSN '''
    # print(bank.getAllCustomers())
    # del_customer = bank.removeCustomer('199707058301')
    # print(del_customer)
    # print(bank.getAllCustomers())
    
    '''Adding and closing account for a customer specified by SSN'''
    # c = bank.get_customer('199707058301')
    # print('\n***********************BEFORE ADDING ACCOUNT***********************')
    # c.printAccounts(c.getAccounts(), '28/11/2022','29/11/2022')
    # bank.addAccount('199707058301',500)
    
    # print('\n***********************AFTER ADDING ACCOUNT***********************')
    # c.printAccounts(c.getAccounts(), '28/11/2022','29/11/2022')
    # bank.closeAccount('199707058301', c.getAccounts()[1].getAccountNumber())

    # print('\n***********************AFTER CLOSING ACCOUNT***********************')
    # c.printAccounts(c.getAccounts(), '28/11/2022','29/11/2022')

    '''View customer information (accounts, account numbers, account type, balance)'''
    '''Deposit and withdraw money'''
    # c = bank.get_customer('199707058301')
    # print('\n***********************INITIAL STATE OF ACCOUNT***********************')
    # c.printAccounts(c.getAccounts(), '28/11/2022','29/11/2022')
   
    # bank.deposit('199707058301', 1344, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), '28/11/2022')
    # bank.deposit('199707058301', 500, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), '27/11/2022')
    # bank.deposit('199707058301', 1908.2, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), '24/11/2022')
    # bank.deposit('199707058301', 178.1, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), '27/11/2022')

    # print('\n***********STATE OF ACCOUNT AFTER DEPOSITS WITHIN PERIOD****************')
    # print(c.printAccounts(c.getAccounts(), '27/11/2022','29/11/2022'))

    # print('\n***********STATE OF ACCOUNT AFTER DEPOSITS ALL-TIME****************')
    # c.printAccounts(c.getAccounts(), None, None)

    # print('\n***********STATE OF ACCOUNT AFTER WITHDRAW****************')
    # bank.withdraw('199707058301', 1930.3, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), None)
    # c.printAccounts(c.getAccounts(), None, None)

    # print('\n***********STATE OF ACCOUNT AFTER NO-COVER WITHDRAW****************')
    # bank.withdraw('199707058301', 10000, c.getAccounts()[0].getAccountNumber(), c.getAccounts()[0].getAccountNumber(), None)
    # c.printAccounts(c.getAccounts(), None, None)

    '''Sending funds between customers own accounts and other customers'''
    # c1 = bank.get_customer('199707058301')  # Anna
    # c2 = bank.get_customer('199111117821')  # Rafael

    # print('\n***********************INITIAL STATE OF ANNAS ACCOUNTS***********************')
    # c1.printAccounts(c1.getAccounts(), None, None)

    # print('\n***********************INITIAL STATE OF RAFAELS ACCOUNT***********************')
    # c2.printAccounts(c2.getAccounts(), None, None)

    # bank.send('199111117821',1000,c2.getAccounts()[0].getAccountNumber(), c1.getAccounts()[0].getAccountNumber(), None)

    # print('\n***********STATE OF ANNAS ACCOUNT AFTER TRANS****************')
    # c1.printAccounts(c1.getAccounts(), None, None)

    # print('\n***********STATE OF RAFAELS ACCOUNT AFTER TRANS****************')
    # c2.printAccounts(c2.getAccounts(), None, None)

    # print('\n***********STATE OF ANNAS ACCOUNTS AFTER ADDING ACC****************')
    # bank.addAccount('199707058301',0)
    # c1.printAccounts(c1.getAccounts(), None, None)
    # bank.send('199111117821',1000,c2.getAccounts()[0].getAccountNumber(), c1.getAccounts()[1].getAccountNumber(), None)

    # print('\n***********STATE OF ANNAS ACCOUNTS AFTER NEW TRANS****************')
    # c1.printAccounts(c1.getAccounts(), None, None)

    # print('\n***********STATE OF RAFAELS ACCOUNT AFTER NEW TRANS****************')
    # c2.printAccounts(c2.getAccounts(), None, None)

    # bank.send('199707058301',500,c1.getAccounts()[0].getAccountNumber(), c1.getAccounts()[1].getAccountNumber(), None)
    # print('\n***********STATE OF ANNAS ACCOUNTS AFTER INTERNAL TRANS****************')
    # c1.printAccounts(c1.getAccounts(), None, None)

    '''Get all transactions by SSN'''
    # c1 = bank.get_customer('199707058301')
    # res = bank.getAllTransactionsBySSN('199707058301',c1.getAccounts()[0].getAccountNumber())
    # print(res)



main('mock.txt')
# main('mock.csv')
# main('mock.json')

