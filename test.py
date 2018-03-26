#!/usr/local/bin/python3
# 这是我写的第一个 .py 文件, IDE是jetbrains看到

# from level import level_print
# level_print

from level.ClassTest import *
from level.level_print import *


# print(le.out_param)
# le.out_fun()

a = [1, 2, 3]
b = ['a', 'b', 'c', 'd']
c = map(lambda x,y: str(x) + y, a, b)
# for i in c:
    # print(i)

# print('first: %c, second: %c' % ('a', 'b'))
# print('first: %s, second: %s' % ('aa', 'ba'))


def use_out(out):
    out.out()

use_out(ClassTest('ip192'))
use_out(Level())