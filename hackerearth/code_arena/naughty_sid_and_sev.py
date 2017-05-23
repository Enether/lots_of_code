from math import tan, pi, ceil

def calc_tan(theta):
    return tan(theta_max * pi / 180)

t = int(input())
for _ in range(t):
    a, H, theta_max = [int(p) for p in input().split()]
    h = None
    if theta_max == 0:
        h = H
    elif H / calc_tan(theta_max) > a:
        vol_temp = 0.5 * H * H / calc_tan(theta_max)
        b_temp = H / calc_tan(theta_max) - a
        h_temp = calc_tan(theta_max) * b_temp
        h = ceil((vol_temp - 0.5*b_temp  * h_temp) / a)
    else:
        vol_temp = 0.5 * H * H / calc_tan(theta_max)
        h = ceil(vol_temp/a)

    print(h)
