def arabul(ne,adress):
    import urllib
    try:
        print "baglanti kuruluyor..."
        net_sayfa = urllib.urlopen(adress)
        text = net_sayfa.read().decode("utf8")
        print "baglanti kuruldu."

        kac_kez=0 ; sira=0
        
        while ne in text:
            sira = text.find(ne)
            text=text[sira+1:]
            sira+=1
            kac_kez+=1
        print "text içinde %s kez '%s' dizgisi geçmektedir." %(kac_kez , ne)

    except:
        print "girdiginiz degerleri veya/ninternet baglantinizi kontrol ediniz."
    
