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


def validate_index(index, max_index):
    """
    Проверяет, является ли индекс валидным (целым числом и неотрицательным).

    :param index: Индекс для проверки.
    :param max_index: Максимально допустимый индекс.
    :return: True, если индекс валиден, иначе False.
    """
    if not isinstance(index, int) or index < 0 or index >= max_index:
        print(f'Неверный индекс: {index}. Должен быть числом в диапазоне 0 - {max_index - 1}.')
        return False
    return True


def validate_eth_value(value):
    """
    Проверяет, является ли значение ETH валидным (неотрицательным числом).

    :param value: Значение ETH для проверки.
    :return: True, если значение валидно, иначе False.
    """
    if not isinstance(value, (int, float)) or value <= 0:
        print(f'Неверное значение ETH: {value}. Должно быть положительным числом.')
        return False
    return True


# Экспортировать функции
__all__ = ['get_account', 'get_balance_eth', 'validate_index', 'validate_eth_value']
