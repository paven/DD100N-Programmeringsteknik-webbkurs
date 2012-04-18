# Programmeringsteknik webbkurs KTH inlämningsuppgift 1.
# Patrik Gustafsson
# 2011-07-08
# I den första inlämningsuppgiften ska du skriva och skicka in ditt första pythonprogram. Programmet ska skriva ut de första n kvadrattalen: 1*1, 2*2, ... , n*n, där talet n anges av den som använder programmet. Programmet ska också skriva ut summan av dessa kvadrattal

sum =0; #Summan av kvadraterna
number=int(input("Välkomen till prat i kvadrart\nHur många kvadrattal vill du skriva ut? "))+1 #Ska vara ett högre än antalet vad användaren frågar efter då range går till talet under det det får.

for i in range(1, number):
   kvadrat=i*i 
   sum+=kvadrat
   print(i, "*", i,"=",kvadrat)

print("Summan av kvadrattalen:", sum)
