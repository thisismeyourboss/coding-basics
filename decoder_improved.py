# -*- coding: utf-8 -*-
"""Untitled7.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1jrm8-vOJnNKhFZzXQZZOJAnZpemBCpco
"""

code = input()
while(code!='0'):
  code = list(code)
  """ Every "0" will be combined with its previous element e.g. 101 will be broken as "10" "1" and not"1" "01".
  also "00" will be invalid so will print 0 in that case"""

  for i in range(len(code)-1):
    if(code[i+1]=='0'):
      code[i]=code[i]+code[i+1]

  for i in range(len(code)):
    if (code[i]=='00'):
      flag = 0
      break
    elif(int(code[i])>26):
      flag=0
      break
    else:
      flag=1
  rectified = [(code[i])  for i in range(len(code)) if int(code[i])!=0]

  def magic_s(rect):
    result = [0]*(len(rect)-1)
    for i in range(len(rect)-1):
      num = int(rect[i]+rect[i+1])
      if num>=10 and num<=26:
        result[i]=1
    return result
  chunks = magic_s(rectified)
  """ chunks for 25412 will be [1 0 0 1] and for 10101 [0 0]
  (note that 10101 will be breaked into 10 10 1 so the chunks 1010 and 101 are invalid.)"""
  sum=1
  for i in range(len(rectified)):
    if int(rectified[i])<=26 and int(rectified[i])>0:
      continue
    else:
      sum=0
      break
  """ calc is doing nothing but calculating no of all possible combination.
  Its a bit hard to explain how it works-but it involves repetitive steps:
  1-calculate sum of all numbers except the one ahead:231215---level 1-->[1 0 1 1 1]---level2--> [3 0 1 0 0]
  meaning that you can not choose both 23 and 31 in 23124 at once and you can not choose 31 i.e. 0
  also if you add level2 elements = 4 i.e 3(#23 12 1 5 #23 1 21 5 #23 1 2 15) 1(#2 3 12 15) (notice:3 0 1 0 )
  2- every time you repeat the process you end up calculating the no of possible combination for next level.
  level means how many size 2 chunk you are using e.g. 23 12 4 is level 2 and 23 1 2 4 is level 1"""
  def calc(piece):
    size = len(piece)
    result = [0]*size
    for i in reversed(range(size-2)):
      result[i]+=piece[i+2] + result[i+1]
    for(i) in range(size):
      if(piece[i]==0):
        result[i] =0
    return result
  """ The following step involves adding all possible combination of different levels.
  End the process when a particular level have 0 possible combination."""
  from operator import add
  final = [0]*len(chunks)
  result = chunks
  middle = [1]*len(chunks)
  while (set(middle)!=set(final)):
    middle = calc(chunks)
    result = list(map(add,result,middle))
    chunks = middle
  """sum is for level 0 i.e. no size 2 chunks and sum1 is for level 1 and onwards"""
  sum1=0
  for i in range(len(result)):
    sum1+=result[i]
  if(flag):
    print(sum+sum1)
  else:
    print(0)
  code = input()

