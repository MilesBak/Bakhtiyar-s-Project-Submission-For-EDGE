import re

def main_menu():
    print('Main Menu')
    print('1. String Operation')
    print('2. Number Operation')
    print('3. Exit')


def emailValid(email):
    if re.match(r'[^@]+@[^@]+.[^@]+', email):
        return True
    return False

def phoneValid(phone):
    if re.match(r'01[5-9]\d{8}', phone):
        return True
    return False

def eV_exec():
    email = input('\nEnter a valid email address: ')
    match emailValid(email):
        case True:
            print(f'\nProvided email [{email}] is valid!')
            return
        case _:
            print(f'\nProvided email [{email}] is not valid!')
            return
    eV_exec()

def pV_exec():
    phone = input('\nEnter a valid phone number: ')
    match phoneValid(phone):
        case True:
            print(f'\nThe phone-number {phone} is valid!')
            return
        case _:
            print(f'\nThe phone-number {phone} is not valid!')
            return
    pV_exec()

def main():
    while (True):
        main_menu()
        choice = input('\nEnter choice(1, 2 or 3): ')
        match choice:
            case '1':
                print('\nThank you for choosing String operation.')

                while True:
                    rchoice = input('\nChoice (1-> EmailValidation, 2->PhoneValidation, 3->Back to Main Menu): \n')
                    match rchoice:
                        case '1':
                            eV_exec()
                        case '2':
                            pV_exec()
                        case '3':
                            break
                        case _:
                            ('\nInvalid input!')

            case '2':
                print('\nThank you for choosing number operation.')

                while True:
                    nchoice = input('\n1-> Addition, 2-> Subtraction, 3-> Multiplication, 4-> Division, 5-> Back to Menu Menu\n')
                    if nchoice == '5':
                        break
                    x = float(input('\n1st number: '))
                    y = float(input('\n2nd number: '))
                    match nchoice:
                        case '1':
                            print(f'\n{x} + {y} = {x+y}')
                        case '2':
                            print(f'\n{x} - {y} = {x-y}')
                        case '3':
                            print(f'\n{x} * {y} = {x*y}')
                        case '4':
                            print(f'\n{x} / {y} = {x/y}')
                        case _:
                            print('\nInvalid input!')

            case '3':
                print('\nThanks for using switch statements')
                break
            case _:
                print('\nInvalid Input!!!')
main()

