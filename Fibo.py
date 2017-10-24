# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 13:50:24 2017

@author: kryshi
"""




n = int(input("Kolik prvků? >"))

n1 = 0
n2 = 1
i = 0

if n <= 0:
   print("Nope")
elif n == 1:
   print(n1)
else:
   while i < n:
       print(n1)
       nth = n1 + n2
       n1 = n2
       n2 = nth
       i += 1