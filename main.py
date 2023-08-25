import db
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from tkcalendar import DateEntry


#bazw edw ta layouts kai ta fonts


class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Εxpense Τracker')
        self.geometry('600x400')

        style = ttk.Style(self)
        style.theme_use("clam")
        style.configure("Treeview.Heading", background="green", foreground="white")

        tree = ttk.Treeview(self,selectmode='browse')
        tree.grid(row=0, column=0, columnspan=4, padx=20, pady=20)


        tree["columns"] = ("1","2","3","4")
        tree.column("1", width=30, anchor='c')
        tree.column("2", width=100, anchor='c')
        tree.column("3", width=100, anchor='c')
        tree.column("4", width=100, anchor='c')
        tree.heading("1", text="id")
        tree.heading("2", text="Κατηγορία")
        tree.heading("3", text="Ποσό")
        tree.heading("4", text="Ημερομηνία")

        expenses = self.refresh()
        for item in expenses:
            tree.insert('', 'end', values= item)

        # scrollbar
        verscrlbar = ttk.Scrollbar(self, orient ="vertical",command = tree.yview)
        
        verscrlbar.grid(row=0, column=0, columnspan=4,padx=20,pady=20, sticky='nse')
        tree.configure(yscrollcommand = verscrlbar.set)

        #insert expense data
        Label(self, text="Ποσό", width= 10, height=1,font=('Sans Serif', 10, 'italic bold')).grid(column=0, row=1)
        entry_1 = Entry(self).grid(column=1, row=1)  

        Label(self, text="Κατηγορία Εξόδων", width= 15, height=1,font=('Sans Serif', 10, 'italic bold')).grid(column=2, row=1)
        entry_2 = Entry(self).grid(column=3, row=1) 

        cal = DateEntry(self, selectmode= 'day').grid(column=2,row=3)

        tk.Label(self).grid(column=3,row=3)

        Button(self, text="πρόσθεσε έξοδα", command=lambda: (self.insert(db.insert_expenses,entry_1,entry_2,cal))).grid(row=3,column=3)

        entry_3 = Entry(self).grid(row=5, column=1)
        Button(self, text="Διέγραψε την καταγραφή με id", command=lambda:(self.delete(db.delete_expense,entry_3))).grid(row=5, column=0)
    
        Button(self, text="Διαγραφή όλων", command=lambda:(db.delete_all())).grid(row=6, column=2)

        Button(self, text="Exit", command=self.Close).grid(column=3, row=5)
    
    def refresh(self):
        expenses = db.select_all_expenses()
        return expenses

    def insert(self, database, val1, val2, val3):
        category = val1.get()
        price = val2.get()
        date = val3.get()
    
        if category == '' or price == '' or date == '':
            return messagebox.showwarning('Warning', 'Empty Fields')
        else:
            insertion = database(category, price, date)
            self.added(self)
            return insertion
    
    def added(self, boxaile):
        myLabel = Label(boxaile, text="The value has been inserted")
        myLabel.grid(row=4, column=0)

    def delete(self,database,val):
        id = val.get()
        delete = database(id)
        return delete

    def Close(self):
        self.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()