'''catOp = float(input('Comprimento do cateto oposto: '))
catAd = float(input('Comprimento do cateto adjacente: '))
hip = (catOp ** 2 + catAd ** 2) ** (1/2)
print('A hipotenusa vai medir {}'.format(hip))'''

import math
from math import hypot

co = float(input('Comprimento do cateto oposto:'))
ca = float(input('Comprimento do cateto adjacente: '))
hi = hypot(co, ca)
print('A hipotenusa vai medir {:.2f}'.format(hi))