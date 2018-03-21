


class ClassTest:
    def __init__(self, name):
        self.init = True
        self.finish = False
        self.name = name

    def set_name(self, name):
        self.name = name
        return self.name


if __name__ == '__main__':
    test = ClassTest('ip192')
    print(test.name)
    print(test.set_name('ip193'))
