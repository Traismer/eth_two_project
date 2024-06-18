from eth_project.connection import connect_test_provider
from menu.tab_menu import get_account_balance, perform_transaction, new_account


def display_menu():
    print('\nЧто вы хотите сделать?')
    print('1. Введите номер аккаунта чтобы получить баланс и информацию по тестовому счету')
    print('2. Сделать транзакцию с одного тестового счета на другой')
    print('3. Создать новый аккаунт в сети Ethereum')
    print('4. Выйти')
    choice = input('Введите номер действия (1-4): \n')
    return choice


def main():
    connect_test_provider()
    invalid_attempts = 0

    while True:
        choice = display_menu()

        match choice:
            case '1':
                get_account_balance()
                invalid_attempts = 0
            case '2':
                perform_transaction()
                invalid_attempts = 0
            case '3':
                new_account()
                invalid_attempts = 0
            case '4':
                print('Выход из программы.')
                break
            case _:
                invalid_attempts += 1
                if invalid_attempts < 4:
                    print(f'Неверный номер действия. Попробуйте снова. ({invalid_attempts}/4)')
                else:
                    print('Слишком много неверных попыток. Программа завершается.')
                    break


if __name__ == '__main__':
    main()
