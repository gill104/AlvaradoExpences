import DemoAlvarado as da
import DemoAlvaradoMethods as dam
import tkinter as tk
from tkinter import messagebox

class demoTK(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.d, self.mvh = da.loadMemory()
        self.t = da.ExpenceStorage()
        # self.m = da.MenuVariableHolder()
        self.selected_vendor = 'N/A'
        self.topLeftFrame = tk.Frame(self)
        self.topLeftFrame.grid(row=0)

        self.topRightFrame = tk.Frame(self)
        self.topRightFrame.grid(row = 0, column=2)

        self.leftFrame = tk.Frame(self)
        self.leftFrame.grid(row=1,column=2)

        self.textFrame = tk.Frame(self)
        self.textFrame.grid(row=2,column=0,columnspan=6, sticky='NSWE')

        self.botFrame = tk.Frame(self)
        self.botFrame.grid(row=3,column=0, columnspan=2, sticky='W')

        tk.Frame.config(self, padx=10, pady=10)
        self.variable = tk.StringVar(root)
        self.string_invoice = tk.StringVar(root)
        self.string_date = tk.StringVar(root)
        self.string_vendor = tk.StringVar(root)
        self.string_product = tk.StringVar(root)
        self.string_paytype = tk.StringVar(root)
        self.string_amount = tk.StringVar(root)
        self.string_notes = tk.StringVar(root)
        self.start_focused_date = tk.StringVar(root, value='N/A')
        self.end_focused_date = tk.StringVar(root, value='N/A')
        self.radio_choice = tk.IntVar(root)

        self.menu()
        self.VendorDD()
        self.pack()

    def menu(self):
        self.vendor_label = tk.Label(self.topLeftFrame, text='Focused Vendor: ')
        self.vendor_label.pack(side=tk.LEFT)

        self.date_label = tk.Label(self.topRightFrame, text='Focused Date: ')
        self.date_label.pack(side=tk.LEFT)

        self.add_button = tk.Button(self, text='1.) Add new entry', borderwidth=2, highlightthickness= 3, highlightbackground='green',
                                    command=self.addNewItem).grid(row=1, padx=5, pady=3)

        self.all_button = tk.Button(self.leftFrame, text='2.) Get total [ALL]',borderwidth=2, highlightthickness= 3, highlightbackground='blue', command=self.findAll)
        self.all_button.pack(side=tk.LEFT)
        self.all_button.config(width=15, relief="raised")
        '''##############################################################################'''
        self.type_radio = tk.Radiobutton(self.leftFrame, text='ALL', variable=self.radio_choice,
                                         value=0, command=self.modButton)
        self.type_radio.pack(side=tk.LEFT)

        self.type_radio = tk.Radiobutton(self.leftFrame, text='CARD', variable=self.radio_choice,
                                         value=1, command=self.modButton)
        self.type_radio.pack(side=tk.LEFT)

        self.type_radio = tk.Radiobutton(self.leftFrame, text='CASH', variable=self.radio_choice,
                                         value=2, command=self.modButton)
        self.type_radio.pack(side=tk.LEFT)
        self.type_radio = tk.Radiobutton(self.leftFrame, text='EBT', variable=self.radio_choice,
                                         value=3, command=self.modButton)
        self.type_radio.pack(side=tk.LEFT)
        '''##############################################################################'''
        self.start_date_entry = tk.Entry(self.topRightFrame, textvariable=self.start_focused_date)
        self.start_date_entry.pack(side=tk.LEFT)

        self.dash_label = tk.Label(self.topRightFrame, text='-', width=5).pack(side=tk.LEFT)

        self.end_date_entry = tk.Entry(self.topRightFrame, textvariable=self.end_focused_date)
        self.end_date_entry.pack(side=tk.LEFT)

        self.total_label = tk.Label(self.botFrame, text='Total: ')
        self.total_label.pack(side=tk.LEFT)
        self.total_label.config(font = (tk.NONE, 30))

        self.result_label = tk.Label(self.botFrame, text=' ', justify=tk.LEFT)
        self.result_label.pack(side = tk.LEFT)
        self.result_label.config(font = (tk.NONE, 30))

        self.display_menu = tk.Text(self.textFrame, borderwidth=3,
                                    state=tk.DISABLED)
        '''this may work may not'''
        self.scrollbar = tk.Scrollbar(self.textFrame, orient=tk.VERTICAL,command=self.display_menu.yview)

        '''##################'''

        self.display_menu['yscroll'] = self.scrollbar.set
        self.scrollbar.pack(side = tk.RIGHT, fill=tk.Y)
        self.display_menu.pack(side = tk.LEFT,fill = tk.BOTH,expand = tk.TRUE)


        self.quit = tk.Button(self, text="QUIT", fg="red",borderwidth=0, highlightthickness= 2, highlightbackground='red', command=root.destroy)
        self.quit.grid(row=4, column=0, columnspan=4, sticky='WNSE')

    def modButton(self):
        if (self.radio_choice.get() == 0):
            self.all_button['text'] = '2.) Get total [ALL]'
            self.mvh.setMenuPayType('N/A')
        elif (self.radio_choice.get() == 1):
            self.all_button['text'] = '2.) Get total [CARD]'
            self.mvh.setMenuPayType('card')
        elif (self.radio_choice.get() == 2):
            self.all_button['text'] = '2.) Get total [CASH]'
            self.mvh.setMenuPayType('cash')
        elif (self.radio_choice.get() == 3):
            self.all_button['text'] = '2.) Get total [EBT]'
            self.mvh.setMenuPayType('ebt')
            # self.all_button['text'] = 'Get total [' + str(self.radio_choice.get()) + ']'

    def findAll(self):

        self.start_date_bool = 0
        self.end_date_bool = 0

        if (self.start_focused_date.get() != 'N/A'):
            print('ere')
            print(self.start_focused_date.get())
            if (dam.dateCheck(self.start_focused_date.get()) == True):
                self.mvh.setMenuStartDate(self.start_focused_date.get())
                self.start_date_bool = 1
            else:
                print('start date wrong!')
        else:
            self.mvh.setMenuStartDate('N/A')
            self.start_date_bool = 1

        if (self.end_focused_date.get() != 'N/A'):
            if (dam.dateCheck(self.end_focused_date.get()) == True):
                self.mvh.setMenuEndDate(self.end_focused_date.get())
                self.end_date_bool = 1
        else:
            self.mvh.setMenuEndDate('N/A')
            self.end_date_bool = 1

        if (self.start_date_bool == 1 and self.end_date_bool == 1):
            self.total, self.tempList = dam.totalTypeSpec(self.mvh, self.d)

            tk.messagebox.showinfo('Total', 'total: ' + str(self.total))
            self.result_label['text'] = str(self.total)

            self.display_menu.config(state=tk.NORMAL)
            self.display_menu.delete(1.0, tk.END)
            for x in range(len(self.tempList)):
                for y in range(len(self.tempList[x])):
                    self.display_menu.insert(tk.INSERT, self.tempList[x][y])
                    self.display_menu.insert(tk.INSERT, '\t')
                '''self.display_menu.insert(tk.INSERT, self.tempList[x])
                self.display_menu.insert(tk.INSERT, '\n')'''
                self.display_menu.insert(tk.INSERT, '\n')
            self.display_menu.config(state=tk.DISABLED)
        else:
            tk.messagebox.showinfo('Date Error', 'Date Format incorrect\nmm-dd-yyyy\nType \'N/A\' for no date')

    def VendorDD(self):
        self.vendorList = self.d.selectVendor()

        self.variable.set(self.vendorList[0])

        dropdown = tk.OptionMenu(self.topLeftFrame, self.variable, *self.vendorList,
                                 command=self.setMenuVendor)
        dropdown.pack(side=tk.LEFT)
        dropdown.config(relief="groove")

    def setMenuVendor(self, value):
        # print(value)
        self.mvh.setMenuVendor(value)
        print(self.mvh.getMenuVendor())

    def addNewItem(self):
        self.window = tk.Toplevel(root)
        self.window.grab_set()
        self.window.config(padx=5, pady=5)
        self.invoice_label = tk.Label(self.window, text='Invoice #: ').grid(row=1, sticky=tk.W)
        self.invoice_entry = tk.Entry(self.window, textvariable=self.string_invoice)
        self.invoice_entry.grid(row=1, column=1)

        self.date_label = tk.Label(self.window, text='Date: ').grid(row=2, sticky=tk.W)
        self.date_entry = tk.Entry(self.window, textvariable=self.string_date)
        self.date_entry.grid(row=2, column=1)

        self.vendor_label = tk.Label(self.window, text='Vendor: ').grid(row=3, sticky=tk.W)
        self.vendor_entry = tk.Entry(self.window, textvariable=self.string_vendor)
        self.vendor_entry.grid(row=3, column=1)

        self.product_label = tk.Label(self.window, text='Product: ').grid(row=4, sticky=tk.W)
        self.product_entry = tk.Entry(self.window, textvariable=self.string_product)
        self.product_entry.grid(row=4, column=1)

        self.paytype_label = tk.Label(self.window, text='Pay Type: ').grid(row=5, sticky=tk.W)
        self.paytype_entry = tk.Entry(self.window, textvariable=self.string_paytype)
        self.paytype_entry.grid(row=5, column=1)

        self.amount_label = tk.Label(self.window, text='Amount: ').grid(row=6, sticky=tk.W)
        self.amount_entry = tk.Entry(self.window, textvariable=self.string_amount)
        self.amount_entry.grid(row=6, column=1)

        self.notes_label = tk.Label(self.window, text='Notes: ').grid(row=7, sticky=tk.W)
        self.notes_entry = tk.Entry(self.window, textvariable=self.string_notes)
        self.notes_entry.grid(row=7, column=1)

        self.invoice_button = tk.Button(self.window, text='submit',
                                        command=self.submit_button)
        self.invoice_button.grid(row=8, columnspan=2, sticky='NSEW')
        # self.invoice_button.config(fg = "green")

    def submit_button(self):
        '''
         *Check to make sure all data i there b4 saving nothing blank
         *Then clear everything for future data input
        '''

        # print('Invoice NUM: ', self.t.getInvoiceNumber())
        dam.expenceChoices(self.string_invoice.get(), self.t)
        # print('HMMMM: ' , self.t.getInvoiceNumber())
        if (dam.gui_date(self.t, self.string_date.get()) == False):
            tk.messagebox.showinfo('Date Error', 'Date format mm-dd-yyy')
            self.date_entry.delete(0, tk.END)
            self.input_error1 = 1
        else:
            self.input_error1 = 0

        dam.gui_vendor(self.t, self.string_vendor.get())

        dam.gui_product(self.t, self.string_product.get())

        dam.gui_payType(self.t, self.string_paytype.get())

        if (dam.gui_amount(self.t, self.string_amount.get()) == False):
            tk.messagebox.showinfo('Amount Error', 'Only (0-9)')
            self.amount_entry.delete(0, tk.END)
            self.input_error2 = 1
        else:
            self.input_error2 = 0

        dam.gui_notes(self.t, self.string_notes.get())

        if (self.input_error1 == 0 and self.input_error2 == 0):
            self.t.saveToFile('TestDocument.txt')
            self.d.setDictionary(self.t.getVendor(), self.t.getData())
            self.d.saveDictionary()

            self.invoice_entry.delete(0, tk.END)
            self.date_entry.delete(0, tk.END)
            self.vendor_entry.delete(0, tk.END)
            self.product_entry.delete(0, tk.END)
            self.paytype_entry.delete(0, tk.END)
            self.amount_entry.delete(0, tk.END)
            self.notes_entry.delete(0, tk.END)

            self.window.destroy()
        else:
            tk.messagebox.showinfo('Error', 'Entry is empty!')
        self.VendorDD()


root = tk.Tk()
root.resizable(0,0)
app = demoTK(master=root)
app.mainloop()
