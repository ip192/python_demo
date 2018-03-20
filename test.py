#!/usr/local/bin/python3
# 这是我写的第一个 .py 文件, IDE是netBrain看到
a = 'first'
b = 'seconde'


num = [a, 2, 3.3, 'four']
mun = [b, 'third', 'two']
print(num + mun)
# print(num * 2)
print(num, ',', mun)
print(num[2:])  # 记得shell里面也有这类似的写法

print()
obj = {}
obj['a'] = a
# obj[num] = a  # unhashable type 'list'
obj['b'] = b
obj[3] = 3
obj[3] = 4  # 被覆盖
print(obj)
print(obj.keys())

print()
tupl1 = tuple('key',)
list1 = list('key',)
print(tupl1, list1)

