from sympy import Limit, Symbol, S

c = 229 % 10


def lim1(x):
    return (1 + ((c + 4) / x**3)) ** (x**3)


x = Symbol('x')

Result1 = Limit(lim1(x), x, 0).doit()
Result2 = Limit(lim1(x), x, S.Infinity).doit()
Result3 = Limit(lim1(x), x, -S.Infinity).doit()

print('Resutado 1:', Result1)
print('Resutado 2:', Result2)
print('Resutado 3:', Result3)
