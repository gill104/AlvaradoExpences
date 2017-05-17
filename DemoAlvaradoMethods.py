import os
from DemoAlvarado import ExpenceStorage
def expenceChoices(invoice,t):
        #allows user to add a new item to the file  
        #if(usrInput == '1'):
            #print(uI1 + uI2 + uI3 + uI4 + uI5 + uI6 + uI7)
            #t = InformationStorage()
            #t = ExpenceStorage()
            
            #os.system('clear')
            #print('Enter Invoice Num:', end='')
            #usrInput = input()
            
            t.setInvoiceNumber(invoice)
            print(t.getInvoiceNumber())
def gui_date(t,date):
    while(True):
        if(dateCheck(date) == True):
            t.setDate(date)
            return(True)
        else:
            return(False)
def gui_vendor(t,vendor):
    lowerVendor = vendor.lower()
    t.setVendor(lowerVendor)

def gui_product(t,product):
    t.setProduct(product)

def gui_payType(t,paytype):
    t.setPayMethod(paytype)
def gui_amount(t, amount):
    while(True):
        if(paymentCheck(amount) == True):
            t.setPayAmount(amount)
            return(True)
        else:
            return(False)
def gui_notes(t, notes):
    if(notes == ''):
        notes = 'N/A'
        t.setNotes(notes)
            
    '''print('Do you want to save the file? (y/n)')
            usrInput = input()
            if(usrInput.lower() == 'y'):
                t.saveToFile('TestDocuement.txt')
                d.setDictionary(t.getVendor(),t.getData())
                d.saveDictionary()
            cls()
            return(True)'''
def paymentCheck(amount):
    print('amount: ' , amount)
    if(amount == ''):
        return False
    for x in range(len(amount)):
        if(not amount[x].isdigit()):
            if(amount[x] == '.'):
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
