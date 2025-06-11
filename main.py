def add(a: float, b: float) -> float:
    """Сложение двух чисел"""
    return a + b

def is_prime(n: int) -> bool:
    """Проверка числа на простоту"""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def factorial(n: int) -> int:
    """Вычисление факториала числа"""
    if n == 0:
        return 1
    return n * factorial(n - 1)

def find_max(numbers: list) -> float:
    """Поиск максимального числа в списке"""
    if not numbers:
        return None
    return max(numbers)

if __name__ == "__main__":
    # Примеры использования функций
    print("Сложение:", add(5, 3.5))
    print("Проверка на простоту:", is_prime(17))
    print("Факториал:", factorial(5))
    print("Максимальное число:", find_max([2, 1, 8, 4]))
