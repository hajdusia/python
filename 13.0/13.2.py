#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem ośmiu hetmanów.
# Znajdowanie wielu rozwiązań.
# Wiersze i kolumny mają zakres od 0 do N-1.


def rysuj():
    for w in range(N):
        for k in range(N):
            if x[k] == w:
                print "H",
            else:
                print ".",
        print
    print


def dopuszczalny(w, k):
    return a[w] and b[w + k] and c[w - k]


def zapisz(w, k):
    x[k] = w
    a[w] = False
    b[w + k] = False
    c[w - k] = False


def wymaz(w, k):
    a[w] = True
    b[w + k] = True
    c[w - k] = True


def probuj(k):
    # Sprawdzanie wszystkich kandydatow (wiersze).
    for w in range(N):
        if dopuszczalny(w, k):
            zapisz(w, k)
            if k < (N - 1):
                probuj(k + 1)
            else:
                rysuj()
            wymaz(w, k)


N = 6   # bok szachownicy i jednocześnie liczba hetmanów

# x[i] to pozycja hetmana w kolumnie i
x = N * [None]

# a[j] == True to brak hetmana w wierszu j
a = N * [True]

# b[k] == True to brak hetmana na przekątnej k [/].
# Suma wiersz+kolumna od 0 do (2N-2).
b = (2 * N - 1) * [True]

# c[k] == True to brak hetmana na przekątnej k [\].
# Różnica wiersz-kolumna od (-N+1) do (N-1).
c = (2 * N - 1) * [True]

probuj(0)


# 1 rozwiązanie dla N = 1


# 0 rozwiązań dla N = 2, 3


# 2 rozwiązania dla N = 4
# . . H .
# H . . .
# . . . H
# . H . .
#
# . H . .
# . . . H
# H . . .
# . . H .


# 10 rozwiązań dla N = 5
# H . . . .
# . . . H .
# . H . . .
# . . . . H
# . . H . .
#
# H . . . .
# . . H . .
# . . . . H
# . H . . .
# . . . H .
#
# . . H . .
# H . . . .
# . . . H .
# . H . . .
# . . . . H
#
# . . . H .
# H . . . .
# . . H . .
# . . . . H
# . H . . .
#
# . H . . .
# . . . H .
# H . . . .
# . . H . .
# . . . . H
#
# . . . . H
# . . H . .
# H . . . .
# . . . H .
# . H . . .
#
# . H . . .
# . . . . H
# . . H . .
# H . . . .
# . . . H .
#
# . . . . H
# . H . . .
# . . . H .
# H . . . .
# . . H . .
#
# . . . H .
# . H . . .
# . . . . H
# . . H . .
# H . . . .
#
# . . H . .
# . . . . H
# . H . . .
# . . . H .
# H . . . .


# 4 rozwiązania dla N = 6
# . . . H . .
# H . . . . .
# . . . . H .
# . H . . . .
# . . . . . H
# . . H . . .
#
# . . . . H .
# . . H . . .
# H . . . . .
# . . . . . H
# . . . H . .
# . H . . . .
#
# . H . . . .
# . . . H . .
# . . . . . H
# H . . . . .
# . . H . . .
# . . . . H .
#
# . . H . . .
# . . . . . H
# . H . . . .
# . . . . H .
# H . . . . .
# . . . H . .
