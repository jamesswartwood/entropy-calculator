''' Copyright (c) James Swartwood, Remington Tideman. All rights reserved. '''

# Calculates x:n where x:n equals the number of ways x number of
# objects can be distributed amongst n number of spaces.
# Core equation -> x:n = x-1:n-1 + x:n-1

import sys
import numpy as np

def x_n(x, n, n_max):
    if x >= n+1:
        return table[n-x][n_max-n]

    if x == 0:
        table[x][n] = 1
        return table[x][n]
    elif x == 1:
        table[x][n] = n
        return table[x][n]
    elif n == 0:
        table[x][n] = 1
        return table[x][n]
    elif n == 1:
        table[x][n] = 0
        return table[x][n]
    else:
        if table[x-1][n-1] == 0:
            table[x-1][n-1] = x_n(x-1, n-1, n_max)
        if table[x][n-1] == 0:
            table[x][n-1] = x_n(x, n-1, n_max)
        return table[x-1][n-1] + table[x][n-1]

if __name__ == "__main__":
    print("PROGRAM START\n")

    n_max = 998
    try:
        if len(sys.argv) == 2:
            n_max = int(sys.argv[1])
    except:
        print("WARNING: <n_max> is not a valid integer")

    print("INFO: Table populating...")
    table = np.zeros((n_max+1, n_max+1))
    for x in range(n_max + 1):
        x_n(x, n_max, n_max)
    print("INFO: Complete\n")

    print("Enter a negative number to end the program.")
    print("Entering a number greater than", n_max, "will also end the program.\n")

    while(1):
        try:
            x = int(input("Enter x value: "))
            if x < 0 or x > n_max:
                break
            n = int(input("Enter n value: "))
            if n < 0 or x > n_max:
                break
        except:
            print("WARNING: Input is not a valid integer\n")
            continue
        print(x, ":", n, " = ", x_n(x, n, n), "\n")

    print("\nPROGRAM EXIT")
    exit()