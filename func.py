from math import *
import math

zn = 0.7
Pi = math.pi
r_gr = Pi / 6
tochn = 0.001
mid_gr = Pi / 12
l_gr = 0
while abs(math.tg(mid_gr) - zn) > tochn:
    mid_gr = (l_gr + r_gr) / 2
    if math.sin(mid_gr) > 0.3:
        r_gr = mid_gr
    else:
        l_gr = mid_gr

print(mid_gr)