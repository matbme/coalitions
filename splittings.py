# pyright: basic
from math import factorial, ceil
import matplotlib.pyplot as plt

n = 25


def possible_subsets(n: int, s: int) -> int:
    return factorial(n) // (factorial(n - s) * factorial(s))


def calculate_nss(s: int) -> int:
    result = 0
    for spp in range(ceil(s / 2), s):
        if (s - spp) == spp:
            result += possible_subsets(s, spp) // 2
        else:
            result += possible_subsets(s, spp)

    return result


x = []
y = []
for smax in range(2, n + 1):
    t: float = 0
    for s in range(1, n + 1):
        cns = possible_subsets(n, smax)
        nss = calculate_nss(smax)
        t += cns * nss

    x.append(smax)
    y.append(t)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y, "-o")
ax[1].plot(x, y, "-o")
ax[1].set_yscale("log")

plt.tight_layout()
plt.show()
