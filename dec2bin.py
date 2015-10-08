#!/usr/bin/env python
#-*-coding:utf-8-*-

def dec2bin(decNumber):        #oncelikle fonksiyonumuzu tanimladik,arguman olarak decimal bir sayi aliyor.               
    listem=[]                  #bos bir liste olusturduk.
    while decNumber>0:         #girdigimiz arguman sifirdan büyük oldugu sürece devam edecek bir while dongusu..
        a=decNumber%2          #girilen decimal sayisinin 2 ye göre modunu al ve modulden kalani a degiskenine at.
        listem.insert(0,a)     #a degerlerini sırasıyla listemin başına ekliyoruz...bunun için listem.insert(0,a)
        decNumber=decNumber/2  #dongu devam ettigi surece decimal sayiyi surekli 2'ye boluyoruz.

    binString=""                         #2'lik tabana cevirdigimiz sayilari tutmak icin bos bir string olusturduk.
    binString=repr(listem)+ binString    #sonra repr() fonksiyonunu kullanarak listemi bos olan binString icine attim.
    return binString              

                            #ben burda listeler,stringler ve donguler den yararlandim..   
                            #sorularınız icin fatih.tastemur@bil.omu.edu.tr
                         
