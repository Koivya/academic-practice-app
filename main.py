def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

if __name__ == "__main__":
    print("Сложение:", add(5, 3.5))
    print("Проверка на простоту:", is_prime(17))
    