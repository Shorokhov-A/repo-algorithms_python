# 1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая
# только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.
# ------------------------------------------------------------------------------------------------------------------
import hashlib


def str_encode(arg):
    result = hashlib.sha1(arg.encode('utf-8')).hexdigest()
    return result


def dif_sub_strs(arg):
    sub_strs_set = set()
    arg_hash = str_encode(arg)
    for i in range(len(arg)):
        sub_str_hash = str_encode(arg[i])
        sub_strs_set.add(sub_str_hash)
        for j in range(i + 1, len(arg)):
            j += 1
            sub_str_hash = str_encode(arg[i:j])
            if sub_str_hash != arg_hash:
                sub_strs_set.add(sub_str_hash)
    result = len(sub_strs_set)
    return result


if __name__ == '__main__':
    my_string = 'kyahekbtyfhrn'
    print(f'Количество различных подстрок в строке "{my_string}": {dif_sub_strs(my_string)}')
