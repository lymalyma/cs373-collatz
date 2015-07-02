#!/usr/bin/env python3

# -------------------------------
# projects/collatz/TestCollatz.py
# Copyright (C) 2015
# Glenn P. Downing
# -------------------------------

# https://docs.python.org/3.4/reference/simple_stmts.html#grammar-token-assert_stmt

# -------
# imports
# -------

from io       import StringIO
from unittest import main, TestCase

from Collatz import collatz_read, collatz_eval, collatz_print, collatz_solve

# -----------
# TestCollatz
# -----------

class TestCollatz (TestCase) :
    # ----
    # read
    # ----

    def test_read (self) :
        s    = "1 10\n"
        i, j = collatz_read(s)
        self.assertEqual(i,  1)
        self.assertEqual(j, 10)

        st = "100 200\n"
        i, j = collatz_read(st)
        self.assertEqual(i, 100)
        self.assertEqual(j, 200)

    def test_read_empty(self):
        s = ""
        self.assertRaises(IndexError, collatz_read, s)

    def test_read_negative_integers(self):
        s = "-1 -2"
        i, j = collatz_read(s)
        self.assertEqual(i, -1)
        self.assertEqual(j, -2)

    def test_read_two_integers(self):
        s = " 1 2 3 4 "
        i, j = collatz_read(s)
        self.assertEqual(i, 1)
        self.assertEqual(j, 2)

    def test_read_one_integer(self):
        s = "1"
        self.assertRaises(IndexError, collatz_read, s)
    # ----
    # eval
    # ----

    def test_eval_1 (self) :
        v = collatz_eval(1, 10)
        self.assertEqual(v, 20)

    def test_eval_2 (self) :
        v = collatz_eval(100, 200)
        self.assertEqual(v, 125)

    def test_eval_3 (self) :
        v = collatz_eval(201, 210)
        self.assertEqual(v, 89)

    def test_eval_4 (self) :
        v = collatz_eval(900, 1000)
        self.assertEqual(v, 174)

    def test_eval_reverse_range(self):
        self.assertRaises(AssertionError, collatz_eval, 10, 1)  

    def test_eval_negative_integer(self):
        self.assertRaises(AssertionError, collatz_eval, -1, -2)
        self.assertRaises(AssertionError, collatz_eval, 1, -2)
        self.assertRaises(AssertionError, collatz_eval, -1, 2)

    def test_eval_same_integer(self):
        v = collatz_eval(1, 1)
        self.assertEqual(v, 1)
        v = collatz_eval(2, 2)
        self.assertEqual(v, 2)
        v = collatz_eval(4, 4)
        self.assertEqual(v, 3)
        v = collatz_eval(5, 5)
        self.assertEqual(v, 6)

                

    # -----
    # print
    # -----

    def test_print (self) :
        w = StringIO()
        collatz_print(w, 1, 10, 20)
        self.assertEqual(w.getvalue(), "1 10 20\n")   

    # -----
    # solve
    # -----

    def test_solve (self) :
        r = StringIO("1 10\n100 200\n201 210\n900 1000\n")
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "1 10 20\n100 200 125\n201 210 89\n900 1000 174\n")

    def test_solve_empty(self):
        r = StringIO()
        w = StringIO()
        collatz_solve(r, w)
        self.assertEqual(w.getvalue(), "")

    def test_solve_null(self):
        r = None
        w = None 
        self.assertRaises(TypeError, collatz_solve, r, w)


# ----
# main
# ----

if __name__ == "__main__" :
    main()

"""
% coverage3 run --branch TestCollatz.py >  TestCollatz.out 2>&1
% coverage3 report -m                   >> TestCollatz.out
% cat TestCollatz.out
.......
----------------------------------------------------------------------
Ran 7 tests in 0.001s
OK
Name          Stmts   Miss Branch BrMiss  Cover   Missing
---------------------------------------------------------
Collatz          18      0      6      0   100%
TestCollatz      33      1      2      1    94%   79
---------------------------------------------------------
TOTAL            51      1      8      1    97%
"""