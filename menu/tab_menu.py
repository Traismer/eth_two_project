from eth_project.account import create_account, validate_index, validate_eth_value, get_account, get_balance_eth
from eth_project.blocks import to_hex
from eth_project.connection import w3
from eth_project.transaction import send_transaction, wait_for_transaction_receipt, get_transaction_info


def get_account_balance():
    try:
        acc = int(input('Введите номер аккаунта: '))
        address = get_account(acc)
        accounts = w3.eth.accounts
        if not validate_index(acc, len(accounts)):
            return
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


def perform_transaction():
    try:
        from_acc = int(input('Введите номер аккаунта-отправителя: '))
        to_acc = int(input('Введите номер аккаунта-получателя: '))
        value_in_eth = float(input('Введите количество ETH для отправки: '))

        accounts = w3.eth.accounts
        if not (validate_index(from_acc, len(accounts)) and validate_index(to_acc, len(accounts))):
            return

        if not validate_eth_value(value_in_eth):
            return

        from_address = get_account(from_acc)
        to_address = get_account(to_acc)
        if not from_address or not to_address:
            print('Неверный номер аккаунта.')
            return

        from_balance = get_balance_eth(from_address)
        if from_balance < value_in_eth:
            print(f'Недостаточно средств на аккаунте {from_address}. Доступно только {from_balance} ETH.')
            return

        # Отправка транзакции
        tx_hash = send_transaction(from_address, to_address, value_in_eth)

        # Ожидание включения транзакции в блок
        receipt = wait_for_transaction_receipt(tx_hash)

        # Получение информации о транзакции
        tx_info = get_transaction_info(tx_hash)

        # Проверка баланса аккаунтов
        from_balance = get_balance_eth(from_address)
        to_balance = get_balance_eth(to_address)

        # Вывод минимальной информации
        print(f'Transaction completed, hash: {tx_hash.hex()}')
        print(f'New balance for address {from_address}: {from_balance} ETH')
        print(f'New balance for address {to_address}: {to_balance} ETH')

        # Optional: возвращаемые данные могут быть использованы в дальнейших функциях
        return {
            'tx_hash': tx_hash,
            'receipt': receipt,
            'tx_info': tx_info,
            'from_balance': from_balance,
            'to_balance': to_balance
        }
    except ValueError:
        print('Ошибка: введите корректное числовое значение.')
    except Exception as e:
        print(f'Произошла ошибка: {e}')


def new_account():
    try:
        address, key = create_account()
        print(f'Аккаунт создан: {address}')
        print(f'Закрытый ключ: {to_hex(key)}')
    except Exception as e:
        print(f'Произошла ошибка: {e}')
