

class ClassTest:

    def __init__(self, name):
        self.init = True
        self.finish = False
        self.name = name
        self._inner = 'inner'

    def set_name(self, name):
        self.name = name
        return self.name

    def __private(self):
        print('__')

    def get_inner(self):
        return self._inner

    def out(self):
        print('class test out')

# if __name__ == '__main__':
#     test = ClassTest('ip192')
#     test._inner = 'outer'
#     print(test.get_inner())
#     print(test.name)
#     print(test.set_name('ip193'))
#     print(isinstance(test, ClassTest))
