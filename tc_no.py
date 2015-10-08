# -*- coding: utf-8 -*-
def tc_no_dogrula(no):
    tekler_toplami = 0
    ciftler_toplami = 0
    if len(str(no)) == 11 and no > 0 and type(no) == type(5) and type(no) != type(2147483648):
        no = str(no)

        for i in range(0,10,2):
            tekler_toplami += int(no[i])

        for j in range(1,9,2):
            ciftler_toplami += int(no[j])

        onuncu_hane = ((tekler_toplami * 7) - ciftler_toplami) % 10

        toplam = 0 # 10 hane toplamını bulmak için .
        on_hane = int(no[:10])
        
        while on_hane :
            son_basamak = on_hane % 10
            on_hane = on_hane / 10
            toplam = toplam + son_basamak

        son_hane = toplam % 10

        if son_hane == int(no[10]) and onuncu_hane == int(no[9]):
            print "geçerli tc no"

        else :
            print "geçersiz tc no"           
            
    else :
        print "Lutfen 11 basamakli bir tamsayi giriniz!"
