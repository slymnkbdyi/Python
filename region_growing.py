# veriyapilari odev_01 fatih tastemur #
############### kuyruk ###################################

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items==[]

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
    def search(self, item):
        return (item in self.items)
        
################ region_growing ##################################

import Image
import os

def region_growing(im,epsilon,spoint):
    
    Q=Queue()
    s=[]
    x=spoint[0]
    y=spoint[1]
    im =im.convert("L")
    
    Q.enqueue((x,y))
    while not Q.isEmpty():
        t = Q.dequeue()
        x = t[0]
        y = t[1]
        
        if x < im.size[0]-1 and (im.getpixel((x+1,y)) - im.getpixel((x,y))) <= epsilon :
            if not Q.search((x+1, y)) and not (x+1, y) in s:
                Q.enqueue((x+1,y))
                
        if x > 0 and (im.getpixel((x-1,y)) - im.getpixel((x,y))) <= epsilon:
            if not Q.search((x-1, y)) and not (x-1, y) in s:
                Q.enqueue((x-1,y))
                     
        if y < im.size[1]-1 and (im.getpixel((x,y+1)) - im.getpixel((x,y))) <= epsilon:
            if not Q.search((x, y+1)) and not (x, y+1) in s:
                Q.enqueue((x,y+1))
                    
        if y > 0 and (im.getpixel((x,y-1)) - im.getpixel((x,y))) <= epsilon:
            if not Q.search((x, y-1)) and not (x, y-1) in s:
                Q.enqueue((x,y-1))

        if t not in s:
            s.append(t)
            
    im.load()
    putpixel = im.im.putpixel
    
    for i in range (im.size[0]):
        for j in range (im.size[1]):
            putpixel((i, j), 0)

    for i in s:
        putpixel(i, 150)
        
    output=raw_input("kaydedilecek dosya adini giriniz: ") #fatih girelim
    im.thumbnail((im.size[0],im.size[1]), Image.ANTIALIAS)
    im.save(output + ".JPEG", "JPEG")

##### programin calistirilmasi ###################################

im=Image.open("ft.png")
epsilon=12
spoint=(13,11)
region_growing(im,epsilon,spoint)
