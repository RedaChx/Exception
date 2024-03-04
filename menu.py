import tkinter
from tkinter import messagebox
fenetre = tkinter.Tk()
fenetre.title("Concatenation")
fenetre.geometry("500x300")
fenetre.config(bg="green")

L1 = tkinter.Label(text="Menu",bg="green")
L1.place(x=30,y=40)



text = tkinter.Text(height=10,width=20)
text.place(x=260,y=40)
def clear():
    messagebox.askokcancel("Question","Voulez vous continuer ?")
    check1.deselect()
    check2.deselect()
    check3.deselect()
    check4.deselect()
    check5.deselect()
    check6.deselect()
    text.delete(0.0,tkinter.END)
but1 = tkinter.Button(text="RAZ" , command=clear)
but1.place(x=40,y=230)

def Afficher():
    text.delete(0.0,tkinter.END)
    if var1.get() == 1:
        text.insert(tkinter.INSERT,"Poisson \n")
    if var2.get() == 1:
        text.insert(tkinter.INSERT,"Salade \n")
    if var3.get() == 1:
        text.insert(tkinter.INSERT,"Fromage \n")
    if var4.get() == 1:
        text.insert(tkinter.INSERT,"Dessert \n")
    if var5.get() == 1:
        text.insert(tkinter.INSERT,"Cafe \n")
    if var6.get() == 1:
        text.insert(tkinter.INSERT,"Jus \n")
but2 = tkinter.Button(text="Ok")
"but2.place(x=150,y=230)"
var1 = tkinter.IntVar()
check1 = tkinter.Checkbutton(text="Poisson" , bg="green" , variable=var1 , command=Afficher)
check1.place(x=40,y=70)
var2 = tkinter.IntVar()
check2 = tkinter.Checkbutton(text="Salade" , bg="green" , variable=var2 , command=Afficher)
check2.place(x=40,y=100)
var3 = tkinter.IntVar()
check3 = tkinter.Checkbutton(text="Fromage" , bg="green" , variable=var3 , command=Afficher)
check3.place(x=40,y=130)
var4 = tkinter.IntVar()
check4 = tkinter.Checkbutton(text="Dessert" , bg="green" , variable=var4 , command=Afficher)
check4.place(x=150,y=70)
var5 = tkinter.IntVar()
check5 = tkinter.Checkbutton(text="Cafe" , bg="green" , variable=var5 , command=Afficher)
check5.place(x=150,y=100)
var6 = tkinter.IntVar()
check6 = tkinter.Checkbutton(text="Jus" , bg="green" , variable=var6 , command=Afficher)
check6.place(x=150,y=130)
def close():
    fenetre.destroy()
but3 = tkinter.Button(text="Fermer" , command=close)
but3.place(x=260,y=230)
fenetre.mainloop()
