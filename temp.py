import fractions as F
x = repr(F.Fraction(723520/51680)).split(', ')
z = ', '.join(x).split(', ')
print(z[0].strip('Fraction('))
print(z[1].strip(')'))