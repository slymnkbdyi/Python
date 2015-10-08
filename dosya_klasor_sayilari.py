# -*- coding: utf-8 -*-
import os

klasor_sayisi = 0
dosya_sayisi = 0

klasor_yolu = raw_input("Klasor yolunu eksiksiz olarak girin : \n")

for i in os.walk(klasor_yolu): # os.walk ' in sonucu bir tuple 'dir
		klasor_sayisi = klasor_sayisi + 1 
		dosya_sayisi = dosya_sayisi + len(i[2]) # tuple ' in 2. ogesi dosyalari icerdigi icin uzunlugunu ekledik

print """
Klasor Sayisi %d
Dosya Sayisi %d
""" %(klasor_sayisi , dosya_sayisi)
