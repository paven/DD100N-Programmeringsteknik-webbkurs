dikt = ["En båt\n", "i plåt\n", "blev våt\n"]
diktfil = open("poesi.txt", "w")
 
diktfil.writelines(dikt)
diktfil.close() 
