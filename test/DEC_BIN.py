from bint2 import *
while True:
  try:
    a = int(input('>input'))
    b = DecTobin(a)
    print(b)
  except:
    print('only integers')
  