#!/usr/bin/env python
#-*-coding:utf-8-*-
# http://www.dmi.gov.tr/tahmin/il-ve-ilceler.aspx?m=SAMSUN

from Tkinter import *
import urllib2

pencere = Tk()
pencere.title("Hava Durumu ")
pencere.geometry("480x260+200+100")
pencere.resizable(width=FALSE, height=FALSE)
pencere.tk_setPalette("grey")

sehir_gir = Entry()
sehir_gir.place(relx=0.1, rely=0.1, relheight=0.15, relwidth=0.3)

sehir_gir_yazi = Label(text="Şehir İsmi ",font="Verdana 8 bold",fg = "white")
sehir_gir_yazi.place(relx=0.1, rely=0.005,relheight=0.10)

min_s = Entry()
min_s.place(relx=0.5, rely=0.5,relheight=0.15,relwidth=0.15)

min_s_yazi = Label(text="En Düşük Sıcaklık",font="Verdana 8 bold",fg = "white")
min_s_yazi.place(relx=0.2, rely=0.50,relheight=0.15)

max_s = Entry()
max_s.place(relx=0.5, rely=0.3,relheight=0.15,relwidth=0.15)

max_s_yazi = Label(text="En Yüksek Sıcaklık",font="Verdana 8 bold",fg = "white")
max_s_yazi.place(relx=0.2, rely=0.30,relheight=0.15)

kim = Label(text="Made by Emre Can YILMAZ\n ecylmz v0.1",font="Verdana 13 bold",fg = "white")
kim.place(relx=0.2, rely=0.70,relheight=0.15)

def hava_durumu_al(event=None):
    sehir = sehir_gir.get()
    page = urllib2.urlopen("http://www.dmi.gov.tr/tahmin/il-ve-ilceler.aspx?m="+sehir)
    text = page.read().decode("utf8")
    
    kb = text.find('"minS"')
    sb = text.find(">", kb) + 1
    ss = text.find("<", sb)
    minS = int(text[sb:ss])
    
    kb = text.find('"maxS"')
    sb = text.find(">", kb) + 1
    ss = text.find("<", sb)
    maxS= int(text[sb:ss])
    
    max_s.insert(0,maxS)
    min_s.insert(0,minS)

def temizle():
    sehir_gir.delete(0,END)
    min_s.delete(0,END)
    max_s.delete(0,END)

btn_hava_durumu_al = Button(text="Bilgileri Al",command=hava_durumu_al)
btn_hava_durumu_al.place(relx=0.70, rely=0.3, relheight=0.07, relwidth=0.15)

btn_temizle = Button(text="Temizle", command = temizle)
btn_temizle.place(relx=0.70, rely = 0.4 , relheight = 0.07 , relwidth = 0.15)

pencere.bind("<Return>",hava_durumu_al)


mainloop()
