from Tkinter import *

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

