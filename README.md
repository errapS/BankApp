# BankApp
Backend for a simplified bank application.

###### Task
The task was to create a fictiv system for a bank. The bank should be able to handle multiple customers and each customer may have multiple accounts.

###### General requirements
- Bank only supports accounts of type 'Debit'
- The application will be run from `main.py`
- Three classes is required; `Account`, `Customer` and `Bank`

###### Class requirments: Bank
- Print a list containing all the bank's customers (social security number, first- and last name)
- Add a new customer with a unique social security number.
- Change an existing customer's name.
- Remove an existing customer, their accounts needs to be closed as well.
- Create an account for a customer with a unique account number.
- Close a customer's account given the account number.
- Store and present transaction history for each account.
- Deposit to an account
- Withdraw from account.

###### Class requirements: Customer
- Customer ID
- Customer's first- and last name
- Customer's social security number
- Customer's account/accounts

###### Class requirements: Account
- Account balance
- Account type
- Account number
- Account transactions
- Fetch account number

###### Class: DataSource
Importing and handling data into a dataframe, needs to support following file types:
- `.json`
- `.csv`
- `.txt`

###### Other
The mock-data used in this project has been created in order to test functionality of the functions and logics. The format of the data has not been specified which might cause issues in the data-handling functions when using data that has a different format.

## Description of functions

##### Required packages
- Pandas, `pip install pandas`
- NumPy, `pip install numpy`
- DateTime, `pip install DateTime`
- uuid, `pip install uuid`
- csv, `pip install python-csv`


##### Class: DataSource
- `dataSourceConn(self, path: str)` - tries to load the data from given path, calls load-function depending on file extension. Raises exception if the file format is not supported or bad path. 
- `jsonLoad(self, path: str)`, `txtLoad(self, path: str)`, `csvLoad(self, path: str)` - loads given file, converts it into a dataframe and returns the dataframe. It is currently limited to the format of given input file.
- `getAll(self)` - returns all customers in the dataframe, presented with name and social security number.
- `findByID(self, id: str)` - returns a customer's name and social security number given the social security number. If customer/social security number does not exist in the dataframe, function returns -1.
- `removeByID(self, id: str)` - removes a customer from the dataframe given a social security number. Returns the deleted customer's name and social security number if customer was found in the dataframe, else returns -1 if customer was not found.
- `def getData(self):` - returns the dataframe.

##### Class: Account
- Initializing the class takes two input arguments, `type` and `balance`. Creating an object from the Account class, generates random account number by utilizing `UUID` which creates a unique 32-character hexadecimal string. 
- `getType(self)` - returns the account type.
- `getBalance(self)` - returns the account balance.
- `getAccountNumber(self)` - returns the account number.
- `getTransactions(self)` - returns a list of transactions.
- `setBalance(self, amount: float, sender: str, reciever: str, trans_date: str)` - updates the account balance with the given amount and calls for the function `addTransaction` to append the transaction.
- `addTransaction(self, amount: float, sender: str, reciever: str, trans_date: str)` - function takes 4 input arguments and appends the transaction to the transactions list. If the trans_date argument is None the function will call on `DateTime` to get the current date. The trans_date argument needs to be either None or on the format "d/m/Y", the function does not currenty support other formats. 
- `printAccount(self)` - formatted print of the account's number, type and balance
- `printTransactions(self, start_date: str, end_date: str)` - formatted print of the account's transaction history within a given period (start_date:end_date]. If both start_date and end_date are None, it will print the entire transaction history of the account.

##### Class: Customer
- Initializing the class takes three input arguments, `name`, `ssn` and `cust_ids`. Creating an object from the Customer class, generates random account number by utilizing `UUID` which creates a unique 32-character hexadecimal string. If the generated customer id already exists it will generate a new id until it's unique.
- `getId(self)` - returns customer's id.
- `getName(self)` - returns customer's name.
- `getSsn(self)` - returns customer's social security number. 
- `getAccounts(self)` -  returns a list with a customer's accounts (objects)
- `setName(self, name: str)` - takes input argument `name`, changes the customer's name to the given input.
- `setAccount(self, account_type: str, balance: float)` - calls for the `Account`-class which creates an account-object and appends it to the list of accounts.
- `printAccounts(self, accounts: list, start_date: str, end_date: str)` - prints the account-details (number, type, balance) and its transaction history within the given period for all of the customer's accounts. 
- `removeAccount(self, account: str)` - removes a customer's account from the list of accounts given the account number.
        
##### Class: Bank
- `_load(self, path)` - takes a path as input-argument and calls for `DataSource` to handle the file and return a dataframe. It proceeds to use the dataframe in order to populate the bank with the customers.
- `getCustomers(self)` - returns a list of customers (customer-objects).
- `get_customer(self, ssn: str)` - returns a customer-object given a social security number, returns -1 if customer was not found.
- `def getAllCustomers(self):` - returns a list with each customer's name, social security number and customer id. 
- `addCustomer(self, name: str, ssn: str, cust_ids: list)` - adds customer given a name and a social security number. If the pair of name and social security number already exist in the bank (the customer already exists), it will return False.
- `changeCustomerName(self, new_name: str, ssn: str)` - changes a customer's name given its social security number. Returns True if successful, else returns False.
- `removeCustomer(self, ssn: str)` - removes customer from the customer-list given the customers social security number and returns the removed customer's details if successful, else returns -1.
- `addAccount(self, ssn: str, balance: float)` - adds an account to customer specified by its social security number. Returns the added account's id if succesful, else returns -1.
- `getAccount(self, ssn: str, acc_id: str)` - returns the account details given a account owner's social security number and the account number, returns False if account was not found.
- `deposit(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str)` -  returns False if the sender- and the reciever-adress does not match or if the account number/customer is not found. Else it will call for the `Account`-function `setBalance` which updates the account balance and adds the transaction to the transaction list, returns True. 
- `withdraw(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str)` - returns False if the sender- and the reciever-adress does not match or if the account number/customer is not found. If the account does not have enough funds to cover the transaction it will raise an exception. Else it will call for the `Account`-function `setBalance` which updates the account balance and adds the transaction to the transaction list, returns True. 
- `send(self, ssn: str, amount: float, sender: str, reciever: str, trans_date: str)` - returns False if sender or reciever-adress is not found. If the sender-account does not have enough funds to cover the transaction it will raise an exception. Else it will call for the `Account`-function `setBalance` for both the sender- and reciever-account which updates each account's balance and adds the transaction to the transaction list, returns True. 
- `closeAccount(self, ssn: str, account_number: str)` - if account is not found it will return False. If account is found it will remove the account from the list of accounts and return the removed account's balance and account number.
- `getAllTransactionsBySSN(self, ssn: str, acc_id )` - if account is found it will return a list of the account's transactions, else it will return -1.

##### Diagram
![https://app.conceptboard.com/export/ab9a389c-44a4-44f7-883b-450ef4c7fdc6/versions/;hi=1;low=196]

## Conclusion/reflection


    
    
  
    
    
    
    


    
    

 


  


  
  

    

