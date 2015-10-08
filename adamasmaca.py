#!/usr/bin/env  python
# -*- coding: utf-8 -*-

#Fatih TASTEMUR

from Tkinter import *
from re import search
from time import sleep
from random import choice

def yenioyun():
	global kelime, uzunluk, yuzunluk, yazan
	kelimeler=["fatih", "tastemur", "bilgisayar", "zemzem","samsun", "omu", "python", "tkinter", "kde", "ofis", "galatasaray", "ankara", "kwrite", "linux", "firefox",  "gimp", "konsole", "konversation", "kmix", "gnome", "xfce", "rails", "bash", "mysql", "amsn"]
	kelime=choice(kelimeler)
	print kelime
	uzunluk=len(kelime)*"_ "
	cizgiler.config(text=uzunluk)
	yuzunluk=""
	yazan=yazan+"\n Yeni Oyuna Başladınız. Kolay Gelsin (:\n"
	olaylar.config(text=yazan)
	adam.config(text="")
	agac.config(text=metin1)
	
	
	
def tahmin(x):
	global kelime, uzunluk, yuzunluk, hatasayisi, yazan
	if search(x, kelime):
		yazi=uzunluk.split(" ")
		k=""
		for i in range(len(kelime)):
			if kelime[i]==str(x):
				k=k+str(i)
				
		for i in k:
			yazi[int(i)]=str(x).upper()
			
		yuzunluk=""
		
		for i in yazi:
			yuzunluk=yuzunluk+i+" "
			
			
		cizgiler.config(text=yuzunluk)
		yuzunluk=yuzunluk[:-1]
		uzunluk=yuzunluk
		
		deneme=""
		for i in yuzunluk.split(" "):
			deneme=deneme+i
			
		
		if deneme.lower()==kelime:
			adam.config(text="       "+"Tebrikler, Bildiniz!")	
		
	else:
		yazan=yazan+"\nSeçilen Harf Bulunmamaktadır.\n"
		hatasayisi=hatasayisi+1
		liste=[metin1, metin2, metin3, metin4, metin5, metin6]
		for i in range(len(liste)):
			agac.config(text=liste[hatasayisi])
			olaylar.config(text=yazan)
		if hatasayisi==5:
			yazan=yazan+"\n Maalesef Kaybettiniz\n"
			olaylar.config(text=yazan)
			cizgiler.config(text=kelime)
			adam.config(text="Maalesef Başarısız Oldunuz")
			hatasayisi=0
			
			yenioyun()


ana=Tk()
ana.geometry("500x300")
ana.title("Adam Asmaca")



ck1=Frame()
ck1.pack()

ck2=Frame(ck1)
ck2.grid(row=0, column=0)

cerceve1=Frame(ck2)
cerceve1.grid(row=0, column=0)


adam=Label(cerceve1)
adam.pack(side="bottom")

cizgiler=Label(cerceve1)
cizgiler.pack(side="bottom")

Button(cerceve1, text="Yeni Oyun", command=yenioyun).pack(side="bottom")





cerceve3=Frame(ck2)
cerceve3.grid(row=1, column=0)

alfabe=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u", "v", "y", "z", "w", "q", "x"]

for i in alfabe:
	Button(cerceve3, text=i.upper(), command=(lambda i=i: tahmin(i)), width=2, height=1).grid(column=alfabe.index(i)%8, row=alfabe.index(i)/8)
	




cerceve4=Frame(ck1)
cerceve4.grid(row=0, column=1)

hatasayisi=0

metin1="\n _ _ _ _\n |\n |\n |\n |\n |\n |\n/_\ \n"
metin2="\n _ _ _ _\n |      |\n |\n |\n |\n |\n |\n/_\ \n"
metin3="\n _ _ _ _\n |      |\n |     O\n |\n |\n |\n |\n/_\ \n"
metin4="\n _ _ _ _\n |      |\n |     O\n |     /|\ \n |\n |\n |\n/_\ \n"
metin5="\n _ _ _ _\n |      |\n |     O\n |     /|\ \n |      |\n |\n |\n/_\ \n"
metin6="\n _ _ _ _\n |      |\n |     O\n |     /|\ \n |      |\n |     / \ \n |\n/_\ \n"

agac=Message(cerceve4, text=metin1)
agac.config(justify="left", font=("bold"))
agac.pack()




cerceve5=Frame()
cerceve5.pack(expand=YES, fill=BOTH)


yazan=""
olaylar=Message(cerceve5, text=yazan)
olaylar.config(justify="left", relief=SUNKEN, bg="#ffffff")
olaylar.pack(expand=YES, fill=BOTH, pady="10", padx="30")


ana.mainloop()
