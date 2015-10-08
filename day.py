#!/usr/bin/env python
#-*- coding: utf-8 -*-


from sys import exit

class gunbul:
	def __init__(self):
		self.aylar={0:0, 1:31 , 2:28 , 3:31 , 4:30 , 5:31 , 6:30 , 7:31 , 8:31 , 9:30 , 10:31 , 11:30}
			
		self.gunler={0:"Pazartesi",1:"Sali",2:"Carsamba",3:"Persembe",4:"Cuma",5:"Cumartesi",6:"Pazar"}
				
		self.temel=730501    
		
	def hesapla(self,x,y,z): 
		self.incegun=0
		self.incegun=self.incegun+x
		self.kabagun=(z-1)/4*1461
		
		for i in range(ay):
			self.incegun=self.incegun+self.aylar.get(i)
		
		self.incegun=self.incegun+ (z-1) % 4 * 365
		
		if z%4==0 and y>2: 
			self.incegun=self.incegun+1
		
		self.bizimgun=self.kabagun+self.incegun
		self.katsayi=(self.bizimgun-self.temel)%7
		return self.gunler.get(self.katsayi)

while 1:
	a=raw_input("girin(cikmak icin \"cik\" yazin)   :")
	if a=="cik":
		exit()
	e=a.split(".")
	gun, ay, yil = int(e[0]), int(e[1]), int(e[2])
	print gunbul().hesapla(gun, ay, yil)
