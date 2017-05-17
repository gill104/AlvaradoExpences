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


class SalesInformation():
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
class MenuVariableHolder():
    def __init__(self):
        self.__MenuVendor = 'N/A'
        self.__MenuStartDate = 'N/A'
        self.__MenuEndDate = 'N/A'
        
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
        
    def getMenuVendor(self):
        return self.__MenuVendor
    def getMenuStartDate(self):
        return self.__MenuStartDate
    def getMenuEndDate(self):
        return self.__MenuEndDate
    
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
            
            
def loadMemory():
    d = DictionaryHash()
    d.loadDictionary()
    mvh = MenuVariableHolder()
    return(d,mvh)
   # main(d, True,t)

def main(d, regular,t):
    #userinterface and booleans to check user input
     
    #d = DictionHash
    #regular = True
    
    #loop getting user input
    while(regular):
        if(mainMenu(d,t) == False):
            #print('False!')
            regular = False
            main(d,regular,t)
            
    while(regular == False):
        if(salesMenu(t) == True):
            #print('True')
            regular = True
            main(d,regular,t)

def mainMenu(d,t):
        #os.system('clear')
        cls()
        center = '\t\t\t\t'
        left = '\t\t|'  
        print(left + '*EXPENCES MENU*'.ljust(46) + ' |')
        print(('\t\t*').ljust(50,'=')+'*')
        print('\t\t   Focused Vendor: ' + t.getMenuVendor() + ' || Date Range: ' + t.getMenuStartDate() + ' - ' +t.getMenuEndDate() )
        print(('\t\t*').ljust(50,'=')+'*')
        print(left + ('1. Add new item').ljust(23) +  '|'.ljust(2) + '6. Get total [all]    |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('2. Specify Company').ljust(23) + '|'.ljust(2) + '7. Get total [Card]   |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('3. Specify date range').ljust(23) + '|'.ljust(2) + '8. Get total [Cash]   |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('4. Clear Vendor').ljust(23) + '|'.ljust(2) + '9. Get total [EBT]    |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('5. Clear Date').ljust(23) + '|'.ljust(2) + '0. Switch to Sales    |')
      
        
        print(('\t\t*').ljust(50,'=')+'*')
        print('\t\t ' + 'Select choice:', end='')
        usrInput = input()
        if(expenceChoices(usrInput, d,t) == False):
            return(False)
        else:
            return(True)
def salesMenu(t):
        os.system('clear')
        cls()
        center = '\t\t\t\t'
        left = '\t\t|' 
        print(left + '*SALES MENU*'.ljust(46) + ' |')
        print(('\t\t*').ljust(50,'=')+'*')
        print(left + 'Focused Vendor: ' + t.getMenuVendor() + ' || Date Range: ' + t.getMenuStartDate() + ' - ' +t.getMenuEndDate() )
        print(('\t\t*').ljust(50,'=')+'*')
        print(left + ('1. Add Sales').ljust(23) +  '|'.ljust(2) + '5. Show total [all]  |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('                     ').ljust(23) + '|'.ljust(2) + '7. Show total [Card]  |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('3. Specify date range').ljust(23) + '|'.ljust(2) + '8. Show total [Cash]  |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('                     ').ljust(23) + '|'.ljust(2) + '9. Show total [EBT]   |')
        print('\t\t|' + ('-----------------------------------------------|'))
        print(left + ('                     ').ljust(23) + '|'.ljust(2) + '0. Switch to Expences |')
      
        
        print(('\t\t*').ljust(50,'=')+'*')
        usrInput = input()
        if(saleChoices(usrInput,t) == True):
            return(True)
        else:
            return(False)
def demo(thing):
    print(thing)
def expenceChoices(usrInput, d,t):
        #allows user to add a new item to the file  
        if(usrInput == '1'):
            #t = InformationStorage()
            t = ExpenceStorage() 
            os.system('clear')
            print('Enter Invoice Num:', end='')
            usrInput = gui.test()
            usrInput = input()
            t.setInvoiceNumber(usrInput)

            while(True):
                print('Enter Date(mm-dd-yyyy):', end='')
                usrInput = input()
                if(dateCheck(usrInput) == True):
                    t.setDate(usrInput)
                    break
                
            print('Enter Vendor:', end='')
            usrInput = input().lower()
            t.setVendor(usrInput)
            
            print('Enter Product:', end='')
            usrInput = input()
            t.setProduct(usrInput)
            
            print('Enter Payment Method(Cash/Card/EBT):', end='')
            usrInput = input()
            t.setPayMethod(usrInput)

            while(True):
                print('Enter Payment Amount:', end='')
                usrInput = input()
                if(paymentCheck(usrInput) == True):
                    t.setPayAmount(usrInput)
                    break
                
            print('Enter Notes:', end='')
            usrInput = input()
            if(usrInput == ''):
                usrInput = 'N/A'
            t.setNotes(usrInput)
            
            print('Do you want to save the file? (y/n)')
            usrInput = input()
            if(usrInput.lower() == 'y'):
                t.saveToFile('TestDocuement.txt')
                d.setDictionary(t.getVendor(),t.getData())
                d.saveDictionary()
            cls()
            return(True)
        #allows user to select vendor  
        elif(usrInput == '2'):
            os.system('clear')
            print('Enter ventor Name: ', end ='')
            usrInput= input()
            focusedCompany = usrInput.lower()
            t.setMenuVendor(focusedCompany)
            cls()
            return(True)
                
        #allows user to specify a date for expences retreval
        elif(usrInput == '3'):
            os.system('clear')
            #print('*for single date [leave end date empty]*')
            while(True):
                print('Enter Start Date(mm-dd-yyyy):')
                startDate = input()
                if(dateCheck(startDate) == True):
                    break

            #print('startDate: ', startDate)
            t.setMenuStartDate(startDate)
            print('*Leave blank for single Day*')
            print('Enter End Date(mm-dd-yyyy):')
            endDate = input()
            if(endDate != ''):
                t.setMenuEndDate(endDate)
            '''if(endDate == ''):
                endDate = 'N/A'
                print('Blank End Date')
            if(startDate == ''):
                startDate = 'N/A'
                print('Blank Start Date')
            startList = startDate.split('-')
            endList = endDate.split('-')
            focusedDate = startDate + ' - ' + endDate'''
            return(True)
        elif(usrInput == '4'):
            os.system('clear')
            t.setMenuVendor('N/A')
            cls()
            return(True)
        elif(usrInput == '5'):
            os.system('clear')
            t.setMenuStartDate('N/A')
            t.setMenuEndDate('N/A')
            cls()
            return(True)
        #allows user to get all expences with parameters for specification
        elif(usrInput == '6'):
            os.system('clear')
            print('')
            totalTypeSpec('N/A', t,d)
            #totalTypeSpec('N/A',focusedCompany, startDate, endDate)
            cls()
            return(True)
          
        elif(usrInput == '7'):
            os.system('clear')
            totalTypeSpec('card', t.d)
            #totalTypeSpec('card',focusedCompany,startDate,endDate)
            cls()
            return(True)

        elif(usrInput == '8'):
            os.system('clear')
            totalTypeSpec('cash', t,d)
            #totalTypeSpec('cash',focusedCompany,startDate,endDate)
            cls()
            return(True)
        elif(usrInput == '9'):
            os.system('clear')
            totalTypeSpec('ebt', t,d)
            #totalTypeSpec('ebt',focusedCompany,startDate,endDate)
            cls()
            return(True)
        elif(usrInput == '0'):
            os.system('clear')
            #salesMenu(t)
            return(False)
        else:
            print('lasdasdet')

def saleChoices(usrInput,t):
    if(usrInput == '1'):
        print('Enter sales date (mm-dd-yyyy): ')
    elif(usrInput == '2'):
        print('Enter [Card] sales:')
    elif(usrInput == '3'):
        print('Enter Start Date(mm-dd-yyyy):')
        startDate = input()
        t.setMenuStartDate(startDate)
        
        print('*Leave blank for single Day*')
        print('Enter End Date(mm-dd-yyyy):')
        endDate = input()
        t.setMenuEndDate(endDate)
    elif(usrInput == '0'):
        return(True)

def exitCheck(usrInput):
     if(usrInput.lower() == 'exit'):
         return True
        
def paymentCheck(usrInput):
    if(usrInput == ''):
        return False
    for x in range(len(usrInput)):
        if(not usrInput[x].isdigit()):
            if(usrInput[x] == '.'):
                continue
            else:
                print('Numbers (0-9) only')
                return False
    return True

def dateCheck(usrInput):
    daysPerMonth = {'1': 31, '3':31, '4':30, '5':31, '6':30, '7':31, '8':31,'9':30,'10':31,'11':30,'12':31}

    DateList = usrInput.split('-')
    for x in range(len(DateList)):
        if(not DateList[x].isdigit()):
            print('Numbers(0-9) and \' - \' only')
            return False
        
    if(len(usrInput) == 10):
        monthDigit = int(DateList[0])
        if(monthDigit > 12 or monthDigit < 1):
            print('Months 1 - 12')
            return False
        
        yearDigit = int(DateList[2])
        if((len(str(yearDigit)) != 4)):
            print('Only 4 digits')
            return False
        
        dayDigit = int(DateList[1])
        #leapYear
        if(monthDigit == 2):
            if(int(yearDigit) % 4 == 0):
                if(dayDigit <= 29 and dayDigit > 0):
                    return True
                else:
                    print('Month  ' + str(monthDigit) + ' contains 29 days')
                    print(dayDigit)
                    
                    return False
            else:
                if(dayDigit <= 28 and dayDigit > 0):
                    return True
                else:
                    print('Month ' + str(monthDigit) + ' contains 28 days')
                    print(dayDigit)
                    
                    return False
         #regular       
        else:
            '''if(str(monthDigit) in daysPerMonth.keys()):
                print('Month: ' + str(monthDigit) + 'Days: ' + str(daysPerMonth.get(str(monthDigit))))'''
            if( not (dayDigit <= (daysPerMonth.get(str(monthDigit))) and dayDigit > 0)):
                print('Month '  + str(monthDigit) + ' contains ' + str(daysPerMonth.get(str(monthDigit))))
                return False
            else:
                #print('date is Good')
                return True
    else:
        print('NOT a 10 digit value')
        return False
    return True

'''
*Attemps to clear the screen when not using the
*   terminal, makes it a bit easier to read
'''
def cls():
    print('='*150 + '\n'*3)

'''
*This function gets the 7 lines within the file
*     and creates a list in order to be able to
*     read the each peice of information the user
*     has inputed
'''
def getBlock(block, file, line,tempList):
    for x in range(block):
        line = line.rstrip('\n')
        tempList.append(line)
        if(x != (block-1)):
            line = file.readline()
    return tempList

'''
*Function is used to check the search conditions the
*     user has specified in the main menu, these
*     vary from having both dates present to vendor
*
*Might be a better way to search for information..pending
'''
def totalTypeSpec(payType,t,d):
    file = open('TestDocuement.txt','r')
    total = 0.0
    block = 7
    tempList = []
    tempDict = d.getDictionary()
    #*Nothing is focused for search. Gets all expenses, can specify payment type'''
    if(t.getMenuVendor() == 'N/A' and t.getMenuStartDate() == 'N/A' and t.getMenuEndDate() == 'N/A'):
        for k,v in tempDict.items():
            for x in range(len(v)):
                if(payType == 'N/A'):
                    total += float(v[x][5])
                    print('None Focused total: ' , total)
                else:
                    if(v[x][4] == payType):
                        total += float(v[x][5])
                        print('None Focused total: ' , total)
            

        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            if(payType == 'N/A'):
                total += float(tempList[5])
            else:
                if(tempList[4].lower() == payType):
                    total += float(tempList[5])
            tempList = []'''
    #*Single Date is Focused searches for that days sales, can specify payment type'''
    elif(t.getMenuVendor() == 'N/A' and t.getMenuStartDate() != 'N/A' and t.getMenuEndDate() == 'N/A'):
        
        #startDateList = t.getMenuStartDate().split('-')
        for k,v in tempDict.items():
            for x in range(len(v)):
                if(payType == 'N/A' and v[x][1] == t.getMenuStartDate()):
                    print('dates the same!')
                    total += float(v[x][5])
                    print('Start ony focused total: ', total)
                else:
                    if(v[x][4] == payType and v[x][1] == t.getMenuStartDate()):
                        total += float(v[x][5])
                        print('Start ony focused total: ', total)

        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            dateList = tempList[1].split('-')
            #print(tempList)
            if(payType == 'N/A'):
                if(dateList == startDateList):
                    total += float(tempList[5])
            else: 
                if(dateList == startDateList and tempList[4].lower() == payType):
                    #print('date match!') 
                    total += float(tempList[5])
            tempList = []'''
    #*Both Date is Focused searches for the sales, can specify payment type
    elif(t.getMenuVendor() == 'N/A' and t.getMenuStartDate() != 'N/A' and t.getMenuEndDate() != 'N/A'):
        
        startDate = time.strptime(t.getMenuStartDate(), '%m-%d-%Y')
        endDate = time.strptime(t.getMenuEndDate(), '%m-%d-%Y')
        #startDate = normalizeDates(startDate)
        #endDate = normalizeDates(endDate)
        for k,v in tempDict.items():
            for x in range(len(v)):
                dictTime = time.strptime(v[x][1], '%m-%d-%Y')
                if(payType == 'N/A' and dictTime >= startDate and dictTime <= endDate):
                    total += float(v[x][5])
                    print('Both dateFocused total: ', total)
                else:
                    if(v[x][4] == payType and dictTime >= startDate and dictTime <= endDate):
                        total += float(v[x][5])
                        print('Both dateFocused total: ', total)
        
        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            dateList =  time.strptime(tempList[1], '%m-%d-%Y')
            if(payType == 'N/A'):
                if(dateList >= startDate and dateList <= endDate):
                    #print(dateList)
                    total += float(tempList[5])
            else:
               if(dateList >= startDate and dateList <= endDate and tempList[4].lower() == payType):
                   #print('date match!') 
                   total += float(tempList[5])
            tempList = []'''
    #*Both Dates are Focused and company as well searches for the sales, can specify payment type
    elif(t.getMenuVendor() !='N/A' and t.getMenuStartDate() != 'N/A' and t.getMenuEndDate() != 'N/A'):
        
        startDate =  time.strptime(t.getMenuStartDate(), '%m-%d-%Y')
        endDate =  time.strptime(t.getMenuEndDate(), '%m-%d-%Y')

        for k,v in tempDict.items():
            if(payType == 'N/A' and k.lower() == t.getMenuVendor()):
                for x in range(len(v)):
                    dictTime = time.strptime(v[x][1], '%m-%d-%Y')
                    if(dictTime >= startDate and dictTime <= endDate):
                        total += float(v[x][5])
                        print('Both dateFocused companyFocused total: ', total)
            else:
                if(k.lower() == t.getMenuVendor()):
                    for x in range(len(v)):
                        dictTime = time.strptime(v[x][1], '%m-%d-%Y')
                        if(v[x][4] == payType and dictTime >= startDate and dictTime <= endDate):
                            total += float(v[x][5])
                            print('Both dateFocused companyFocused total: ', total)
        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            dateList =  time.strptime(str(tempList[1]), '%m-%d-%Y')
            if(payType == 'N/A'):
                if(dateList >= startDate and dateList <= endDate
                             and tempList[2].lower() == t.getMenuVendor()):
                    total += float(tempList[5])
            else:
                if(dateList >= startDate and dateList <= endDate
                             and tempList[2].lower() == t.getMenuVendor()
                             and tempList[4].lower() == payType):
                    #print('date match!') 
                    total += float(tempList[5])
            tempList = []'''
    #*Only Vendor Focused searches for the sales, can specify payment type
    elif(t.getMenuVendor() != 'N/A' and t.getMenuStartDate() == 'N/A' and t.getMenuEndDate() == 'N/A'):
        
        for k,v in tempDict.items():
            if(payType == 'N/A' and k.lower() == t.getMenuVendor()):
                for x in range(len(v)):
                    total += float(v[x][5])
                    print('Company Focused total: ', total)
            else:
                if(k.lower() == t.getMenuVendor()):
                    for x in range(len(v)):
                        if(payType == v[x][4]):
                            total += float(v[x][5])
                            print('Company Focused total: ', total)

        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            if(payType == 'N/A'):
                if(tempList[2].lower() == t.getMenuVendor()):
                    total += float(tempList[5])
            else:
                #print('FocusedCompany: ' + focusedCompany)
                if(tempList[4].lower() == payType and tempList[2].lower() == t.getMenuVendor()):
                    total += float(tempList[5])
            tempList = []'''
    #*Single Date and Company Focused searches for that days sales, can specify payment type
    elif(t.getMenuVendor() != 'N/A' and t.getMenuStartDate() != 'N/A' and t.getMenuEndDate() == 'N/A'):
        #print('Company Focused and Start only')
        startDateList = t.getMenuStartDate().split('-')
        #print('here')
        for k,v in tempDict.items():
            if(payType == 'N/A' and k.lower() == t.getMenuVendor()):
                for x in range(len(v)):
                    if(v[x][1] == t.getMenuStartDate()):
                        total += v[x][5]
                        print('Company Focused and Start only: ', total)
            else:
                if(k.lower() == t.getMenuVendor()):
                    for x in range(len(v)):
                        if(payType == v[x][4] and v[x][1] == t.getMenuStartDate()):
                            total += float(v[x][5])
                            print('Company Focused and Start only: ', total)
        '''for line in file:
            tempList = getBlock(block,file, line,tempList)
            dateList = tempList[1].split('-')
            if(payType == 'N/A'):
                if(dateList == startDateList and tempList[2].lower() == t.getMenuVendor()):
                    total += float(tempList[5])
            else:
                if(dateList == startDateList and tempList[4].lower() == payType 
                                     and tempList[2].lower() == t.getMenuVendor()):
                    total += float(tempList[5])
            tempList = []'''
    else:
        print('no Data found')

#loadMemory()
