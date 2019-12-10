# python-phonebook
from  Tkinter import *
from tkMessageBox import*
import sqlite3
root=Tk()
root.geometry('1000x400')
def close(e):
    root.destroy()
Label(root,text='Project Title :PhoneBook ',font='Arial 20 bold').grid()
Label(root,text='Project of Python and Database',font='Arial 20 bold').grid(row=1,column=1)
Label(root,text='Developed By: Rajat Tripathi',font='Arial 18 bold',fg='blue').grid(row=2,column=1)
Label(root,text='---------------------',font='Arial 20 bold',fg='blue').grid(row=3,column=1)
Label(root,text='Make Mouse Movement To Close',font='Arial 12 bold',fg='red').grid(row=4,column=1)
root.bind('<Motion>',close)
root.mainloop()
def plus():
   a= Entry(root)
   a.grid(row=11,column=2)
def pluss():
   a= Entry(root)
   a.grid(row=14,column=2)

root=Tk()
root.title('phone book')
con=sqlite3.Connection('phonebook')
cur=con.cursor()
cur.execute("create table if not exists contact3(contactid integer primary key autoincrement,F_name varchar(25) ,M_nmae varchar(25),L_name varchar(25),company varchar(25),address varchar(50),city varchar(50),pin number ,URL varchar(50),DOB date)")
cur.execute("create table if not exists phone(c_id integer, contact_type varchar(20),phone_no varchar(20),foreign key(c_id) references contact3(contactid) ON DELETE CASCADE)")
cur.execute("create table if not exists email(c_id_2 integer, email_type varchar(20),email_id varchar(50),foreign key(c_id_2) references contact3(contactid)ON DELETE CASCADE)")
a=PhotoImage(file="image.gif")
Label(root,image=a).grid(row=0,column=1)
Label(root,text='First Name',font='Garamon 12 bold').grid(row=1,column=0)
e1=StringVar()
e1=Entry(root,textvariable=e1)
e1.grid(row=1,column=1)
e2=StringVar()
Label(root,text='Middle Name',font='Garamon 12 bold').grid(row=2,column=0)
e2=Entry(root,textvariable=e2)
e2.grid(row=2,column=1)
e3=StringVar()
Label(root,text='Last Name',font='Garamon 12 bold').grid(row=3,column=0)
e3=Entry(root,textvariable=e3)
e3.grid(row=3,column=1)
Label(root,text='Company',font='Garamon 12 bold').grid(row=4,column=0)
e4=Entry(root)
e4.grid(row=4,column=1)
Label(root,text='Address',font='Garamon 12 bold').grid(row=5,column=0)
e5=Entry(root)
e5.grid(row=5,column=1)
Label(root,text='City',font='Garamon 12 bold').grid(row=6,column=0)
e6=Entry(root)
e6.grid(row=6,column=1)
Label(root,text='Pin Code',font='Garamon 12 bold').grid(row=7,column=0)
e7=Entry(root)
e7.grid(row=7,column=1)
Label(root,text='Write URL',font='Garamon 12 bold').grid(row=8,column=0)
e8=Entry(root)
e8.grid(row=8,column=1)
Label(root,text='Date Of Birth',font='Garamon 12 bold').grid(row=9,column=0)
e9=Entry(root)
e9.grid(row=9,column=1)
Label(root,text='Select Phone Type:',font='Garamon 12 bold',fg="Blue").grid(row=10,column=0)
v1=IntVar()
r1=Radiobutton(root,text='Office',variable=v1,value=1,font='Garamon 12 bold')
r1.grid(row=10,column=1)
r1=Radiobutton(root,text='Home',variable=v1,value=2,font='Garamon 12 bold')
r1.grid(row=10,column=2)
r1=Radiobutton(root,text='Mobile',variable=v1,value=3,font='Garamon 12 bold')
r1.grid(row=10,column=3)
Label(root,text='Phone Number',font='Garamon 12 bold').grid(row=11,column=0)
e10=StringVar()
e10=Entry(root,textvariable=e10)
e10.grid(row=11,column=1)
Button(root,text=' +',command=plus,font='Ariel 12 bold').grid(row=11,column=3)
v2=IntVar()
Label(root,text='Select Email Type:',font='Garamon 12 bold',fg="Blue").grid(row=13,column=0)
r4=Radiobutton(root,text='Office',variable=v2,value=4,font='Garamon 12 bold')
r4.grid(row=13,column=1)
r5=Radiobutton(root,text='Personal',variable=v2,value=5,font='Garamon 12 bold')
r5.grid(row=13,column=2)

Label(root,text='Email Id',font='Garamon 12 bold').grid(row=14,column=0)
e11=StringVar()
e11=Entry(root,textvariable=e11)
e11.grid(row=14,column=1)
Button(root,text=' +',command=pluss,font='Ariel 12 bold').grid(row=14,column=3)
at=0
dot=0
def insert():
    try:
        c=e11.get()
        n=c.count('@')
        m=c.count('.')
        if n==0 or m==0 or n>1 or m>1:
            showerror("Error","Invalid email")
            
            
            
        if len(e1.get())==len(e2.get())==len(e3.get())==0:
            showerror("Error","Name field cannot be empty")
            
            

        
        elif((e1.get()==e2.get()==e3.get())or e1.get()==e3.get() or e1.get()==e2.get() or e2.get()==e3.get()):
            showerror("Error","Enter different values of first name, middle name and last name")
            
            
        if len(e10.get())==0:
             showerror("Error","Length of phoneno cannot be zero")
             return
           
        elif len(e10.get())>0 and len(e10.get())<10:
            showerror("Error","Length of phoneno is not 10")
            return
        b,c,d,e,f,g,h,i,j=e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),e6.get(),int(e7.get()),e8.get(),e9.get()
        cur.execute("insert into contact3(F_name,M_nmae,L_name,company ,address , city , pin ,URL ,DOB )values(?,?,?,?,?,?,?,?,?)",(b,c,d,e,f,g,h,i,j))
        cur.execute("select contactid from contact3")
        p=cur.fetchall()
        print p
        if v1.get()==1:
            a='office'
        elif v1.get()==2:
            a='home'
        elif v1.get()==3:
            a='mobile'
        if v2.get()==5:
            b='personal'
        elif v2.get()==4:
            b='office'
        cur.execute("insert into phone values (?,?,?)",(int(p[len(p)-1][0]),a,int(e10.get())))
        cur.execute("insert into email values (?,?,?)",(int(p[len(p)-1][0]),b,e11.get()))
        con.commit()
        showinfo('saved','contact is saved')
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e5.delete(0,END)
        e6.delete(0,END)
        e7.delete(0,END)
        e8.delete(0,END)
        e9.delete(0,END)
        e10.delete(0,END)
        e11.delete(0,END)
        v1.set(0)
        v2.set(0)
    except:
        showerror("Error","Please input integer value in pin code and phone number or check radiobutton is select or not")
def fun2():
    root2=Tk()
    root2.geometry('600x450')
    Label(root2,text='Search Here:',fg='blue',font='Garamon 20 bold').grid(row=0,column=2)
    Label(root2,text='Enter Your Name :',fg='Black',font='Garamon 15 bold').grid(row=3,column=1)

    e12=Entry(root2,fg='Black',font='Arial 12 bold')
    e12.grid(row=3,column=2)
    lb=Listbox(root2,width=30,height=15,selectmode=SINGLE,font='Times 12 bold',fg='DarkBlue',bd=2)
    lb.grid(row=7,column=2)
    
    def searchh(e=0):
        lb.delete(0,END)
        f12=e12.get()
        cur.execute("select * from contact3  where F_name like (?)",(f12,))
        m2=cur.fetchall()
        for i in range(len(m2)):
            lb.insert(END,m2[i][1])
    def showinfo(e=0):
        m3=lb.get(lb.curselection())
        lb.delete(0,END)
        cur.execute("select contactid,f_name from contact3 where F_name like (?)",(str((m3.partition(" "))[0]),))
        m4=cur.fetchall()
        cur.execute("select * from contact3 where contactid=(?)",(str(m4[0][0]),))
        m5=cur.fetchall()
        print m5
        cur.execute("select * from phone where c_id=(?)",(str(m4[0][0]),))
        m6=cur.fetchall()
        print m6
        cur.execute("select * from email where c_id_2=(?)",(str(m4[0][0]),))
        m7=cur.fetchall()
        print m7
        
        lb.insert(END,"First Name:"+str(m5[0][1]))
        lb.insert(END,"Middle Name:"+str(m5[0][2]))
        lb.insert(END,"Last Name:"+str(m5[0][3]))
        lb.insert(END,"Company Name:"+str(m5[0][4]))
        lb.insert(END,"Address:"+str(m5[0][5]))
        lb.insert(END,"City:"+str(m5[0][6]))
        lb.insert(END,"Pin Code:"+str(m5[0][7]))
        lb.insert(END,"Website URL:"+str(m5[0][8]))
        lb.insert(END,"Date Of Birth:"+str(m5[0][9]))
        lb.insert(END,"Phone Type:"+str(m6[0][1]))
        lb.insert(END,"Phone Number:"+str(m6[0][2]))
        lb.insert(END,"Email Type:"+str(m7[0][1]))
        lb.insert(END,"Email Id:"+str(m7[0][1+1]))
        def delete1():
            root2.destroy()
            cur.execute(" drop table contact3")
            con.commit()
            askyesno('delete','contact is delete')
        Button(root2,text='Delete',command=delete1,font='Ariel 12 bold').grid(row=11,column=3)
        def fun5():
            root2.destroy()
            e1.insert(END,str(m5[0][1]))
            e2.insert(END,str(m5[0][2]))
            e3.insert(0,str(m5[0][3]))
            e4.insert(0,str(m5[0][4]))
            e5.insert(0,str(m5[0][5]))
            e6.insert(0,str(m5[0][6]))
            e7.insert(0,str(m5[0][7]))
            e8.insert(0,str(m5[0][8]))
            e9.insert(0,str(m5[0][9]))
            e10.insert(0,str(m6[0][2]))
            e11.insert(0,str(m7[0][2]))
            if str(m6[0][1])=='office':
                v1.set(1)
            elif str(m6[0][1])=='home':
                v1.set(2)
            elif str(m6[0][1])=='mobile':
                v1.set(3)
            if str(m7[0][1])=='personal':
                v2.set(5)
            elif str(m7[0][1])=='office':
                v2.set(4)
            cur.execute("delete from contact3 where contactid=%d"%m4[0][0])
            cur.execute("delete from phone where c_id=%d"%m4[0][0])
            cur.execute("delete from email where c_id_2=%d"%m4[0][0])
            con.commit()
            
        Button(root2,text=' Edit ',command=fun5,font='Ariel 12 bold').grid(row=11,column=0)
    e12.bind('<Key>',searchh)
    lb.bind('<Double-Button-1>',showinfo)
    def fun3():
        root2.destroy()
    Button(root2,text='Close',command=fun3,font='Ariel 12 bold').grid(row=11,column=2)
    
        
    e12.delete(0,END)
def fun4():
    a=askyesno("close","do you really want to close")
    if a==TRUE:
         root.destroy()
def Edit():
     showinfo('NOTE','Please Search Before Editing')
     fun2()   
        
               
    
Button(root,text=' Save ',command=insert,font='Ariel 12 bold').grid(row=16,column=0)
Button(root,text='Search ',command=fun2,font='Ariel 12 bold').grid(row=16,column=1)
Button(root,text='Edit ',command=Edit,font='Ariel 12 bold').grid(row=16,column=2)
Button(root,text='Close',command=fun4,font='Ariel 12 bold').grid(row=16,column=3)
root.mainloop()
