from web3 import Web3

w3 = Web3(Web3.EthereumTesterProvider())


def handle_exceptions(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as e:
            print(f'Произошла ошибка: {e}')
            return None
        except IndexError as e:
            print(f'Произошла ошибка: {e}')
            return None

    return wrapper


@handle_exceptions
def get_account(index):
    """
    Получаем аккаунт из тестового стенда.
    :param index: Индекс аккаунта
    :return: адрес аккаунта
    """
    accounts = w3.eth.accounts
    return accounts[index]


@handle_exceptions
def get_balance_eth(account):
    """
    Получаем баланс ETH (эфира) в аккаунте.
    :param account: Адрес аккаунта
    :return: Decimal или None, если произошла ошибка
    """
    balance = w3.eth.get_balance(account)
    return w3.from_wei(balance, 'ether')


def main():
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
