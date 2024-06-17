from dataclasses import dataclass, field, asdict
from typing import Any, List, Union
from eth_project.connection import w3
from eth_project.exceptions import handle_exceptions
from eth_project.blocks import to_hex


@dataclass
class TransactionReceipt:
    status: int
    transactionHash: str
    transactionIndex: int
    blockHash: str
    blockNumber: int
    from_address: str
    to_address: Union[str, None]
    cumulativeGasUsed: int
    gasUsed: int
    contractAddress: Union[str, None]
    logs: List[Any] = field(default_factory=list)
    logsBloom: str = ''
    root: Union[str, None] = None

    def __str__(self):
        return self.to_str()

    def to_str(self, indent: int = 4) -> str:
        return str(asdict(self)).replace(", '", ",\n" + " " * indent + "'")


@dataclass
class TransactionInfo:
    hash: str
    nonce: int
    blockHash: str
    blockNumber: int
    transactionIndex: int
    from_address: str
    to_address: str
    value: int
    gas: int
    input: str

    def __str__(self):
        return self.to_str()

    def to_str(self, indent: int = 4) -> str:
        return str(asdict(self)).replace(", '", ",\n" + " " * indent + "'")


@handle_exceptions
def send_transaction(from_account, to_account, value_in_eth):
    """
    Отправляет указанное количество эфира с одного аккаунта на другой.

    :param from_account: Адрес аккаунта отправителя.
    :param to_account: Адрес аккаунта получателя.
    :param value_in_eth: Сумма в эфире для отправки.
    :return: Хеш транзакции.
    """
    tx_hash = w3.eth.send_transaction({
        'from': from_account,
        'to': to_account,
        'value': w3.to_wei(value_in_eth, 'ether')
    })
    return tx_hash


@handle_exceptions
def wait_for_transaction_receipt(tx_hash):
    """
    Ожидает включения транзакции в блок и возвращает квитанцию о транзакции.

    :param tx_hash: Хеш транзакции.
    :return: Квитанция о транзакции.
    """
    receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
    return TransactionReceipt(
        status=receipt.get('status', 0),
        transactionHash=receipt['transactionHash'].hex(),
        transactionIndex=receipt['transactionIndex'],
        blockHash=receipt['blockHash'].hex(),
        blockNumber=receipt['blockNumber'],
        from_address=receipt['from'],
        to_address=receipt.get('to'),
        cumulativeGasUsed=receipt['cumulativeGasUsed'],
        gasUsed=receipt['gasUsed'],
        contractAddress=receipt.get('contractAddress'),
        logs=receipt['logs'],
        logsBloom=to_hex(receipt.get('logsBloom', b'')),
        root=receipt.get('root')
    )


@handle_exceptions
def get_transaction_info(tx_hash):
    """
    Получает информацию о транзакции по её хешу.

    :param tx_hash: Хеш транзакции.
    :return: Словарь с информацией о транзакции.
    """
    tx_info = w3.eth.get_transaction(tx_hash)
    return TransactionInfo(
        hash=tx_info['hash'].hex(),
        nonce=tx_info['nonce'],
        blockHash=tx_info['blockHash'].hex(),
        blockNumber=tx_info['blockNumber'],
        transactionIndex=tx_info['transactionIndex'],
        from_address=tx_info['from'],
        to_address=tx_info['to'],
        value=tx_info['value'],
        gas=tx_info['gas'],
        input=tx_info['input']
    )
