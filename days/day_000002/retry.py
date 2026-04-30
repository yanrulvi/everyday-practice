"""
Написать декоратор @retry. Декоратор должен повторно вызывать функцию, если она выбросила исключение.
Параметры: max_retries=3, delay=1 (секунда между попытками).

Проверить на функции: Напишите функцию unstable_function(), которая случайно (с вероятностью 0.6)
падает с ValueError. Оберните её в @retry и вызовите 5 раз.

Вывод в консоль: При каждом падении печатать "Retry X/3...".
При успехе — печатать "Success after Y retries".
"""

import random
import time


def retry(max_retries=3, delay=1):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"Retry {attempt+1}/{max_retries}: {e}")
                    time.sleep(delay)
            print("All retries failed")

        return wrapper

    return decorator


@retry()
def unstable_function():
    value = random.uniform(0.0, 1.0)
    if value <= 0.6:
        print(f"ERROR: {value:.2f} <= 0.6")
        raise ValueError


def main():
    unstable_function()


if __name__ == "__main__":
    main()
