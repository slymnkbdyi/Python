# ssh_connect
__author__="ftastemur"
__date__ ="$Nisan 02, 2012 ; 03:30 AM$"

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import paramiko
import os
import time
import sys


istemci = paramiko.SSHClient()

def SunucuKomut():
	keyayarlari = paramiko.HostKeys()
	keyayarlari.load("/home/aloneft/.ssh/id_rsa")
	keyayarlari.lookup("server IP") 
	t = paramiko.Transport("server IP")
	t = paramiko.Transport(("server IP"))
	t.start_client()
	host_key = t.get_remote_server_key()
	keyayarlari.add("server IP", host_key.get_name(), host_key())
	keyayarlari.save("/home/aloneft/Desktop/known_hosts")
	istemci.load_system_host_keys()
	test = istemci.connect("server IP" , port = 22, username = "root" , password = "sifre gir" )
    if test == None:
		print " Hedef sunucuya SSH erisimi saglanabiliyor..!!!"

def SunucuDownload():
	sftp = istemci.open_sftp()
	try:
		sftp.get("/home/xoron/dry.txt", "/home/aloneft/Desktop/dry.txt")
	except IOError ,(hatakodu, hataadi):
		if hatakodu == 2:
			print " Sunucuda mevcut dosya bulunamadı, tum islemler iptal edildi.!"
		sys.exit()
	sftp.close()
	

def DosyaIslemleri():
	DomainIsmi = str(raw_input("Eklenecek domain ismini giriniz:"))
	arama = " cat /home/aloneft/Desktop/dry.txt | grep " + DomainIsmi
	os.system(arama)
	if arama != 0 :
		print "Aradiginiz isimde bir domain kayitli degil!"
		time.sleep(1)
		print "Domaininiz dosya'ya ekleniyor.."
	    time.sleep(1)
	    dosya = open("/home/aloneft/Desktop/dry.txt","a")
		dosya.write(DomainIsmi)
		dosya.write("\n")
		dosya.close
	else: print " \nDomain bilgileri ustteki gibidir.Simdi program sonlandırılacaktır."
	
def SunucuUpload():
	sftp = istemci.open_sftp()
	try:
		sftp.remove("/home/xoron/dry.txt")
	except IOError,(hatakodu, hataadi):
		if hatakodu == 2:
			print "Sunucuda silinecek dosya bulunmamaktadır! Upload a geciliyor."
			time.sleep(1)
		pass
		
     try:
		 sftp.put("/home/aloneft/Desktop/dry.txt", "/home/xoron/dry.txt")
	 except IOError,(hatakodu, hataadi):
		 if hatakodu == 2:
			 print "Localde editlenen dosya bulunamadi..!"
	os.remove("/home/aloneft/Desktop/dry.txt")
	

def SunucuDurdur():
	keyayarlari = paramiko.HostKeys()
	keyayarlari.load("/home/aloneft/.ssh/id_rsa")
	keyayarlari.lookup("server IP")
	t = paramiko.Transport("server IP")
    t = paramiko.Transport(("server IP"))
    t.start_client()
    host_key = t.get_remote_server_key()
    keyayarlari.add("server IP", host_key.get_name(),host_key)
    keyayarlari.save("/home/aloneft/Desktop/known_hosts")
    istemci.load_system_host_keys()
    test = istemci.connect("server IP", port = 22 , username = "root", password"sifre gir")
    if test == None:
		print "Servisler durduruluyor..!!"
		time.sleep(1)
		stdin, stdout, stderr = istemci.exec_command('cd /home/xoron; mkdir durdur')
		

def SunucuBaslat():
	keyayarlari = paramiko.HostKeys()
	keyayarlari.load("/home/aloneft/.ssh/id_rsa")
	keyayarlari.lookup("server IP") # sunucunun IP adresi girilecek
	t = paramiko.Transport("server IP")
    t = paramiko.Transport(("server IP"))
    t.start_client()
    host_key = t.get_remote_server_key()
    keyayarlari.add("server IP", host_key.get_name(),host_key)
    keyayarlari.save("/home/aloneft/Desktop/known_hosts")
    istemci.load_system_host_keys()
    test = istemci.connect("server IP", port = 22 , username = "root", password"sifre gir")
    if test == None:
		print "Servisler baslatiliyor..!!"
		time.sleep(1)
		stdin, stdout, stderr = istemci.exec_command('cd /home/xoron; mkdir baslat')
		
SunucuKomut()
SunucuDownload()
DosyaIslemleri()
SunucuDurdur()
SunucuUpload()
SunucuBaslat()
