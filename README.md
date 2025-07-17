# Coalition Structure generation

This repository contains code reproducing the algorithms from the paper _An Improved Dynamic Programming Algorithm for Coalition Structure Generation_ by Rahwan and Jennings (2008), which can be found [here](https://eprints.soton.ac.uk/265062/).

## Running DP and IDP

Both DP and IDP have the same parameter settings:

```sh
$ python idp.py  # Will wun IDP with the same coalition values found in Figure 2 of the paper
$ python idp.py 10  # Will run IDP with 10 agents whose coalition values are randomly generated (but controlled by a hard-coded seed for reproducibility)
```

Be aware that calculating the optimal coalition structure for numbers of agents greater than 12 can take **a lot** of time.

## Calculating splittings

Splittings calculation aims to replicate the results from Figure 4 of the paper, so there are no parameters to pass:

```sh
$ python splittings.py
```

This will generate a plot named `splittings.pdf` in the same directory where the program was executed.
