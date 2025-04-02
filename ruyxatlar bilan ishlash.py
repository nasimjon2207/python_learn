# -*- coding: utf-8 -*-
"""
Created on Mon Mar 10 08:51:12 2025

@author: hp
"""

frinds=['Nasimjon', 'Abdulbosit', 'Doniyor', 'Shohrux']
frinds.sort()
print(frinds)
frinds.sort(reverse=True)
print(frinds)
print(sorted(frinds))
print(sorted(frinds, reverse=True))
number=[2001,2003,2000,2025]
number.sort()
print(number)
print(sorted(number, reverse=True))
number.reverse()
print(number)
print("uzunligi = " , len(number))
sonlar=list(range(0, 10))
print(sorted(sonlar, reverse=True))
juft_son=list(range(0,20,2))
toq_son=list(range(1,20,2))
print("juft sonlar= ",juft_son, " toq sonlar= ",toq_son)
