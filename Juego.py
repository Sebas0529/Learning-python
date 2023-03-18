import random
options = ('piedra', 'papel', 'tijeras')

round = 1
count_person = 0
count_comp = 0


while True :   
    
    print('*' * 10)
    print('round =>', round, '----', count_person, ' : ', count_comp)
    print('*' * 10)
    user = input('piedra - papel - tijeras => ').lower()
    diferencia = int(input('con diferencia de cuanto quieres jugar'))
    round += 1
    if user not in options:
        print('esa opcion no es valida')
        continue

    computer = random.choice(options)
    print('computer =>',computer)
    print('user => ',user)
    if user == computer:
        print('EMPATE')
        continue

    if user == 'piedra':
        if computer == 'tijeras':
            print('piedra gana a tijeras')
            print('user gano')
            count_person += 1
        else:
            print('papel gana a piedra')
            print('computer gano')
            count_comp += 1
    elif user == 'tijeras':
        if computer == 'piedra':
            print('piedra gana a tijeras')
            print('computer gano')
            count_comp += 1
        else:
            print('tijeras gana a papel')
            print('user gano')
            count_person += 1
    elif user == 'papel':
        if computer == 'piedra':
            print('papel gana a piedra')
            print('user gana')
            count_person += 1
        else:
            print('tijeras gana a papel')
            print('computer gana')
            count_comp += 1

    if (count_comp-diferencia) == count_person:
        break
    elif (count_person-diferencia) == count_comp:
        break


print(count_person, ' : ', count_comp)

if (count_comp-3) == count_person:
    print('GANO LA MAQUINA')
elif (count_person-3) == count_comp:
    print('GANO EL HOMBRE')
