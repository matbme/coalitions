# pyright: basic
from math import factorial, ceil
import matplotlib.pyplot as plt

plt.style.use("seaborn-v0_8-colorblind")

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


def calculate_nss_idp(s: int) -> int:
    result = 0
    for spp in range(ceil(s / 2), s):
        if spp <= n - s:
            continue

        if (s - spp) == spp:
            result += possible_subsets(s, spp) // 2
        else:
            result += possible_subsets(s, spp)

    return result


x = []
t_plt = []
d_plt = []

for s in range(1, n + 1):
    cns = possible_subsets(n, s)
    nss = calculate_nss(s)

    t = cns * nss
    d = cns * calculate_nss_idp(s)
    print(f"s: {s:<5} cns: {cns:<15} nss: {nss:<15} t: {t:<15} d: {d}")

    x.append(s)
    t_plt.append(t)
    d_plt.append(d)

print("-" * 50)

print(f"t accumul.: {sum(t_plt)}")
print(f"d accumul.: {sum(d_plt)}")

fig, ax = plt.subplots(1, 2)
ax[0].plot(x, t_plt, "-o", label="DP")
ax[0].plot(x, list(map(lambda t, d: t - d, t_plt, d_plt)), "-o", label="IDP")
ax[0].legend()

ax[1].semilogy(x, list(map(lambda t: max(1, t), t_plt)), "-o", label="DP")
ax[1].semilogy(
    x, list(map(lambda t, d: max(1, t - d), t_plt, d_plt)), "-o", label="IDP"
)
ax[1].legend()
ax[1].set_ylim(bottom=1)

plt.tight_layout()
plt.savefig("splittings.pdf")
