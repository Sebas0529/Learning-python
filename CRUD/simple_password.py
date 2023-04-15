def SimplePassword(stri):
  symbol = '!@#$%^&*"\'=+-,.<>:;|'
  numeros = '0123456789'
  x = y = False

  for n in numeros:
    if stri.find(n) >= 0:
      y = True

  if y:
    for n in symbol:
      if stri.find(n) >= 0:
        x = True
        stri = stri.replace(n,'0')
  else:
    print('falta minimo un numero')

      
      
  if x:
    if (stri.lower()).find('password') < 0:
      if stri.isalnum():
        if stri != stri.lower():
          if len(stri)>7 and len(stri)<31:
              return True
          return False
      return False
  return False
            

# keep this function call here 
print(SimplePassword(input()))