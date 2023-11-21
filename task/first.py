#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    num = tuple(map(int, input('Введите числа: ').split()))
    result = []
    for i, char in enumerate(num):
        if i + 2 > len(num):
            break
        elif num[i-1] < num[i] > num[i+1]:
            result = num[:i-1]

    if result:
        print(result)
    else:
        print("Тройки соседних чисел с условием не найдено.")

