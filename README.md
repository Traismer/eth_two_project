# ETH Project

Это учебный проект для взаимодействия с тестовым стендом Ethereum с использованием Python и библиотеки Web3.

## Описание

Проект позволяет подключиться к тестовому стенду Ethereum, получить адрес и баланс выбранного тестового аккаунта.

## Требования

- Python 3.12
- Poetry
- Web3

## Установка

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/yourusername/eth_project.git
    cd eth_project
    ```

2. Установите зависимости:
    ```sh
    poetry install
    ```

## Использование

1. Активируйте виртуальное окружение:
    ```sh
    poetry shell
    ```

2. Запустите программу:
    ```sh
    python main.py
    ```

3. Следуйте инструкциям на экране:
    - Введите номер аккаунта для получения адреса и баланса.

## Структура проекта
    |eth_project/
        ├── init.py │ 
        ├── connection.py 
        ├── exceptions.py 
        ├── account.py
    ├── main.py 
    ├── pyproject.toml 
    └── README.md


- **eth_project/connection.py**: подключение к тестовому стенду Ethereum.
- **eth_project/exceptions.py**: декоратор для обработки исключений.
- **eth_project/account.py**: функции для работы с аккаунтами и их балансом.
- **main.py**: основной скрипт для запуска программы.
- **pyproject.toml**: файл для управления зависимостями с помощью Poetry.
- **README.md**: документация проекта.

## Контрибуции

Если вы хотите сделать вклад в проект:
1. Форкните репозиторий
2. Создайте новую ветку (`git checkout -b feature/your-feature`)
3. Внесите изменения и закоммитьте (`git commit -am 'Add your feature'`)
4. Запушьте изменения (`git push origin feature/your-feature`)
5. Создайте Pull Request