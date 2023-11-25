from sympy import symbols, Eq, solve

c = 229 % 10

I1, I2, I3 = symbols('I1 I2 I3')

V1 = (c + 2) * 4
V2 = (c + 1) * 5

R1, R2, R3 = 12, 4, 6

eq1 = Eq(I1, I2 + I3)
eq2 = Eq(V1, I1*R1 + I3*R3)
eq3 = Eq(V2, I2*R2 - I3*R3)

solutions = solve((eq1, eq2, eq3), (I1, I2, I3))

print('I1 = ', solutions[I1])
print('I2 = ', solutions[I2])
print('I3 = ', solutions[I3])
