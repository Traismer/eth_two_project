# ETH Project

Это учебный проект для взаимодействия с тестовым стендом Ethereum с использованием Python и библиотеки Web3.

## Описание

Проект позволяет подключиться к тестовому стенду Ethereum, получить адрес и баланс выбранного тестового аккаунта.

## Требования

- Docker
- Poetry (если вы не используете Docker)

## Установка с использованием Docker

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/Traismer/eth_two_project.git
    cd eth_two_project
    ```

2. Постройте Docker-образ:
    ```sh
    docker build -t eth_two_project .
    ```

## Запуск с использованием Docker

1. Запустите контейнер:
    ```sh
    docker run -it --rm eth_two_project
    ```

2. Следуйте инструкциям на экране:
    - Введите номер аккаунта для получения адреса и баланса.

## Установка и запуск без Docker

### Требования

- Python 3.12
- Poetry
- Web3

### Установка без Docker

1. Клонируйте репозиторий:
    ```sh
    git clone https://github.com/Traismer/eth_two_project.git
    cd eth_two_project
    ```

2. Установите зависимости с помощью Poetry:
    ```sh
    poetry install
    ```

### Запуск без Docker

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

      |eth_two_project/
      │
      ├── eth_project/
      │   ├── __init__.py
      │   ├── connection.py
      │   ├── exceptions.py
      │   ├── account.py
      │
      ├── main.py
      ├── pyproject.toml
      ├── poetry.lock
      ├── Dockerfile
      ├── README.md

- **eth_project/connection.py**: подключение к тестовому стенду Ethereum.
- **eth_project/exceptions.py**: декоратор для обработки исключений.
- **eth_project/account.py**: функции для работы с аккаунтами и их балансом.
- **main.py**: основной скрипт для запуска программы.
- **pyproject.toml**: файл для управления зависимостями с помощью Poetry.
- **README.md**: документация проекта.
- **Dockerfile**: файл для сборки Docker-образа.

## Контрибуции

Если вы хотите сделать вклад в проект:

1. Форкните репозиторий
2. Создайте новую ветку (`git checkout -b feature/your-feature`)
3. Внесите изменения и закоммитьте (`git commit -am 'Add your feature'`)
4. Запушьте изменения (`git push origin feature/your-feature`)
5. Создайте Pull Request