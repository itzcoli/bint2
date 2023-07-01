def DecTobin(input_dec):
  try:
    input_dec = int(input_dec)
    out_bin = []
    op1 = ""
    while True:
      if input_dec > 1 :
        operation = int(input_dec / 2)
        opt2 = input_dec % 2 
        out_bin.append(str(opt2))
        input_dec = operation
      else:
        out_bin.append('1')
        break
    out_bin.reverse()
    return int(op1.join(out_bin))
  except ValueError:
    raise ValueError('only int.')
  
def BinTodec(input_bin):
  try:
    int(input_bin)
    input_bin = str(input_bin)
    input_bin = list(input_bin)
    input_bin.reverse()
    value_dec = 0
    co1 = 0
    for number in input_bin:
      bin_dec = int(number)*2**co1
      value_dec = value_dec + bin_dec
      co1 = co1 + 1
    return value_dec
  except ValueError:
    raise ValueError('only int')
  
  #Bint decimal and binary utilities
  #Code by itzcoli
  

    
