import DemoAlvarado as da
import DemoAlvaradoMethods as dam
import tkinter as tk
import sys

class demoTK(tk.Frame):
    def __init__(self,master =None):
        super().__init__(master)
        self.pack()
        self.create_widgets()
        self.string_invoice = tk.StringVar()
        self.string_date = tk.StringVar()
        self.string_vendor = tk.StringVar()
        self.string_product = tk.StringVar()
        self.string_paytype = tk.StringVar()
        self.string_amount = tk.StringVar()
        self.string_notes = tk.StringVar()


        self.d,self.mvh = da.loadMemory()
        
        
    def create_widgets(self):
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = "1.) Add new entry"
        self.hi_there["command"] = self.create_window
        self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text = "QUIT", fg="red",
                                      command=root.destroy)

        self.quit.pack(side="bottom")

    def create_window(self):
        self.window = tk.Toplevel(root)
        #dam.expenceChoices('1',self.d)
        self.t = da.ExpenceStorage()
        self.invoice_label = tk.Label(self.window,text = 'Invoice #: ').grid(row=0, sticky=tk.W)
        self.invoice_entry = tk.Entry(self.window,textvariable = self.string_invoice )
        self.invoice_button = tk.Button(self.window, text='submit',command=self.submit_button).grid(row=0,column=2)
        self.invoice_entry.grid(row=0,column=1)

        self.date_label = tk.Label(self.window,text = 'Date: ').grid(row=1, sticky=tk.W)
        self.date_entry = tk.Entry(self.window,textvariable = self.string_date )
        self.date_entry.grid(row=1,column=1)

        self.vendor_label = tk.Label(self.window,text = 'Vendor: ').grid(row=2, sticky=tk.W)
        self.vendor_entry = tk.Entry(self.window,textvariable = self.string_vendor)
        self.vendor_entry.grid(row=2,column=1)
        #self.invoice_button = tk.Button(self.window, text='submit',command=self.get_entry).grid(row=0,column=2)

        self.product_label = tk.Label(self.window,text = 'Product: ').grid(row=3, sticky=tk.W)
        self.product_entry = tk.Entry(self.window,textvariable = self.string_product )
        self.product_entry.grid(row=3,column=1)

        self.paytype_label = tk.Label(self.window,text = 'Pay Type: ').grid(row=4, sticky=tk.W)
        self.paytype_entry = tk.Entry(self.window,textvariable = self.string_paytype)
        self.paytype_entry.grid(row=4,column=1)

        self.amount_label = tk.Label(self.window,text = 'Amount: ').grid(row=5, sticky=tk.W)
        self.amount_entry = tk.Entry(self.window,textvariable = self.string_amount )
        self.amount_entry.grid(row=5,column=1)

        self.notes_label = tk.Label(self.window,text = 'Notes: ').grid(row=6, sticky=tk.W)
        self.notes_entry = tk.Entry(self.window,textvariable = self.string_notes )
        self.notes_entry.grid(row=6,column=1)

        
    def submit_button(self):
        '''
         *Check to make sure all data i there b4 saving nothing blank
         *Then clear everything for future data input
        '''
        #print('Invoice NUM: ', self.t.getInvoiceNumber())
        dam.expenceChoices(self.string_invoice.get(),self.t)
        #print('HMMMM: ' , self.t.getInvoiceNumber())
        if(dam.gui_date(self.t, self.string_date.get()) == False):
            tk.messagebox.showinfo('Date Error', 'Date format mm-dd-yyy')
            self.date_entry.delete(0, tk.END)
            
        dam.gui_vendor(self.t, self.string_vendor.get())
        
        dam.gui_product(self.t, self.string_product.get())
        
        dam.gui_payType(self.t, self.string_paytype.get())
        
        if(dam.gui_amount(self.t, self.string_amount.get()) == False):
            tk.messagebox.showinfo('Amount Error', 'Only (0-9)')
            self.amount_entry.delete(0,tk.END)
            
        dam.gui_notes(self.t, self.string_notes.get())

        self.t.saveToFile('TestDocument.txt')
        self.d.setDictionary(self.t.getVendor(), self.t.getData())
        self.d.saveDictionary()

        self.window.destroy()
            
       # print(passed_entry)
    def say_hi(self):
        print("Hi there, everyone!")
def test():
    print('erererrrrrrr')
root = tk.Tk()
app = demoTK(master=root)
app.mainloop()
