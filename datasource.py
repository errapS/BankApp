import os
import json
import pandas as pd
import numpy as np
import csv


# from bank import Bank
from customer import Customer

class DataSource:
    
    def __init__(self):
        self.data = None
    def dataSourceConn(self, path: str):
        try:
            file_name, file_extension = os.path.splitext(path)
            if file_extension == '.json':
                self.data = self.jsonLoad(path)
            elif file_extension == '.txt':
                self.data = self.txtLoad(path)
            elif file_extension == '.csv':
                self.data = self.csvLoad(path)

            return (True, "Connection successful", [file_name + file_extension], file_extension)
        except:
            raise Exception("Bad datasource! Verify path and format, supported file extensions '.json, .txt, .csv'")

    def jsonLoad(self, path: str):
        with open(path, 'r', encoding='utf-8') as f:
            json_list = json.load(f)
        data = pd.DataFrame(json_list, columns = ['Name','SSN','Type','Balance'])

        return data

    def txtLoad(self, path: str):
        with open(path) as f:
            text = [l.replace("#", ":") for l in f]

        d = np.loadtxt(text, dtype=str, delimiter="\n")
        d_split = [l.split(':') for l in d]

        df_array = []
        for line in d_split:
            for i in range(0,len(line)):
                if line[i] == 'debit account':
                    df_array.append([line[1],line[2], 'Debit', line[i+1]])

        data = pd.DataFrame(df_array, columns = ['Name','SSN','Type','Balance'])

        return data


    def csvLoad(self, path: str):
        with open(path, 'r') as f:
            reader = csv.reader(f)
            csv_list = list(reader)
        data = pd.DataFrame(csv_list, columns = ['Name','SSN','Type','Balance'])

        return data

    def getAll(self):
        customers = []
        print('{:<15} | {:5}'.format('NAME', 'SSN'))
        print('=====================================')
        for index, row in self.data.iterrows():
            if (row[0],row[1]) not in customers:
                customers.append((row[0], row[1]))
                print('{:<15} | {:5}'.format(row[0], row[1]))

        return customers

    def updateByID(self, id: str):
        '''Update what? Should take arg for what field to update'''
        pass

    def findByID(self, id: str):
        for index, row in self.data.iterrows():
            if row[1] == id:
                return {'Name': row[0], 'SSN': row[1]}
        return -1

    def removeByID(self, id: str):
        for index, row in self.data.iterrows():
            if row[1] == id:
                del_customer = {'Name': row[0], 'SSN': row[1]}
                self.data = self.data.drop(index)
                return del_customer
        return -1

    def getData(self):
        return self.data

'''Uncomment to print the dataframe from different files'''
# d = DataSource()
# x, data_json = d.dataSourceConn('mock.json')
# print(data_json)
# print(d.getAll())
# print(d.findByID('199707058301'))
# d.removeByID('199707058301')
# print(data_json)
# print(d.getData())

# y, data_csv = DataSource().dataSourceConn('mock.json')
# print(data_csv)

# z, data_txt = DataSource().dataSourceConn('mock.txt')
# print(data_txt)