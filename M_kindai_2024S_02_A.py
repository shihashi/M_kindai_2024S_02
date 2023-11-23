#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# M_kindai_2024S_02_A.py
#
# Copyright (c) 2023 shihashi
#
# Released under the MIT license.
# see https://opensource.org/licenses/mit-license.php
#

from itertools import permutations, product

COINS = [1, 5, 10, 50, 100, 500]

print("アイウ {}".format(len(list(permutations(COINS, 4)))))
print("エオカ {}".format(','.join([str(y) for y in
                                {x[0] + x[1] + x[2] + x[3] for x in permutations(COINS, 4) if (x[0] + x[1]) % 10 == 0 and (x[2] + x[3]) % 10 == 0 }])))
print("キク {}".format(len([x for x in permutations(COINS, 4)
                        if (x[0] + x[1]) % 10 == 0 and (x[2] + x[3]) % 10 == 0 ])))
print("ケコ {}".format(len([x for x in permutations(COINS, 4)
                        if (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 2 == 0 and (x[0] + x[2]) % 2 == 1 and (x[1] + x[3]) % 2 == 1 ])))
print("サシス {}".format(len([x for x in permutations(COINS, 4)
                        if (x[0] + x[1] > 500 or x[2] + x[3] > 500) and (x[0] + x[2] < 100 or x[1] + x[3] < 100) ])))
print("セソタチ {}".format(len(list(product(COINS, repeat = 4)))))
print("ツテ {}".format(len([x for x in product(COINS, repeat = 4)
                        if (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 5 == 0 and (x[0] + x[2]) % 10 == 0 and (x[1] + x[3]) % 100 == 0 ])))
print("トナニ {}".format(min([sum(x) for x in product(COINS, repeat = 4)
                        if (x[0] + x[1]) % 2 == 0 and (x[2] + x[3]) % 5 == 0 and (x[0] + x[2]) % 10 == 0 and (x[1] + x[3]) % 100 == 0 ])))
