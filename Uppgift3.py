# Programmeringsteknik webbkurs KTH inlämningsuppgift 3.
# Patrik Gustafsson
# 2011-07-11
# simulerar ett nöjesfält

import random
from tkinter import *
import time
from threading import Thread

"""liten stöd funktion som ger ifrån sig ett av de finaste orden som finns"""
def slumpAttribut():
    a = ['största', 'minsta', 'vackraste', 'kortaste', 'rundaste', 'fyrkantigaste', 'finaste', 'coolaste', 'blötaste' ]
    return a[random.randrange(len(a))]
                    
"""En klass som beskriver ett virtuellt åk atraktion.
Är en tråd för att flera attraktioner ska kunna vara igång samtidigt.
Attribut:
    namn -  nanm
    skick - ett heltal som beskriver attraktionens skick
    utrop - hur det låter från attraktionen
    frekvens - hur ofta det låter och hur ofta slitage sker
    körNu - om attraltoionen är i gång
    kontroller - applikationen som kontrollerar attraktionen
    

"""
class Attraktion(Thread):
    """ Konstruktorn, initierar attributen namn, utrop och slumpvisskick."""
    def __init__(self, attraktionnamn, utrop, applikation):
        Thread.__init__(self)
        self.namn = attraktionnamn ##
        self.skick = random.randrange(-5,7) ##hur troligt en krasch är
        self.utrop = utrop ##vad som låter från attracktionen
        self.frekvens = random.randrange(1, 10) ##omvändfrekvens slumpas
        self.körNu= False
        self.kontroller = applikation
        
    """ returnerar sig attraktionens namn."""
    def getNamn(self):
        return self.namn

    """Gör reklam för attraktionen"""
    def reklam(self):
        print ("Prova världens" , slumpAttribut(), self.getNamn())

    """Startar karusellen (och tråden om det behövs)"""
    def kör(self):
        if self.isAlive() == False:
            self.start()
        self.körNu = True
        
    """ Trådem startar attraktionen och ger desutom ifrån sig dess utrop om inget farligt händer då något värre sker"""
    def run(self):
        while(True):
            while(self.körNu == True):
                if random.randrange(-20, -1) > self.skick: #Om attraktionen är i fördåligt skick kan den gå sönder.
                    ordlängd = len(self.utrop) #ordlängd används för att klippa ordet på mitten.
                    ordlängd = int(ordlängd/2)
                    print (self.utrop[:-ordlängd], "Aaaaaaaa...... <Kabom>" ) #sedan skirker folk i panik...
                    jag = self
                    self.kontroller.toggleAttraktionMedObjekt(jag)
                else:
                    print (self.utrop) #går allt bra så gör dom utropet.
                    self.skick -= random.randrange(-1, 10)/10 #går lite sönder
                time.sleep(self.frekvens)
            time.sleep(1)
        

    """Stannar attraktionen, och lite lagning sker"""
    def stopp(self):
        self.körNu = False
        self.skick += random.randrange(-1, 10) #lagas lite

"""Fönster som stannar och stoppar attraktionerna"""
class Applikation(Frame):
    """skapar fönster och initierar knappar"""
    def __init__(self, master=None):
        Frame.__init__(self, master)   
        self.grid()                    
        self.skapaWidgets()

    """Växlar mellan kör och inte kör"""
    def toggleAttraktionMedIndex(self, index=0):

        if self.attraktion[index].körNu:
            self.attraktion[index].stopp()
            self.knappar[index].configure(text= self.attraktion[index].getNamn(), state=NORMAL)

            
        else:
            self.attraktion[index].kör()
            self.knappar[index].configure(text= "STOPPA " + self.attraktion[index].getNamn(), state=NORMAL)

    """Växlar mellan kör och inte kör"""    
    def toggleAttraktionMedObjekt(self, attraktion):
        index = self.attraktion.index(attraktion)
        self.toggleAttraktionMedIndex(index)
        

    """Skapar en funktion som togglar Attraktion för givet index, som används i Button då Button.command ej tar parametrar"""
    def lambdaFactory(self, index):
        return lambda:self.toggleAttraktionMedIndex(index)
    
    """initierar knapparna och gör reklam"""
    def skapaWidgets(self):
        antal = 3 ##antal attraktioner som ska bli knappar. De defineras på radernarna nedan.
        self.attraktion = antal*[None]
        self.attraktion[0] = Attraktion("Berg o Dal bana", "Weee ahh whee heheh", self)
        self.attraktion[1] = Attraktion("Dansbana", "Så låt de sista ljuva åren\nbli de bästa i vårt liv\nDen lycka som vi känner", self)
        self.attraktion[2] = Attraktion("Flumride", "Whoo splash", self)

        ##Knapparna skapas utifrån attraktionerna ovan.  
        self.knappar = antal*[None]
        
        for i in range(antal):
            self.knappar[i] = Button( self, text=self.attraktion[i].getNamn(),
                                      command=self.lambdaFactory(i)) #kopplar knappen till attraktionen
            self.knappar[i].grid() ##gör knappen synlig
            self.attraktion[i].reklam()
    
        self.quitButton = Button ( self, text='Quit', command=self.quit )
        self.quitButton.grid()
        
     

app = Applikation()                    
app.master.title("Nöjespark") 
app.mainloop()                         
            



