from tkinter import* 
from tkinter import ttk
import pymysql
from tkinter import messagebox
class Student:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")
        

        title=Label(self.root,text="Student Management System",bd=10,relief=GROOVE,font=("time new roman",40,"bold"),bg="green4",fg="black")
        title.pack(side=TOP,fill=X)


        #.......Variables...........
        self.roll_var=StringVar()
        self.name_var=StringVar()
        self.email_var=StringVar()
        self.gender_var=StringVar()
        self.contact_var=StringVar()

        self.search_by=StringVar()
        self.search_text=StringVar()

        #........Manage Frame......

        Manage_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="chocolate2")
        Manage_Frame.place(x=20,y=100,width=470,height=550)
        
        m_title=Label(Manage_Frame,text="Manage Student",bg="chocolate2",fg="black",font=("time new roman",30,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        #...Roll Number......

        l_roll=Label(Manage_Frame,text="Roll No",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")

        text_roll=Entry(Manage_Frame,textvariable=self.roll_var,font=("time new roman",15),bd=5,relief=GROOVE)
        text_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        #......Name..............

        l_name=Label(Manage_Frame,text="Name",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_name.grid(row=2,column=0,pady=10,padx=20,sticky="w")

        text_name=Entry(Manage_Frame,textvariable=self.name_var,font=("time new roman",15),bd=5,relief=GROOVE)
        text_name.grid(row=2,column=1,pady=10,padx=20,sticky="w")

        #....Email...........

        l_email=Label(Manage_Frame,text="E-mail",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_email.grid(row=3,column=0,pady=10,padx=20,sticky="w")

        text_email=Entry(Manage_Frame,textvariable=self.email_var,font=("time new roman",15),bd=5,relief=GROOVE)
        text_email.grid(row=3,column=1,pady=10,padx=20,sticky="w")

        #......Gender....

        l_gender=Label(Manage_Frame,text="Gender",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_gender.grid(row=4,column=0,pady=10,padx=20,sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("time new roman",14,),state='readonly')
        combo_gender['values']=("Male","Female","Other")
        combo_gender.grid(row=4,column=1,padx=20,pady=10)



        #......Contact.......

        l_contact=Label(Manage_Frame,text="Contact",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_contact.grid(row=5,column=0,pady=10,padx=20,sticky="w")

        text_contact=Entry(Manage_Frame,textvariable=self.contact_var,font=("time new roman",15),bd=5,relief=GROOVE)
        text_contact.grid(row=5,column=1,pady=10,padx=20,sticky="w")


        #.......Address........

        l_address=Label(Manage_Frame,text="Address",bg="chocolate2",fg="white",font=("time new roman",20,"bold"))
        l_address.grid(row=6,column=0,pady=10,padx=20,sticky="w")

        self.text_address=Text(Manage_Frame,width=32,height=4,font=("",10),bd=5,relief=GROOVE)
        self.text_address.grid(row=6,column=1,pady=10,padx=20,sticky="w")

        #....Button Frame.............
        btn_Frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="chocolate2")
        btn_Frame.place(x=10,y=490,width=430)
        
        addbtn=Button(btn_Frame,text="ADD",width=10,command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_Frame,text="UPDATE",width=10,command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        deletebtn=Button(btn_Frame,text="DELETE",width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clearbtn=Button(btn_Frame,text="CLEAR",width=10,command=self.clear).grid(row=0,column=3,padx=10,pady=10)
        
        
         #........Detail Frame......
        
        Data_Frame=Frame(self.root,bd=4,relief=RIDGE,bg="chocolate2")
        Data_Frame.place(x=500,y=100,width=750,height=550)

        l_search=Label(Data_Frame,text="Search By",bg="chocolate2",fg="black",font=("time new roman",16,"bold"))
        l_search.grid(row=0,column=0,pady=10,padx=20,sticky="w")

        combo_search=ttk.Combobox(Data_Frame,textvariable=self.search_by,width=15,font=("time new roman",13,"bold"),state='readonly')
        combo_search['values']=("Roll_No","Name","Contact")
        combo_search.grid(row=0,column=1,padx=20,pady=10)

        text_search=Entry(Data_Frame,textvariable=self.search_text,width=15,font=("time new roman",13,"bold"),bd=5,relief=GROOVE)
        text_search.grid(row=0,column=2,pady=10,padx=20,sticky="w")

        searchbtn=Button(Data_Frame,text="Search",width=10,pady=5,command=self.search_data).grid(row=0,column=3,padx=10,pady=10)
        showallbtn=Button(Data_Frame,text="Show All",width=10,pady=5,command=self.fetch_data).grid(row=0,column=4,padx=10,pady=10)


        #....Table Frame.............

        Table_Frame=Frame(Data_Frame,bd=4,relief=RIDGE,bg="chocolate2")
        Table_Frame.place(x=10,y=70,width=720,height=480)

        scroll_x=Scrollbar(Table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(Table_Frame,orient=VERTICAL)
        
        self.Student_table=ttk.Treeview(Table_Frame,columns=("Roll","Name","Email","Gender","Contact","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        self.Student_table.heading("Roll",text="Roll No")
        self.Student_table.heading("Name",text="Name")
        self.Student_table.heading("Email",text="E-mail")
        self.Student_table.heading("Gender",text="Gender")
        self.Student_table.heading("Contact",text="Contact")
        self.Student_table.heading("Address",text="Address")
        self.Student_table['show']='headings'
        self.Student_table.column("Roll",width=100)
        self.Student_table.column("Name",width=130)
        self.Student_table.column("Email",width=130)
        self.Student_table.column("Gender",width=100)
        self.Student_table.column("Contact",width=130)
        self.Student_table.column("Address",width=130)

        self.Student_table.pack(fill=BOTH,expand=1)

        self.Student_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.roll_var.get()==""or self.name_var.get()=="":
            messagebox.showerror("Error","All fields are required!!")

        else:

            connection=pymysql.connect(host="localhost",user="root",password="",database="sms")     
            cur=connection.cursor()
            cur.execute("insert into Students values(%s,%s,%s,%s,%s,%s)",(self.roll_var.get(),self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.text_address.get('1.0',END)))

            connection.commit()
            self.fetch_data()
            self.clear()
            connection.close()

            messagebox.showinfo("Success","Record has been inserted")

    def fetch_data(self):
        connection=pymysql.connect(host="localhost",user="root",password="",database="sms")     
        cur=connection.cursor()
        cur.execute("select * from Students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                connection.commit()
            connection.close()
    
    def clear(self):
        self.roll_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.text_address.delete('1.0',END)
    
    def get_cursor(self,event):
        curr_row=self.Student_table.focus()
        content=self.Student_table.item(curr_row)
        row=content['values']
        self.roll_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.text_address.delete('1.0',END)
        self.text_address.insert(END,row[5])


    def update_data(self):    
        connection=pymysql.connect(host="localhost",user="root",password="",database="sms")     
        cur=connection.cursor()
        cur.execute("update Students set name=%s,email=%s,gender=%s,contact=%s,address=%s where roll_no=%s",(self.name_var.get(),
        self.email_var.get(),
        self.gender_var.get(),
        self.contact_var.get(),
        self.text_address.get('1.0',END),
        self.roll_var.get()
        ))

        connection.commit()
        self.fetch_data()
        self.clear()
        connection.close()

    def delete_data(self):
        connection=pymysql.connect(host="localhost",user="root",password="",database="sms")     
        cur=connection.cursor()
        cur.execute("delete from Students where roll_no=%s",self.roll_var.get())

        connection.commit()
        connection.close() 
        self.fetch_data()
        self.clear() 

    def search_data(self):
        connection=pymysql.connect(host="localhost",user="root",password="",database="sms")     
        cur=connection.cursor()
        cur.execute("select * from Students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_text.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('',END,values=row)
                connection.commit()
            connection.close()   
        
       
root=Tk()

ob=Student(root)
root.mainloop()





