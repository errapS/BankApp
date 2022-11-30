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
        


    
    

 


  


  
  

    

