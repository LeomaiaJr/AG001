from sympy import Symbol, solve, tan

c = 229 % 10


def eq1(x):
    return (2**x) + (2 ** (4*x)) - 1 - c


x = Symbol('x')
y = eq1(x)
result = solve(y)

print('Resultado Equação 1: ', result)


def eq2(w):
    return 5*(w**(1/2)) - (4 * (w**2)) + (w/2) - c


w = Symbol('w')
z = eq2(w)
result2 = solve(z)

print('Resultado Equação 2: ', result2)


def eq3(a):
    return ((3 * tan((c - 3) * a)) + 2) ** 2


a = Symbol('a')
b = eq3(a)
result3 = solve(b)

print('Resultado Equação 3: ', result3)
