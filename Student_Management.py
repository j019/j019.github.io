import tkinter as tk
import tkinter.messagebox
def database2(name,address,phone):
    import sqlite3
    connection = sqlite3.connect("student_record1.db")
    print("database opened successfully.")

    table_name = "student_record"
    student_id = "student_id"
    student_name = "student_name"
    student_college = "student_college"
    student_address = "student_address"
    student_phone = "student_phone"

    connection.execute(
        " CREATE TABLE IF NOT EXISTS " + table_name + "( " + student_id + " INTEGER PRIMARY KEY AUTOINCREMENT, " + student_name +
        " TEXT, " + student_college + " TEXT, " + student_address + " TEXT, " + student_phone + " INTEGER);")

    print("Table created successfully.!!")

    connection.execute("INSERT INTO " + table_name + "( "+ student_name + ", "+ student_college+", "+student_address+", "+
                       student_phone+") VALUES ('"+name+"','BFIT','"+address+"',"+str(phone)+");")
    connection.commit()

class Student:
    def __init__(self):
        self.mainWindow=tk.Tk()
        self.mainWindow.title("Student Management System")
        self.mainWindow.geometry('900x500+400+100')

        self.heading1=tk.Label(self.mainWindow,text="Welcome to Student Management System!!\n",fg="red",font=("algerian",20,"italic","bold"))
        self.heading1.grid(row=0,column=5)

        self.heading2=tk.Label(self.mainWindow,text="\nEnter Student Name:\n",fg="green")
        self.heading2.grid(row=1,column=4)

        self.Name=tk.Entry(self.mainWindow)
        self.Name.grid(row=1,column=7)

        self.heading3=tk.Label(self.mainWindow,text="\nEnter Student's Course:\n",fg="green")
        self.heading3.grid(row=2,column=4)

        self.Course=tk.Entry(self.mainWindow)
        self.Course.grid(row=2,column=7)

        self.heading4=tk.Label(self.mainWindow, text="\nEnter Student's PhoneNo:\n",fg="green")
        self.heading4.grid(row=3,column=4)

        self.PhoneNo=tk.Entry(self.mainWindow)
        self.PhoneNo.grid(row=3,column=7)

        def getvalues():
            name1=(self.Name.get())
            course1=(self.Course.get())
            phone1=int(self.PhoneNo.get())
            print("The Name of the Student is: ", name1, "\nThe Course Student had Opted is: ", course1,
                  "\nThe PhoneNo of Student is: ", phone1)
            c=database2(name1,course1,phone1)

        def take_input():
            self.Name.delete('0',tk.END)
            self.Course.delete('0',tk.END)
            self.PhoneNo.delete('0',tk.END)

        def retrieve():
            import sqlite3
            connection = sqlite3.connect("student_record1.db")
            print("database opened successfully.")

            table_name = "student_record"
            student_id = "student_id"
            student_name = "student_name"
            student_college = "student_college"
            student_address = "student_address"
            student_phone = "student_phone"

            cursor = connection.execute("Select * From " + table_name + " ;")

            for row in cursor:
                print("Student id is: ", row[0])
                print("Student name is: ", row[1])
                print("Student college is: ", row[2])

            connection.close()


        self.button=tk.Button(self.mainWindow,text="Display_Input",fg="blue",command=lambda: getvalues())
        self.button.grid(row=8,column=7)

        self.button=tk.Button(self.mainWindow,text="Take_Input",fg="blue",command=lambda: take_input())
        self.button.grid(row=8,column=4)

        self.button=tk.Button(self.mainWindow,text="Retrieve_Record",fg="red",bg="steel blue",command=lambda: retrieve())
        self.button.grid(row=8,column=5)

        self.mainWindow.mainloop()

b=Student()