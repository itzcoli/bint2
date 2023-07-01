import bint2
while True:
  try:
    a = int(input('>input'))
    b = DecTobin(a)
    print(b)
  except:
    print('only integers')
  