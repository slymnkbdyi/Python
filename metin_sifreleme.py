#!/usr/bin/env python
#-*-coding:utf-8-*-
from Tkinter import *
pencere = Tk()
pencere.title("Metin Şifreleme")
pencere.geometry("480x260+200+100")
pencere.resizable(width=FALSE, height=FALSE)
pencere.tk_setPalette("grey")

giris = Entry()
giris.place(relx=0.1, rely=0.1, relheight=0.15, relwidth=0.3)

cikis = Entry()
cikis.place(relx=0.5, rely=0.1,relheight=0.15,relwidth=0.3)

kim = Label(text="Made by Emre Can YILMAZ\n ecylmz v0.1",font="Verdana 13 bold",fg = "white")
kim.place(relx=0.2, rely=0.50,relheight=0.15)

uyari=Label(text="Türkçe Karakter,Büyük Harf ve Noktalama İşareti KULLANMAYINIZ...",fg="white",font="Verdana 10 ")
uyari.place(relx=0.01,rely=0.0)

def sifrele():
    x=giris.get() #kullanıcının girdiği metni x değişkenine atıyoruz
    uzunluk=len (x) # metinin uzunluğunu değerlendirip kullanıcıya yanıt veriyoruz...
    if uzunluk >= 500:
        m="Cümle Çok Uzun!!!En Fazla 500 Karakter."
        cikis.insert(0,m)
    if uzunluk < 500:
        for yazilan in x: #görüldüğü gibi sözlük kullandık her harfe ikili bir sayı atadık 5 haneli...
            matrix = {"a":"01010", "b":"01011", "c":"01100" , "d":"01101" , "e":"01110" , "f":"01111" , "g":"10000" , "h":"10001" ,
             "i":"10010" , "j":"10011" , "k":"10100" , "m":"10101" ,"n":"10110" ,"o":"10111" , "p":"11000" ,"r":"11001" , "l":"00111",
             "s":"11010" , "t":"11011" , "u":"11100" ,"v":"11101" , "y":"11110" , "z":"11111" , "x":"00001" ,"q":"00010" , " ":"00011",}
            i=str(matrix.get(yazilan)) #ikili sayıları sayı olarak değilde metin olarak yazması gerekiyordu...
            cikis.insert(0,i)
def coz():
    y=giris.get() #sifrelemedikin tersini uyguluyoruz...
    uzunluk_1=len(y)
    if uzunluk_1 >= 2500:
        n="Şifre Çok Uzun!!! En Fazla 2500 Karakter."
        cikis.insert(0,n)
    if uzunluk_1 < 2500:
        for okunan in xrange(0,uzunluk_1,5):
            matrix_1 = {"01010":"a","01011":"b","01100":"c","01101":"d","01110":"e","01111":"f","10000":"g","10001":"h",
                            "10010":"i","10011":"j","10100":"k","10101":"m","10110":"n","10111":"o","11000":"p","11001":"r","11010":"s",
                            "11011":"t","11100":"u","11101":"v","11110":"y","11111":"z","00001":"x","00010":"q","00011":" ","00111":"l"}
            j=matrix_1.get(y[okunan:okunan+5]) #ikili ifadeleri 5 er li okuması gerekiyordu...önceden harflerin karşılığını 5 haneli seçtiğimiz için
            cikis.insert(0,j)
            
def temizle():
    giris.delete(0,END)
    cikis.delete(0,END)
    
def yardim():
    pencere2=Toplevel()
    pencere2.title("Metin Şifreleme [Yardım]")
    pencere2.geometry("720x180+200+100")
    
    yazi=Label(pencere2, text="*Türkçe karakter,noktalama işareti,büyük harf kullanılamaz.Şayet kullanılırsa program düzgün çalışmayacaktır.\n*Şifrelenecek metin 500 karakteri geçemez,çözülecek metin ise 2500 karakteri geçemez.\n*Şifrelenmiş veya çözülmüş metni çift tıklatarak seçip kopyalayabilirsiniz bu size kolaylık sağlayacaktır.")
    yazi.place(relx=0.01, rely=0.1)
    
    dugme6=Button(pencere2,text="Kapat", command=pencere2.destroy)
    dugme6.place(relx=0.45,rely=0.4)

dugme = Button(text = "Şifrele", command = sifrele)
dugme.place(relx=0.1, rely=0.3,relheight=0.07,relwidth=0.15)

dugme2 = Button(text = "Çöz", command = coz)
dugme2.place(relx=0.25, rely=0.3,relheight=0.07,relwidth=0.15)

dugme4=Button (text ="Temizle", command = temizle)
dugme4.place(relx=0.4, rely=0.3,relheight=0.07,relwidth=0.15)

dugme3 = Button (text = "Çıkış", command = pencere.quit)
dugme3.place(relx=0.55, rely=0.3, relheight=0.07, relwidth=0.15)

dugme5=Button(text="Yardım",command=yardim)
dugme5.place(relx=0.70, rely=0.3, relheight=0.07, relwidth=0.15)


mainloop()
