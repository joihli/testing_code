import numpy as np


def square(x):
    return x * x


def culomb(x):
    assert type(x) in [float, int], " You pasesed and invalid argument"
    if abs(x) == 0:
        return 0
    else:
        return 1 / abs(r)


def centraldifference(f, x, h):
    # f(x+h)-f(x-h)
    # ------------\approx f'(x)
    #          2*h
    return (f(x + h) - f(x - h)) / (2 * h)

# for i in range(2,8):
#   h=10**(-i)
#    print (h,abs(CentralDifference(np,sin))
