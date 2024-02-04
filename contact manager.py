from tkinter import*
#def
def Insert():
    E1 = EFname.get()
    E2 = ELname.get()
    E3 = ECity.get()
    E4 = ETel.get()
    data = f'{E1},{E2},{E3},{E4}'
    data.split(",")
    L.insert(END,data)
    Clear()
    
def Clear():
    EFname.delete(0,END)
    ELname.delete(0,END)
    ECity.delete(0,END)  
    ETel.delete(0,END)

def Delete():
    Index = L.curselection()
    L.delete(Index)
def Fetch():
    Clear()
    Index= L.curselection()
    data= L.get(Index)
    Nlist = data.split(",")
    EFname.insert(0,Nlist[0])
    ELname.insert(0,Nlist[1])
    ECity.insert(0,Nlist[2])
    ETel.insert(0,Nlist[3])
def Exit():
    windows.destroy()


    
    
#Tk
windows = Tk()
windows.geometry("500x500")
windows.title("contact manager")
windows.config(bg="gold")
#label
Fname = Label(windows,text="Name ->",bg="gold",fg="Blue")
Fname.place(x= 50,y= 30)

Lname = Label(windows,text="Last name ->",bg="gold",fg="Blue")
Lname.place(x= 250,y= 30)

City = Label(windows,text="City ->",bg="gold",fg="Blue")
City.place(x= 50,y= 70)

Tel = Label(windows,text="Telephone ->",bg="gold",fg="Blue")
Tel.place(x= 250,y= 70)

#Entery,get
EFname = Entry()
EFname.place(x=110,y=30)

ELname = Entry()
ELname.place(x= 330,y= 30)

ECity = Entry()
ECity.place(x= 110,y= 70)

ETel = Entry()
ETel.place(x= 330,y= 70)
#button
Binsert =  Button(windows,text="insert",bg="#334d50",fg="#cbcaa5",command=Insert)
Binsert.place(x= 330,y= 110)

Bclear =  Button(windows,text="clear",bg="#334d50",fg="#cbcaa5",command=Clear)
Bclear.place(x= 330,y= 160)

Bdelete =  Button(windows,text="delete",bg="#334d50",fg="#cbcaa5",command=Delete)
Bdelete.place(x= 330,y= 210)

Bfetch =  Button(windows,text="fetch",bg="#334d50",fg="#cbcaa5",command=Fetch)
Bfetch.place(x= 330,y= 260)

Bexit =  Button(windows,text="exit",bg="#334d50",fg="#cbcaa5",command=Exit)
Bexit.place(x= 330,y= 310)

#listbox
L = Listbox(windows,width=35,height=13)
L.place(x=50,y= 120)

windows.mainloop()