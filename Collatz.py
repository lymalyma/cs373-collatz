#!/usr/bin/env python3

# ---------------------------
# projects/collatz/Collatz.py
# Copyright (C) 2015
# Glenn P. Downing
# ---------------------------

# ------------
# collatz_read
# ------------

def collatz_read (s) :
    """
    read two ints
    s a string
    return a list of two ints, representing the beginning and end of a range, [i, j]
    """
    a = s.split()
    return [int(a[0]), int(a[1])]

# ------------
# collatz_eval
# ------------

def collatz_eval (i, j) :
    """
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    return the max cycle length of the range [i, j]
    """
    assert i > 0 and j > 0

    if i > j:
        i, j = j, i 

    max_cycle_length = 0
    for n in range(i, j + 1):
        cycle = collatz_cycle(n)
        if cycle > max_cycle_length:
            max_cycle_length = cycle

    return max_cycle_length

cache = {1: 1}

def collatz_cycle(n): 
    """
    n is a integer
    returns cycke length in 3n+1 
    """
    original_n = n
    cycle = 0

    while n not in cache and n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3*n + 1

        cycle += 1

    cache[original_n] = cycle + cache[n]

    return cache[original_n]  


    
# -------------
# collatz_print
# -------------

def collatz_print (w, i, j, v) :
    """
    print three ints
    w a writer
    i the beginning of the range, inclusive
    j the end       of the range, inclusive
    v the max cycle length
    """
    w.write(str(i) + " " + str(j) + " " + str(v) + "\n")

# -------------
# collatz_solve
# -------------

def collatz_solve (r, w) :
    """
    r a reader
    w a writer
    """
    for s in r :
        i, j = collatz_read(s)
        v    = collatz_eval(i, j)
        collatz_print(w, i, j, v)

