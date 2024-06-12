from web3 import Web3

w3 = Web3(Web3.EthereumTesterProvider())


def connect_test_provider():
    if w3.is_connected():
        print('Подключение к тестовому стенду успешно.')
    else:
        print('Не удалось подключиться к тестовому стенду.')


# Экспортировать объект w3
__all__ = ["w3", "connect_test_provider"]
