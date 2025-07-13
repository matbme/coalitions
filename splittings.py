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
for s in range(1, n + 1):
    t = 0
    cns = possible_subsets(n, s)
    nss = calculate_nss(s)
    print(f"s: {s} \t cns: {cns} \t nss: {nss} \t t: {cns * nss}")

    t += cns * nss

    x.append(s)
    y.append(t)

print("-" * 50)

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, y, "-o")
ax[1].plot(x, y, "-o")
ax[1].set_yscale("log")

plt.tight_layout()
plt.show()
