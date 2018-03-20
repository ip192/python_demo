
import math


# for index in range(5):
#     print('nothing'[index])


# var = 1
# while var < 5:
#     print(var)
#     var += 1
# else:
#     print('over')


# math try
print(len(dir(math)))
line = []
for item in range(len(dir(math))):
    line.append(dir(math)[item])
    if item % 10 == 0 and item / 10 > 0:
        print(line)
        line.clear()


