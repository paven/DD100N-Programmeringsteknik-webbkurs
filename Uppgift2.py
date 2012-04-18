# Programmeringsteknik webbkurs KTH inlämningsuppgift 2.
# Patrik Gustafsson
# 2011-07-09

#I den här inlämningsuppgiften ska du skriva ett antal funktioner för att göra ett program som skapar en dikt av en inläst text. Programmet ska läsa in fyra meningar och sedan skriva ut texten uppdelad på följande rader:
#Textens fyra första ord
#Resten av första meningen
#Textens fyra första ord igen
#Andra meningen
#Tredje meningen
#Fjärde meningen
#Textens fyra första ord en sista gång
#Texten kommer då att likna en rondelet - en fransk diktform.


# Data:
sentences = 4*[None]
# TestData
##sentences[0] = "Det fanns ingen fil när jag handlade på Konsum."
##sentences[1] = "Bananerna var också slut."
##sentences[2] = "Jag köpte bröd istället."
##sentences[3] = "Nån sorts limpa med mycket fibrer."

#Functions

#Funktion för att skriva ut fyra ord på en rad sedan resten på en ny rad
def printFourWordsThenPrintTheRest(sentence):
    words = printFourWordsAndReturnTheRest(sentence)
    while(len(words)>0):
        print(words.pop(), end=' ')
    print() #För att der ska bli en radbrytning i slutat.

 
        
    
#Funktion för att skriva ut fyra ord(om eller så många som finns) på en rad och sedan retunera resten, 
def printFourWordsAndReturnTheRest(sentence):
    words = sentence.split()
    words.reverse()
    four = 4
    if len(words) < four: #kontrollerar att 4 ord finns och minskar annars antalet ord att skriva ut.
        four = len(words)
    for i in range(four):
        print (words.pop() , end=" ")
    print()
    return words
    

#Input algorithm

print("                DIKTAUTOMATEN\nSkriv in fyra meningar och få ut en rondelet!\n")
for i in range(0,4):
    sentences[i] = input("Skriv mening nr %d:" % (i+1))




#output algorithm
printFourWordsThenPrintTheRest(sentences[0]) #row 1-2

printFourWordsAndReturnTheRest(sentences[0]) #row 3

for i in range(1, 4):
    print(sentences[i]) #row 4-6

printFourWordsAndReturnTheRest(sentences[0]) #row 7






