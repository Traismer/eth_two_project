from .connection import w3
from .exceptions import handle_exceptions


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


# Экспортировать функции
__all__ = ["get_account", "get_balance_eth"]
