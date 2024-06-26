from math import factorial


def solution(n: float, x: float):
    calculation = 1
    for i in range(1, int(n) + 1):
        if i % 2 != 0:
            calculation -= x / factorial(i)
        else:
            calculation += x / factorial(i)
        print(i, calculation)


def main():
    print("Введите числа n и x в строку через пробел, где n - точность ряда, x - число разложения")
    n, x = map(float, input().split())
    solution(n, x)


if __name__ == '__main__':
    main()
