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


# Экспортировать декоратор
__all__ = ["handle_exceptions"]
