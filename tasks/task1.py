from math import factorial


# число на ввод для проверки программы 0.4078082482993198
def solution(result: float):
    calculation = 0
    n = 1
    while result != calculation:
        # условие, что каждый четный член отрицательный
        if n % 2 != 0:
            calculation += ((factorial(2 * n - 1)) / (n * factorial(2 * n)))
        else:
            calculation -= ((factorial(2 * n - 1)) / (n * factorial(2 * n)))
        print(n, calculation)
        n += 1
    print(f"Программа закончена на {n - 1}-ой итерации. Достигнута необходимая сумма ряда")


def main():
    result = float(input())
    solution(result)


if __name__ == '__main__':
    main()
