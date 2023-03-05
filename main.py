from Pizza import Pizza
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.ttk import Combobox
from PIL import Image,ImageTk
from Sos import Sos
from PizzaOrder import PizzaOrders
from datetime import datetime
import sys
while True:
    aciklama=""
    fiyat=0
    pizzaorder1=PizzaOrders()
    def urunekle():
        pizzaTur = entry_pizzaTur.get()
        boyutT = boyut.get()
        print(boyutT + " " + pizzaTur)
        next_button["state"]="disabled"
        if boyutT=="":
            msg=messagebox.showinfo("Hata",message="Lutfen boyut secimi yapiniz")
        elif pizzaTur=="01" or pizzaTur=="02" or pizzaTur=="03" or pizzaTur=="04":
            myPizza= Pizza(pizzaTur,boyutT)
            aciklama=myPizza.get_description()
            fiyat=myPizza.get_cost()
            pizzaorder1.pizza_description=myPizza.get_description()
            pizzaorder1.pizza_cost=fiyat
            lbl_Describtion=tk.Label(form,text=aciklama,bg="#bbbcbb",font="Times 12 italic").place(x=720,y=360)
            lbl_cost = tk.Label(form, text="Cost:" + str(fiyat), bg="#bbbcbb", font="Times 12 italic").place(x=720, y=400)
            next_button["state"]="normal"
        else : 
            msg=messagebox.showinfo("Hata",message="Belirtilen pizza kodu bulunamadi")
    def nextpage():
        form.destroy()
        #import page2
    def Close():
        sys.exit()
    form = tk.Tk()
    form.geometry('1000x600')
    form.title('MX Pizza House')
    interface=ImageTk.PhotoImage(Image.open("form1.png"))
    label=tk.Label(image=interface)

    lbl_pizzaTur=tk.Label(form,text="Pizza Kodu: ",font="Times 15",bg="#bbbcbb").place(x=760,y=140)
    entry_pizzaTur=ttk.Entry(form)
    entry_pizzaTur.place(x=860,y=140,height=25,width=25)
    boyut=tk.StringVar()
    radbuton_small=tk.Radiobutton(form,text= 'Kucuk(+25)',bg= '#bbbcbb' ,value= 'Small' , variable=boyut).place(x=690,y=185)
    radbuton_mid=tk.Radiobutton(form,text='Orta(+50)' ,bg='#bbbcbb' ,value= 'Medium' , variable=boyut).place(x=780,y=185)
    radbuton_large=tk.Radiobutton(form,text='Buyuk(+75)' ,bg='#bbbcbb' ,value= 'Large' , variable=boyut).place(x=855,y=185)
    next_button=tk.Button(form,text="Next",command=nextpage,bg="#0d9700",activebackground="green",state="disabled")
    next_button.place(x=847,y=542,height=35,width=102)
    cikis_button=tk.Button(form,text="Close",command=Close,bg="#0d9700",activebackground="green").place(x=950,y=15)
    ekle_button=tk.Button(form,text="Ekle",command=urunekle,bg="#bbbcbb",activebackground="gray").place(x=800,y=225,height=25,width=50)
    lbl_Siparisbilgi=tk.Label(form,text="Siparis Bilgileri",bg="#bbbcbb",font="Times 12 italic").place(x=760,y=300)
    label.pack()
    form.mainloop()
    print(aciklama,str(fiyat))
    form=tk.Tk()
    form.geometry("1000x600")
    form.title("MX Pizza House")
    interface=ImageTk.PhotoImage(Image.open("form2.png"))
    label=tk.Label(image=interface)
    sosdesc=""
    sos_fiyat=0
    Sauce=[]
    def sosekle():
        Sauce = [olive.get(), mushroom.get(), goatcheese.get(), meat.get(), onion.get(), corn.get()]
        soslar=Sos(Sauce)
        print(soslar.get_description())
        sosdesc=soslar.get_description()
        sos_fiyat=soslar.get_cost()
        pizzaorder1.sauce_description=soslar.get_description()
        pizzaorder1.sauce_cost=soslar.get_cost()
        lbl_Describtion = tk.Label(form, text=soslar.get_description(), bg="#bbbcbb", font="Times 12 italic").place(x=780, y=200)
        lbl_cost = tk.Label(form, text="Cost: " + str(soslar.cost), bg="#bbbcbb", font="Times 12 italic").place(x=780, y=350)
    def nextpage():
        form.destroy()
        #import page3
    next_button=tk.Button(form,text="Next",command=nextpage,bg="#0d9700",activebackground="green")
    next_button.place(x=847,y=542,height=35,width=102)
    olive = tk.StringVar()
    mushroom = tk.StringVar()
    goatcheese = tk.StringVar()
    meat = tk.StringVar()
    onion = tk.StringVar()
    corn = tk.StringVar()

    check_olive=tk.Checkbutton(form,text="Olive",variable=olive,bg="#ff0000",activebackground="#ff0000",onvalue="Olive")
    check_olive.place(x=115,y=240)
    check_mushroom=tk.Checkbutton(form,text="Mushroom",variable=mushroom,bg="#ff0000",activebackground="#ff0000",onvalue="MushRoom")
    check_mushroom.place(x=300,y=240)
    check_goatcheese=tk.Checkbutton(form,text="Goat Cheese",variable=goatcheese,bg="#ff0000",activebackground="#ff0000",onvalue="GoatCheese")
    check_goatcheese.place(x=465,y=240)
    check_meat=tk.Checkbutton(form,text="Meat",variable=meat,bg="#ff0000",activebackground="#ff0000",onvalue="Meat")
    check_meat.place(x=115,y=440)
    check_onion=tk.Checkbutton(form,text="Onion",variable=onion,bg="#ff0000",activebackground="#ff0000",onvalue="Onion")
    check_onion.place(x=300,y=440)
    check_corn=tk.Checkbutton(form,text="Corn",variable=corn,bg="#ff0000",activebackground="#ff0000",onvalue="Corn")
    check_corn.place(x=465,y=440)
    ekle_button=tk.Button(form,text="Soslari Onayla",command=sosekle,bg="#ff0000",activebackground="#ff0000").place(x=270,y=500,height=25,width=100)

    label.pack()
    form.mainloop()

    form = tk.Tk()
    form.geometry('1000x600')
    form.title('MX Pizza House')
    interface=ImageTk.PhotoImage(Image.open("form3.png"))
    label=tk.Label(image=interface)
    def siparisonay():
        pizzaorder1.gotocsv()
        form.destroy()
    def bilgionay():
        if entry_adsoyad.get()!="" and entry_kredikart.get()!="" and entry_kredipass.get()!=""and entry_tcno.get()!="":
            pizzaorder1.name_surname=entry_adsoyad.get()
            pizzaorder1.tckimlikno=entry_tcno.get()
            pizzaorder1.creditcardnumber=entry_kredikart.get()
            pizzaorder1.creditpass=entry_kredipass.get()
            pizzaorder1.date=datetime.now()
            siparis_onay["state"]="normal"
        else:
            siparis_onay["state"]="disable"
            msg=messagebox.showinfo("Hata",message="Lutfen tum alanlari doldurdugunuzdan emin olunuz")
            

    lbl_siparisbilgi=tk.Label(form,text=pizzaorder1.pizza_description+"\n"+pizzaorder1.sauce_description+" \nCost:"+str(pizzaorder1.pizza_cost+pizzaorder1.sauce_cost),bg="#bbbcbb",font="Times 12 italic").place(x=750,y=200)
    entry_adsoyad=ttk.Entry(form)
    entry_adsoyad.place(x=180,y=220,height=25,width=80)

    entry_tcno=ttk.Entry(form)
    entry_tcno.place(x=195,y=275,height=25,width=80)

    entry_kredikart=ttk.Entry(form)
    entry_kredikart.place(x=310,y=330,height=25,width=100)

    entry_kredipass=ttk.Entry(form,show="*")
    entry_kredipass.place(x=275,y=380,height=25,width=35)
    bilgi_onay=tk.Button(form,text="Bilgileri Onayla",command=bilgionay,bg="#ff0000",activebackground="red")
    bilgi_onay.place(x=300,y=450,height=35,width=102)

    siparis_onay=tk.Button(form,text="Siparisi Onayla",command=siparisonay,bg="#0d9700",activebackground="green",state="disabled")
    siparis_onay.place(x=847,y=542,height=35,width=102)


    label.pack()
    form.mainloop()