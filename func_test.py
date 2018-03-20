from send_err_email import send


out = 'outer'

def none(strr):
    print(out)
    print(strr)


def person(name, age):
    print(out)
    print(name, age)


def normal(normal1, normal2):
    print(normal1, normal2)

normal(normal2 = '1', normal1='2')

send('w_angpeng@sina.cn', 'error found by python')