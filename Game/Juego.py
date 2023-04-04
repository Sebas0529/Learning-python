import random
options = ('piedra', 'papel', 'tijeras')

round = 1
count_person = 0
count_comp = 0
diferencia = int(input('con diferencia de cuanto quieres jugar ==> '))

def choose_options():
    user = input('piedra - papel - tijeras => ').lower()
    if user not in options:
        print('esa opcion no es valida')
        #continue
        return None, None
    computer = random.choice(options)
    return computer, user

def check_rules(user,computer,count_person, count_comp):
    if user == computer:
        print('EMPATE')
        return count_person,count_comp

    if user == 'piedra':
        if computer == 'tijeras':
            print('user gano')
            count_person += 1
        else:
            print('computer gano')
            count_comp += 1
    elif user == 'tijeras':
        if computer == 'piedra':
            print('computer gano')
            count_comp += 1
        else:
            print('user gano')
            count_person += 1
    elif user == 'papel':
        if computer == 'piedra':
            print('user gana')
            count_person += 1
        else:
            print('computer gana')
            count_comp += 1
    return count_person, count_comp

def winer(count_person, count_comp):
    if (count_comp-diferencia) == count_person:
        return 'GANO LA MAQUINA',count_person,' : ',count_comp
    elif (count_person-diferencia) == count_comp:
        return 'GANO EL HOMBRE'
    


def run_game():
    round = 1 
    count_person = 0
    count_comp = 0
    while True :  
        print(('*' * 10) + '      COUNT PERSON         COUNT COMP')
        print('round =>', round, '----     ', count_person, '         :       ', count_comp)
        print('*' * 10)
        round += 1

        computer, user = choose_options()

        print('computer =>',computer)
        print('user => ',user)

        count_person, count_comp = check_rules(user, computer, count_person, count_comp)

        if (count_comp-diferencia) == count_person:
            print(winer(count_person,count_comp))
            break
        elif (count_person-diferencia) == count_comp:
            print(winer(count_person,count_comp))
            break

run_game()

