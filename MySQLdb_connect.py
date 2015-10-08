
__author__="ftastemur"
__date__ ="$Nisan 02, 2012 ; 21:40 PM$"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import MySQLdb

class MySQLVeritabani:
    _baglantidurumu = 0		#Veritabanina yapilmis olan baglanti durumunu saklar. 0->Bagli degil 1->Bagli
    _dry = 0			#Veritabani baglanti nesnesi

    def __init__(self):
        self._baglantidurumu = 0
        self._dry = 0

    #Veritabani baglanti durumunu dondurur.
    def BaglantiDurumu(self):
        return self._baglantidurumu

    #Veritabanina baglanti yapar. Baglanti basarisiz olursa 0, basarili olursa 1 degerini dondurur.
    def Baglan(self):
        try:
            self._dry = MySQLdb.connect("SunucuAdresi", "KullaniciAdi", "Parola", "VeritabaniAdi")
            self._baglantidurumu = 1
        except:
            self._baglantidurumu = 0
        return self._baglantidurumu

    #Veritabani baglantisini kapatir. Baglanti kapatildiktan sonra 1 degerini dondurur.
    def BaglantiyiKapat(self):
        self._dry.close()
        self._baglantidurumu = 0
        return 1

    #Parametre olarak gelen sorguyu calistirir ve veritabanindan aldigi verileri dondurur.
    def VeriSorgula(self, sorgu):
        cursor = self._dry.cursor()
        cursor.execute(sorgu)
        sonuc = cursor.fetchall()
        return sonuc

    #Parametre olarak gelen komutu calistirir ve degisiklik yapilan satir sayisini dondurur.
    def KomutCalistir(self, komut):
        try:
            cursor = self._dry.cursor()
            satirSayisi = cursor.execute(komut)
            self._dry.commit()		#Islem basarili oldugu icin commit yapilir.
            return satirSayisi
        except:
            self._dry.rollback()		#Hata olustugu icin yapilan degisiklikler geri alinir.
            return 0
