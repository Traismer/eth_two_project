from eth_project.connection import connect_test_provider
from eth_project.account import get_account, get_balance_eth


def main():
    connect_test_provider()
    try:
        acc = int(input('Введи номер аккаунта: '))
        address = get_account(acc)
        if address:
            balance = get_balance_eth(address)
            if balance is not None:
                print(f'Account {acc}:\nAddress - {address}\nBalance - {balance} ETH')
            else:
                print('Невозможно получить баланс аккаунта.')
        else:
            print('Неверный номер аккаунта.')
    except ValueError:
        print('Введенный номер аккаунта должен быть целым числом.')


if __name__ == '__main__':
    main()
