# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jrm8-vOJnNKhFZzXQZZOJAnZpemBCpco
"""

rate , money , num = (input().split())
rate ,money,num =  int(rate),int(money),int(num)
price =  num*(num+1)/2 * rate
if (price-money)>0:
  print(int(price-money))
else:
  print(0)

