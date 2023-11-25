from math import pi
from sympy import Derivative, Integral, Symbol, cos

c = 229 % 10


def v(x):
    return 15 * 40 * pi * cos((40 * pi * x) - c)


x = Symbol('x')

aceleracao = Derivative(v(x), x).doit()
deslocamento = Integral(v(x), x).doit()

print('Aceleração: ', aceleracao)
print('Deslocamento: ', deslocamento)
print('Aceleração em t = 10: ', aceleracao.subs({x: 10}))
