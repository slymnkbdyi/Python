#!/usr/bin/env python
#-*- coding: utf-8 -*-
#Sozluk
#Fatih TAŞTEMUR

import re, urllib
from Tkinter import *

class sozluk:
	def __init__(self):
		self.site="http://......./"  #url
		
		self.ana=Tk()
		self.ana.title("Sözlük")
		self.ana.geometry("400x300")
		self.ana.bind_all('<Key>', self.tus)
		self.cerceve0=Frame(self.ana, bg="#F9F9F9")
		self.cerceve0.pack(fill=X, side=TOP)
		
		Label(self.cerceve0, bg="#F9F9F9", text="Aranacak Kelime:").pack(padx=15, side="left")
		
		self.kelimegir=Entry(self.cerceve0, bg="pink")
		self.kelimegir.focus_set()
		self.kelimegir.pack(expand=YES, fill=X, pady=20, side="left")
		
		self.tus=Button(self.cerceve0)
		self.tus.config(text="Ara", command=self.ara)
		self.tus.pack(padx=35, pady=35, side="right")
		
		self.aracerceve=Frame(self.ana, bg="#F9F9F9", padx=20)
		self.aracerceve.pack(fill=X)

		self.eee=StringVar()
		self.ka=OptionMenu(self.aracerceve, self.eee, "İngilizce => Türkçe", "Türkçe => İngilizce")
		self.eee.set("İngilizce => Türkçe")
		self.ka.pack(side="left")
		Label(self.aracerceve, text="fatih.tastemur@ce.omu.edu.tr", bg="gray", font=("DejaVu_Sans_Condensed", 12)).pack(side="right")
		
		self.cerceve1=Frame(self.ana, bg="#F9F9F9", padx=35, pady=30)
		self.cerceve1.pack(expand=YES, fill=BOTH)

		self.metin=Text(self.cerceve1, bg="green", font=("DejaVu_Sans_Condensed", 13))
		self.metin.config(bd=5, relief=SUNKEN, state=DISABLED, width=140)
		self.cubuk=Scrollbar(self.cerceve1)
		self.cubuk.config(command=self.metin.yview)
		self.metin.config(yscrollcommand=self.cubuk.set)
		self.cubuk.pack(fill=Y, side="right")
		self.metin.pack(expand=YES, fill=BOTH)
		
		self.ana.mainloop()
				
	def bul(self, aranan, kaynak, hedef):
				
		
		self.site=self.site+"index.php?lang=tr&word=%s&from=%s&to=%s" %(aranan, kaynak, hedef)
		self.arama=urllib.urlopen(str(self.site)).read()
		self.kelime='<td align="left" valign="top" bgcolor="#F7FFE7">'+aranan+'</td>\s*.*\s*<td align="left" valign="top" bgcolor="#FFFFFF"></td>\s*</tr>\s*<tr>\s'
		self.e=re.search(self.kelime, self.arama)
			
		if self.e:
			self.g=re.search(self.kelime, self.arama[self.e.end():])
			self.f=re.search(self.kelime, self.arama[self.e.end()+self.g.end():])
			
			try:
				self.b1=self.g.group()
				self.b2=self.f.group()
				self.b3=self.e.group()
			
			except AttributeError:
				self.metin.config(state=NORMAL)
				self.metin.delete(1.0, END)
				self.metin.insert(END, "Kelimeyi Ararken Bir Hata Olustu")
				self.metin.config(state=DISABLED)
			
			self.b1=self.b1[48:-75]
			self.b2=self.b2[48:-75]
			self.b3=self.b3[48:-75]
			
			self.b1=self.b1.replace("<br>", "\n")
			self.b1=self.b1.replace("<b>", "")
			self.b1=self.b1.replace("</b>", "")
			self.b1=self.b1.replace("</td>", "")
			self.b1=self.b1.replace('<td align="left" valign="top" bgcolor="#FFFFFF">', "")
			self.b1=self.b1.replace('<font color="#0000FF">', "")
			self.b1=self.b1.replace('&nbsp;', " ")
			self.b1=self.b1.replace('</font>', "")
			self.b1=self.b1.replace('<font color="#aa0033">__', "")
			
			self.b2=self.b2.replace("<br>", "\n")
			self.b2=self.b2.replace("<b>", "")
			self.b2=self.b2.replace("</b>", "")
			self.b2=self.b2.replace("</td>", "")
			self.b2=self.b2.replace('<td align="left" valign="top" bgcolor="#FFFFFF">', "")
			self.b2=self.b2.replace('<font color="#0000FF">', "")
			self.b2=self.b2.replace('&nbsp;', " ")
			self.b2=self.b2.replace('</font>', "")
			self.b2=self.b2.replace('<font color="#aa0033">__', "")				
						
			self.b3=self.b3.replace("<br>", "\n")
			self.b3=self.b3.replace("<b>", "")
			self.b3=self.b3.replace("</b>", "")
			self.b3=self.b3.replace("</td>", "")
			self.b3=self.b3.replace('<td align="left" valign="top" bgcolor="#FFFFFF">', "")
			self.b3=self.b3.replace('<font color="#0000FF">', "")
			self.b3=self.b3.replace('&nbsp;', " ")
			self.b3=self.b3.replace('</font>', "")
			self.b3=self.b3.replace('<font color="#aa0033">__', "")
			
			return self.b1+"\n\n"+self.b2+"\n\n"+self.b3
				
		else: 
			return "Aradıginiz Kelime Bulunamadi"
	
	def ara(self):
		if re.search("[0-9]", self.kelimegir.get()) or len(self.kelimegir.get())==0:
			self.metin.config(state=NORMAL)
			self.metin.delete(1.0, END)
			self.metin.insert(END, "Gecersiz islem (:")
			self.metin.config(state=DISABLED)
				
		
		else:
			if self.eee.get()=="İngilizce => Türkçe":
				self.bulunan=self.bul(self.kelimegir.get(), "en", "tr")
		
			else:
				self.bulunan=self.bul(self.kelimegir.get(), "tr", "en")
		
			self.metin.config(state=NORMAL)
			self.metin.delete(1.0, END)
			self.metin.insert(END, self.bulunan)
			self.metin.config(state=DISABLED)
		
	def tus(self, event):
		if event.keysym=='Return':
			self.ara()
	
E=sozluk()
