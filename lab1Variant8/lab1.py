from functools import reduce
from typing import List
import itertools

math_operators = ['/', '*', '-', '+']
brackets = ['(', ')']


def parse_math(string: str):
    stack = parse_string(string)
    for i in math_operators:
        loop = True
        while loop:
            k = 0
            while True:
                _stack = evaluate_expression(stack, k, i)
                if _stack is False:
                    k += 1
                if k == len(stack):
                    loop = False
                    break
    return stack[0]


def reform_stack(stack: List, expression: float, k: int):
    stack.pop(k + 1)
    stack.pop(k)
    stack.insert(k, expression)
    stack.pop(k - 1)


def parse_string(string: str):
    stack = []
    num = ''
    for i, obj in enumerate(string):
        if obj not in math_operators and obj not in brackets:
            num += obj
            if i == len(string) - 1 or (string[i + 1] in math_operators or string[i + 1] in brackets):
                stack.append(num)
                num = ''
        elif obj not in brackets:
            stack.append(obj)
    return stack


def evaluate_expression(stack: List, k: int, i: str):
    if i == stack[k] and stack[k] == '+':
        expression = float(stack[k - 1]) + float(stack[k + 1])
        reform_stack(stack, expression, k)
        return True
    if i == stack[k] and stack[k] == '-':
        expression = float(stack[k - 1]) - float(stack[k + 1])
        reform_stack(stack, expression, k)
        return True
    if i == stack[k] and stack[k] == '*':
        expression = float(stack[k - 1]) * float(stack[k + 1])
        reform_stack(stack, expression, k)
        return True
    if i == stack[k] and stack[k] == '/':
        expression = float(stack[k - 1]) / float(stack[k + 1])
        reform_stack(stack, expression, k)
        return True
    return False


def anagrams(word, words):
    _anagrams = []
    for _word in words:
        if set(word) == set(_word):
            _anagrams.append(''.join(_word))
    return _anagrams


def valid_parentheses(string):
    i = 0
    if len(string) > 0:
        while i != len(string) - 1:
            if len(string) == 0:
                break
            if string[i] == '(' and ')' in string:
                if i < string.index(')'):
                    string = string.replace(')', '', 1)
                    string = string.replace('(', '', 1)
                    i = 0
                    continue
            i += 1
    if '(' not in string and ')' not in string:
        return True
    return False


def max_sequence(arr):
    if len(arr) > 0:
        _max = arr[0]
    else:
        return 0
    for i in range(len(arr) + 1):
        for k in range(len(arr) + 1):
            _max = sum(arr[i:k:]) if sum(arr[i:k:]) > _max else _max
    return _max


def rot13(message):
    lower = [64 < ord(x) < 91 for x in message]
    message = [ord(x.lower()) for x in message]
    result_list = []
    for i, let in enumerate(message):
        if let + 13 > 122:
            _let = 96 - (122 - let) + 13
        elif 96 < let < 122:
            _let = let + 13
        else:
            _let = let
        result_list.append(chr(_let)) if lower[i] is False else result_list.append(chr(_let).upper())
    return ''.join(result_list)


def sum_pairs(ints, s):
    cache = set()
    for i in ints:
        if s - i in cache:
            return [s - i, i]
        cache.add(i)


def sum_pairss(ints, s):
    indexses = {}
    for i in itertools.combinations(enumerate(ints), 2):
        if i[0][1] + i[1][1] == s:
            indexses.update({abs(i[0][0] - i[1][0]): [i[0][0], i[1][0]]})
    return [ints[indexses[min(indexses)][0]], ints[indexses[min(indexses)][1]]] if indexses else None


def next_bigger(n):
    s = list(str(n))
    for i in range(len(s) - 2, -1, -1):
        if s[i] < s[i + 1]:
            t = s[i:]
            m = min(filter(lambda x: x > t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1


def pick_peaks(arr):
    _arr = {"pos": [], "peaks": []}
    if len(set(arr)) == 1 or not arr:
        return _arr
    i = 1
    while i != len(arr) - 1:
        if arr[i] > arr[i + 1] and arr[i] > arr[i - 1]:
            _arr["pos"].append(i)
            _arr["peaks"].append(arr[i])
        elif arr[i] == arr[i + 1]:
            buf_arr = arr.copy()
            k = i
            pre_buf = arr[k - 1]
            buf = arr[k]
            while buf == buf_arr[k + 1]:
                buf_arr.pop(k)
                if len(buf_arr) - 1 == k:
                    break
                i += 1
            if len(buf_arr) - 1 == k:
                break
            if pre_buf < buf > buf_arr[k + 1]:
                _arr["pos"].append(k)
                _arr["peaks"].append(arr[k])
                continue
            else:
                continue
        i += 1
    return _arr


def pick_peakss(arr):
    pos = []
    prob_peak = False
    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            prob_peak = i
        elif arr[i] < arr[i - 1] and prob_peak:
            pos.append(prob_peak)
            prob_peak = False
    return {'pos': pos, 'peaks': [arr[i] for i in pos]}


def sum_of_intervals(intervals):
    _arr = []
    arr = []
    buf_arr = []
    for val in intervals:
        if val not in _arr:
            _arr.append(val)
    for i, val in enumerate(_arr):
        for k, _val in enumerate(_arr):
            if val != _val:
                if _val[1] > val[1] > val[0] and _val[1] > _val[0] > val[0] and val[1] > _val[0] \
                        and [val[0], val[1]] not in _arr:
                    buf_arr.append([val[0], _val[1]])
    for val in buf_arr:
        arr.append(reduce(lambda x, y: x - y, val[::-1]))
    return sum(arr)


switch = input()
if switch == '1':
    print(parse_math('(25476.231+123)-2134/3214.321*(231.3215+3214.9021)-312.041+321/2'))
if switch == '2':
    print(anagrams('racer', ['crazer', 'carer', 'racar', 'caers', 'racer']))
if switch == '3':
    valid_parentheses('((())()())')
if switch == '4':
    print(max_sequence([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
if switch == '5':
    print(rot13("grfg"))
if switch == '6':
    print(sum_pairs(
        [4, 3, 4, 5, 2, 34, 4, 1, 2, 32, 5, 2, 1, 42, 4, 5, 5, 6, 7, 7, 8, 8, 9, 9, 0, 0, 0, 0, 0, 5, 3, 2, 1, 1, 2, 2,
         3, 4], 6))
if switch == '7':
    print(next_bigger(512))
if switch == '8':
    print(pick_peakss([]))
if switch == '9':
    print(sum_of_intervals([(1, 5), (6, 10)]))
