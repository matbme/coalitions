# pyright: basic
import itertools
import random
import sys
from pprint import pprint

from more_itertools import set_partitions

v = {
    (1,): 30,
    (2,): 40,
    (3,): 25,
    (4,): 45,
    # --------
    (1, 2): 50,
    (1, 3): 60,
    (1, 4): 80,
    (2, 3): 55,
    (2, 4): 70,
    (3, 4): 80,
    # --------
    (1, 2, 3): 90,
    (1, 2, 4): 120,
    (1, 3, 4): 100,
    (2, 3, 4): 115,
    # --------
    (1, 2, 3, 4): 140,
}

n = 4


def generate_coalition_values(n):
    coalition_values = {}
    for r in range(1, n + 1):
        for coalition in itertools.combinations(range(n), r):
            coalition_value = random.randint(1, 100)
            coalition_values[tuple(map(lambda x: x + 1, coalition))] = coalition_value

    return coalition_values


f1 = {}
f2 = {}

comps = 0


def compute_f2(c):
    global comps

    if not f2.get(c):
        print(f"f2 for {c} not found! Calculating.")
        max_f2_part = -sys.maxsize - 1
        max_f2_elem = ()
        for l, r in set_partitions(c, 2):
            print(f"Partitioned set into {l} and {r}")

            # E*
            if len(r) > n - (len(l) + len(r)) and len(l) + len(r) != n:
                print("Ignoring set partition")
                continue

            comps += 1

            f2_part = compute_f2(tuple(l)) + compute_f2(tuple(r))
            if f2_part >= max_f2_part:
                max_f2_part = f2_part
                max_f2_elem = tuple(l)  # Or r, doesn't matter. See footnote 3.

        f2[tuple(c)] = max_f2_part

        print(f"f2[{c}] = {f2[c]}, v[{c}] = {v[c]}")
        if f2[c] >= v[c]:
            # If f2[C] >= v[C], then set f1[C]:=C*
            print(f"Greater! Setting f1[{c}] to max elem {max_f2_elem}")
            f1[c] = max_f2_elem
        else:
            # If f2[C] < v[C], then set f1[C]:=C, and f2[C]:=v[C]
            print(f"Lesser. Setting f1[{c}] to itself")
            f1[c] = c
            f2[c] = v[c]

    print(f"f2 for {c} is {f2[c]}")
    return f2[c]


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
        v = generate_coalition_values(n)

    # For all i in {1,...,n}, set f1[{ai}]:={ai}, f2[ai]:=v[{ai}]
    for i in range(1, n + 1):
        f1[(i,)] = (i,)
        f2[(i,)] = v[(i,)]

    # For s:=2 to n, do:
    for s in range(1, n + 1):  # Changed to 1 so that it computes f1 and f2 for A
        # For all C subset-eq A such that |C|=s, do:
        for cs in set_partitions(range(1, n + 1), s):
            for c in cs:
                compute_f2(tuple(c))

    print("f tables built!")
    print("\nf1: ", end="")
    pprint(f1)
    print("\nf2: ", end="")
    pprint(f2)

    # Set CS*:={A}
    css = [tuple(range(1, n + 1))]

    done = False
    while not done:
        # For every C in CS*, do:
        for c in css:
            done = True
            # If f1[C] != C, then:
            if f1[c] != c:
                # Set CS* := (CS*\{C}) U {f1[C],S\f1[c]}
                splits = [tuple([e for e in c if e not in f1[c]]), f1[c]]
                css = [cs for cs in css if cs != c] + splits
                done = False

        if done:
            break

    print(
        f"\nOptimal coalition structure is {sorted(css)} with value {sum(f2[c] for c in css)}"
    )
    print(f"Finished with {comps} splittings")
