def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)

if __name__ == "__main__":
    print("Факториал:", factorial(5))
    