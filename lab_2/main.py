### Zadanie 1
# lista = ['siatkówka', 'piłka nożna', 'ręczna']
# print(lista)
# lista.reverse()
# print(lista)
# lista.append('koszykówka')
# print(lista)

### Zadanie 2
# slownik={
#     "WWW" : "World wide web",
#     "HTML" : "HyperText Markup Language",
#     "FAQ" : "Frequently Asked Questions",
#     "CAPTCHA" : "Completely Automated Public Turing",
#     "IRC" :  "Internet Relay Chat"
# }
# print("Słownik:")
# print(slownik.keys())
# print("Wprowadz nazwe:")
# kod=input()
# print(slownik[kod])

### Zadanie 3
# gry={
#     1 : "League of Legends",
#     2 : "Euro Truck Simulator 2",
#     3 : "GRID 2"
# }
# print("Liczba elementów listy:")
# print(len(gry))

### Zadanie 4
# print("Podaj zdanie")
# zdanie=input()
# print(zdanie.count("a"))

### Zadanie 5

### Zadanie 6
# import math
# print("Podaj liczby")
# l1=input()
# l2=input()
# l3=input()
#
# if l1>l2 and l1>l3:
#     print(l1)
# elif l2>l1 and l2>l3:
#     print(l2)
# elif l3>l1 and l3>l2:
#     print(l3)
# else:print("Liczby są równe")

### Zadanie 7
# liczby=[2,3,6,8,1.11,22.36,9.77]
# il=len(liczby)
# i=0
# for i in range(len(liczby)):
#     liczby[i] = liczby[i] ** 2
#     print(liczby[i])

### Zadanie 8
# parzyste=[]
# count = 0
# while count <=9:
#     liczba = int(input("Podaj liczbe "))
#     count+=1
#     if liczba % 2 == 0 :
#         parzyste.append(liczba)
# print(parzyste)

### Zadanie 9
# napis = ""
# liczby = [1, 2, 3 ,4 ,5]
# for x in liczby:
#     if x%2 == 0:
#         napis+="E\n"
#     else:
#         napis+="EEEEEE\n"
# print(napis)

### Zadanie 10
# import math
# Liczba_dot = (input("Podaj x aby obliczyc sqrt(x): "))
# try:
#         wynik = math.sqrt(int(Liczba_dot))
#         print(wynik)
# except ValueError:
#         print("Podano ujemny x")