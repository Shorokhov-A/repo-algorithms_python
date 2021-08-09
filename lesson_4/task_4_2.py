# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
#    - Без использования «Решета Эратосфена»;
#    - Использовать алгоритм «Решето Эратосфена»


from math import log
from cProfile import run


def prime_counting(i):
    """
    Функция возвращает верхнюю границу массива целых чисел, в
    котором находятся i простых чисел. Функция основана на теореме о
    распределении простых чисел. Она утверждает, что количество
    простых чисел на отрезке [1:n] растёт с увеличением n как n / ln(n).
    """

    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / log(number)
        number += 1
    return number


def prime_number(i):
    """
    Функция поиска i-го простого числа,
    без использования алгоритма «Решето Эратосфена».
    Сложность алгоритма O(n^2).
    """

    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]


def eratosthenes_prime_number(i):
    """
    Функция поиска i-го простого числа,
    используя алгоритм «Решето Эратосфена».
    Сложность алгоритма - O(n * log(n))
    """

    i_max = prime_counting(i)
    a = []
    for idx in range(i_max):
        a.append(idx)
    a[1] = 0
    m = 2
    while m < i_max:
        if a[m] != 0:
            j = m * 2
            while j < i_max:
                a[j] = 0
                j = j + m
        m += 1
    b = []
    for item in a:
        if item != 0:
            b.append(item)
    return b[i - 1]


print(prime_number(10))
print(eratosthenes_prime_number(10))
# Алгоритм нахождения i-го по счету простого числа с использованием Решета Эратосфена должен работать быстрее, чем
# алгоритм без его использования. Проверим это предположение на практике.
run(f'prime_number({10000})')
run(f'eratosthenes_prime_number({10000})')
# Практический тест показал, что алгоритм нахождения i-го по счету простого числа с использованием Решета Эратосфена
# работает значительно быстрее.
