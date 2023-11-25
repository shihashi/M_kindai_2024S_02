#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# M_kindai_2024S_02_B.py
#
# Copyright (c) 2023 shihashi
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

from abc import ABCMeta, abstractmethod
from collections.abc import Iterable, Sequence, Callable
from typing import Self, Literal
from itertools import permutations, product

Coin = Literal[1, 5, 10, 50, 100, 500]
COINS: Sequence[Coin] = (1, 5, 10, 50, 100, 500)

class NotUniqueException(Exception):
    pass

class Question(metaclass=ABCMeta):
    '''基底クラス'''
    def __init__(self, letters: str, condition: Callable[[Sequence[Coin]], bool]):
        self.__letters: str = letters
        self._condition: Callable[[Sequence[Coin]], bool] = condition
        self._value: int = 0

    @abstractmethod
    def count(self, arrangement: Sequence[Coin]) -> None:
        pass

    def print_answer(self) -> None:
        print(f'{self.__letters} {self._value}')

class Count(Question):
    '''数える問題'''
    def count(self, arrangement: Sequence[Coin]):
        if self._condition(arrangement):
            self._value += 1

class UniqueSum(Question):
    '''唯一の合計値を求める問題'''
    def count(self, arrangement: Sequence[Coin]) -> None:
        if self._condition(arrangement):
            if self._value != sum(arrangement) and self._value != 0:
                raise NotUniqueException()
            else:
                self._value = sum(arrangement)

class MinSum(Question):
    '''合計の最小値を求める問題'''
    def count(self, arrangement: Sequence[Coin]) -> None:
        if self._condition(arrangement):
            if self._value == 0 or self._value > sum(arrangement):
                self._value = sum(arrangement)

class LargeQuestion:
    def __init__(self, iter: Iterable[Sequence[Coin]], question_list: Sequence[Question]):
        self.__iter: Iterable[Sequence[Coin]] = iter
        self.__question_list: Sequence[Question] = question_list

    def count(self) -> Self:
        for each_arrangement in self.__iter:
            for question in self.__question_list:
                question.count(each_arrangement)
        return self

    def print_answer(self) -> None:
        for question in self.__question_list:
            question.print_answer()


def main():
    LargeQuestion(permutations(COINS, 4),
                  [
                      Count('アイウ', lambda x: True),
                      UniqueSum('エオカ', lambda x: (x[0] + x[1]) % 10 == 0 and (x[2] + x[3]) % 10 == 0),
                      Count('キク', lambda x: (x[0] + x[1]) % 10 == 0 and (x[2] + x[3]) % 10 == 0),
                      Count('ケコ', lambda x: (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 2 == 0 and (x[0] + x[2]) % 2 == 1 and (x[1] + x[3]) % 2 == 1),
                      Count('サシス', lambda x: (x[0] + x[1] > 500 or x[2] + x[3] > 500) and (x[0] + x[2] < 100 or x[1] + x[3] < 100))
                  ]).count().print_answer()

    LargeQuestion(product(COINS, repeat = 4),
                  [
                      Count('セソタチ', lambda x: True),
                      Count('ツテ', lambda x: (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 5 == 0 and (x[0] + x[2]) % 10 == 0 and (x[1] + x[3]) % 100 == 0),
                      MinSum('トナニ', lambda x: (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 5 == 0 and (x[0] + x[2]) % 10 == 0 and (x[1] + x[3]) % 100 == 0)
                  ]).count().print_answer()


if __name__ == '__main__':
    main()
