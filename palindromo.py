
x = str(input('ingrese una palabra para saber si es palindromo ==> '))
x=x.lower()
if x == x[::-1]:
    print('es palindromo')
else:
    print('no es palindromo')
    