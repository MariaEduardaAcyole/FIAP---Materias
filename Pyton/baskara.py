print('\n === BASKARA ===')

# segundo grau 3x**2 + 2x -8 = 0
a = 3
b = 2
c = -8

delta = (b ** 2) - 4 * a * c
print('Delta = ', delta)

baskara1 = (b + delta ** (1 / 2)) / (2 * a)
baskara2 = (-b - delta ** (1 / 2)) / (2 * a)
print('X1 = ', baskara1)
print('X2 = ', baskara2)