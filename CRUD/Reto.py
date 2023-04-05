
def FirstFactorial(num):
    try:
        int(num)
    except:
        print("El valor ingresado no es un numero, ingresalo nuevamete")
        return False
    num = int(num)
    fact = 1
    if num > 1 and num < 18:
        for x in range(1,num+1):
            fact = fact*x
    else:
        print("El valor ingresado no es un numero, ingresalo nuevamete")
        return False 
    return fact
# keep this function call here 
while True:
    inp = input()
    res = FirstFactorial(inp)
    if res:
        print("El factoria de {}  es {}".format(inp, res))
        break









