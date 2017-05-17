'''
*Created by: Gilbert Salazar
*Description: To provide a log for all expences and sales for 'Alvarado's Bakery'
*
*Implement Dictionary properly to load and save data.
*create a class for menuVendor/MenuStart/MenuEnd
*Fix errors due to moving expence instance to proper location
*deal with memory issue (delete the instance made)
*general cleanup of definition
*
'''
import sys
import os
import time
import pickle
#import GUI as gui
#simple class that stores user information into a list format
class ExpenceStorage:
    def __init__(self):
        self.__InvoiceNumber = 'N/A'
        self.__Date = 'N/A'
        self.__Vendor = 'N/A'
        self.__Product = 'N/A'
        self.__PayMethod = 'N/A'
        self.__Notes = 'N/A'
        self.__PayAmount = 0.0

        
        #self.name = ''
        #self.value = 0.0
        #might not need this list 
        self.__Data = [
                            self.__InvoiceNumber,
                            self.__Date,
                            self.__Vendor,
                            self.__Product,
                            self.__PayMethod,
                            self.__PayAmount,
                            self.__Notes
                          ]
    
    def setInvoiceNumber(self, invoiceNum):
        self.__Data[0] = invoiceNum
    def setDate(self, date):
        self.__Data[1] = date
    def setVendor(self, vendor):
        self.__Data[2] = vendor
    def setProduct(self, product):
        self.__Data[3] = product
    def setPayMethod(self, method):
        self.__Data[4] = method
    def setPayAmount(self, amount):
        self.__Data[5] = amount
    def setNotes(self, notes):
        self.__Data[6] = notes

        
    def getInvoiceNumber(self):
        return self.__Data[0]
    def getDate(self):
        return self.__Data[1]
    def getVendor(self):
        return self.__Data[2]
    def getProduct(self):
        return self.__Data[3]
    def getPayMethod(self):
        return self.__Data[4]
    def getPayAmount(self):
        return self.__Data[5]
    def getNotes(self):
        return self.__Data[6]


    #saves user information into an external file        
    def saveToFile(self, fileName):
        file = open(fileName,'a+')
        file.write(
                        self.__Data[0] + '\n' +
                        self.__Data[1] + '\n' +
                        self.__Data[2] + '\n' +
                        self.__Data[3] + '\n' +
                        self.__Data[4] + '\n' +
                        self.__Data[5] + '\n' +
                        self.__Data[6] + '\n')
        file.close()
                            
        print('Data Saved...press [any button to continue]')
        file = open('usrFile.txt','a+')
        file.write(
                        self.__Data[0] + '\t' +
                        self.__Data[1] + '\t' +
                        self.__Data[2] + '\t' +
                        self.__Data[3] + '\t' +
                        self.__Data[4] + '\t' +
                        self.__Data[5] + '\t' +
                        self.__Data[6] + '\n')
        file.close()
        #input()
        os.system('clear')
        #with open('data.pickle','wb') as f:
        #    pickle.dump(self.__Data,f,pickle.HIGHEST_PROTOCOL)

    def getData(self):
        print(self.__Data)
        return self.__Data
    
    def printList(self):
            print(self.__Data)
            with open('data.pickle', 'rb') as f:
                while(True):
            
                    try:
                      self.readData = pickle.load(f)
                      print('Read Data: ' , self.readData)
                    except EOFError:
                        break


'''class SalesInformation():
    def __init__(self):
        self.__Total = 0.0
        self.__CardTotal = 0.0
        self.__CashTotal = 0.0
        self.__EbtTotal = 0.0

    def setTotal(self, total):
        self.__Total = total
    def setCardTotal(self, cardTotal):
        self.__CardTotal = cardTotal
    def setCashTotal(self, cashTotal):
        self.__CashTotal = cashTotal
    def setEbtTotal(self, ebtTotal):
        self.__EbtTotal = ebtTotal

    def getTotal(self):
        return self.__Total
    def getCardTotal(self):
        return self.__CardTotal
    def getCashTotal(self):
        return self.__CashTotal
    def getEbtTotal(self):
        return self.__EbtTotal

    def saveToFile(self, fileName):
        file = open(fileName, 'a+')
        file.write(
                    self.__Total + '\n' +
                    self.__CardTotal + '\n' +
                    self.__CashTotal + '\n' +
                    self.__EbtTotal + '\n'
                 )
        file.close()
        print('Data saved...press [Any button to continue]')
        input()
        os.system('clear')
    '''
class MenuVariableHolder():
    def __init__(self):
        self.__MenuVendor = 'N/A'
        self.__MenuStartDate = 'N/A'
        self.__MenuEndDate = 'N/A'
        self.__MenuPayType = 'N/A'

    def setMenuVendor(self, menuVendor):
        self.__MenuVendor = menuVendor
    def setMenuStartDate(self,menuStartDate):
        #print('here: ', menuStartDate)
        if(menuStartDate != ''):
            self.__MenuStartDate = menuStartDate
        else:
            self.__MenuStartDate = 'N/A'
    def setMenuEndDate(self, menuEndDate):
        if(menuEndDate != ''):
            self.__MenuEndDate = menuEndDate
        else:
            self.__MenuEndDate = 'N/A'
    def setMenuPayType(self, menuPayType):
        self.__MenuPayType = menuPayType

    def getMenuVendor(self):
        return self.__MenuVendor
    def getMenuStartDate(self):
        return self.__MenuStartDate
    def getMenuEndDate(self):
        return self.__MenuEndDate
    def getMenuPayType(self):
        return self.__MenuPayType

class DictionaryHash():
    def __init__(self):
        self.__d = {}
        self.__l = []

    def setDictionary(self, key, value):

        print('key: ', key)
        print('Value: ', value, '\n')
        if(key not in self.__d.keys()):
            self.__d[key] = []
            self.__d[key].append(value)
            '''self.__d = {}
            self.__d[key] = []
            print('created new empty List for ', key, '\n')
            print('should be empty: ', self.__d)
            self.__d[key].append(value)
            print('newItem Added: ' , self.__d, '\n')'''

        else:
            self.__d.setdefault(key, [])
            self.__d[key].append(value)

    def getDictionary(self):
        return self.__d
    def saveDictionary(self):
        with open('Diction.data.pickle','wb') as f:
            print('Im saving this: ' , self.__d)
            pickle.dump(self.__d,f,pickle.HIGHEST_PROTOCOL)

    def loadDictionary(self):
        try:
            with open('Diction.data.pickle', 'rb') as f:
                #while(True):
                    try:
                        self.__d = pickle.load(f)
                        print('Reading Dictionary')
                        for k,v in self.__d.items():
                            print('k: ', k)
                            print('v: ', v)
                    except EOFError:
                        print('blaj')
        except FileNotFoundError:
           file = open('Diction.data.pickle','a+')
           file.close()
    def selectVendor(self):
        vendorList = ['N/A']
        for k,v in self.__d.items():
            print("Keys: ", k)
            vendorList.append(k)
        return vendorList

def loadMemory():
    d = DictionaryHash()
    d.loadDictionary()
    mvh = MenuVariableHolder()
    return(d,mvh)