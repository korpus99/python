### Zadanie 1
# a = [1-x for x in range(10)]
# b = [4**i for i in range(7)]
# c = [x for x in b if x % 2 == 0]
#
# print(a)
# print(b)
# print(c)

### Zadanie 2
# from random import randint
#
# lista = [randint(0, 100) for q in range(10)]
# lista.sort()
# print(lista)
# parzyste = [q for q in lista if q%2==0]
# print(parzyste)

# Zadanie 3
# sklep = {
#     "Mleko" : "litry",
#     "Jajka" : "sztuki",
#     "Mąka" : "kg"
# }
# sztuki ={}
#
# sztuki = {wartosc: nazwa for nazwa,  wartosc in sklep.items() if wartosc == 'sztuki'}

### Zadanie 4
# def trojkat()

### Zadanie 5
# def pole(aa=1, bb=1, hh=1):
#     if (str(aa).isdigit() == False) | (str(bb).isdigit() == False) | (str(hh).isdigit() == False):
#         return "Zla wartosc"
#     else:
#         aa = float(aa)
#         bb = float(bb)
#         hh = float(hh)
#         if (aa<=0)|(bb<=0)|(hh<=0):
#             return "Zla wartosc"
#         else:
#             P = (aa+bb)*hh/2
#             return P
# hh = input("Wysokosc\n")
# aa = input("Dlugosc pierwszej podstawy\n")
# bb = input("Dlugosc drugiej podstawy\n")
# print(pole(aa, bb, hh))