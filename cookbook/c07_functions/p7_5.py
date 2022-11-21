_NO_VALUE = object()

global x


def spam(a, b=_NO_VALUE):
    if b is _NO_VALUE:
        print('No b value supplied')
    print(f'a = {a}, b = {b}')

x = 20
spam(1)
x = 4444
spam(1)
