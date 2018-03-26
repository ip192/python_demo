from send_err_email import send


class Person:

    def info(self):
        print('person info')


p = Person()
p.info()
p.name = 'ip192'
print(p.name)
Person.name = 'ip193'
print(Person.name, p.name)

print()
class Man:
    __slots__ = ('name', )

    def info(self):
        print('person info')

m = Man()
m.name = 'man'
print(m.name)
Man.name = 'Man'
print(Man.name)

# m.age = 24
Man.age = 24
print(Man.age)
