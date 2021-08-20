# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
import heapq
from collections import Counter, namedtuple


class Node(namedtuple('Node', ['left', 'right'])):
    def walk(self, code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')


class Leaf(namedtuple('Leaf', ['char'])):
    def walk(self, code, acc):
        code[self.char] = acc or '0'


def haffman_encode(arg):
    list_to_tree = []
    for char, rate in Counter(arg).items():
        list_to_tree.append([rate, len(list_to_tree) + len(Counter(arg)), Leaf(char)])
    heapq.heapify(list_to_tree)
    count = 0
    while len(list_to_tree) > 1:
        freq1, count1, left = heapq.heappop(list_to_tree)
        freq2, count2, right = heapq.heappop(list_to_tree)
        heapq.heappush(list_to_tree, [freq1 + freq2, count, Node(left, right)])
        count -= 1
    code = {}
    if list_to_tree:
        [(rate, count, tree)] = list_to_tree
        tree.walk(code, '')
    return code


if __name__ == '__main__':
    my_str = 'beep boop beer!'
    code_dict = haffman_encode(my_str)
    encoded = ''.join(code_dict[el] for el in my_str)
    print(f'Закодированная строка: {encoded}')
