# Entropy Calculator

---

## Contents
- <a href="#description">Description</a>
- <a href="#example">Example Values</a>
- <a href="#instructions">Usage Instructions</a>
- <a href="#credits">Authors and Copyright</a>

---

<section id="description">

## Description

We propose the following question. If we have `x` items and `n` spaces to place the items in, how many ways can we place the items in. For example, if we have 2 items and 3 spaces, the items can be arranged in 3 different ways:
```
1) 110
2) 101
3) 011
```
The formula that represents this can be written as `x:n = x-1:n-1 + x:n-1`

<section id="example">

## Example Values
In this example, we set `n = 8` and increment `x` from 0 to 8.
```
0:8 = 0.0
1:8 = 8.0
2:8 = 28.0
3:8 = 56.0
4:8 = 70.0
5:8 = 56.0
6:8 = 28.0
7:8 = 8.0
8:8 = 1.0
```

<section id="instructions">

## Instructions

1. Confirm that your terminal has Python 3.0 or later. This program was designed and tested in Python 3.8.9.
2. Clone this repository and navigate to it within your terminal.
3. Run the entropy calculator script with `python3 entropy-calc.py <n_max>`. Replace `<n_max>` with whatever value you want the maximum `n` value to be. Removing the argument defaults it to 998.
4. Follow the prompts in your terminal.

<section id="credits">

## Authors and Copyright

Team:
- Remington Tideman (Project Leader)
- James Swartwood (Python Developer)

_Copyright (c) James Swartwood, Remington Tideman. All rights reserved._