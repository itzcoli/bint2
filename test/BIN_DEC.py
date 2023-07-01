import bint2
while True:
  try:
    a = int(input('>input'))
    b = BinTodec(a)
    print(b)
  except:
    print('only integers')
  