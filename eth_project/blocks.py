from eth_project.connection import w3
from eth_project.exceptions import handle_exceptions


def to_hex(value):
    """
    Преобразует байтовое значение в шестнадцатеричное представление.

    :param value: Значение для преобразования.
    :return: Шестнадцатеричное строковое представление байтов либо оригинальное значение.
    """
    return value.hex() if isinstance(value, bytes) else value


@handle_exceptions
def get_info_block(position):
    """
    Получает информацию о блоке и выводит её в читаемом формате.

    :param position: Позиция блока (например, 'latest' для последнего блока).
    ['latest', 'earliest', 'pending', 'safe', 'finalized']
    """
    block = w3.eth.get_block(position)
    for key, value in block.items():
        print(f'{key} - {to_hex(value)}')
