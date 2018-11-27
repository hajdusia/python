#!/usr/bin/python
# -*- coding: utf-8 -*-

# Problem drogi skoczka na kwadratowej szachownicy o boku N.
# Współrzędne planszy x i y mają zakres od 0 do N-1.

def rysuj(plansza):
    for i in range(N):
        for j in range(N):
            print "%2s" % plansza[i, j],
        print


def dopuszczalny(x, y):
    return 0 <= x < N and 0 <= y < N and plansza[x, y] == 0


def zapisz(plansza, krok, x, y):
    plansza[x, y] = krok  # zapis ruchu


def wymaz(plansza, x, y):
    plansza[x, y] = 0


def probuj(plansza, krok, x, y):
    # krok - nr kolejnego kroku do zrobienia
    # x, y - pozycja startowa skoczka
    # Funkcja zwraca bool True/False (czy udany ruch).
    udany = False
    kandydat = 0  # numery od 0 do RUCHY_SKOCZKA-1
    while (not udany) and (kandydat < RUCHY_SKOCZKA):
        u = x + delta_x[kandydat]  # wybieramy kandydata
        v = y + delta_y[kandydat]
        if dopuszczalny(u, v):
            zapisz(plansza, krok, u, v)
            if krok < N * N:  # warunek końca rekurencji
                udany = probuj(plansza, krok + 1, u, v)
                if not udany:
                    wymaz(plansza, u, v)
            else:
                udany = True
        kandydat += 1
    return udany


delta_x = [2, 1, -1, -2, -2, -1, 1, 2]  # różnica współrzędnej x
delta_y = [1, 2, 2, 1, -1, -2, -2, -1]  # różnica współrzędnej y
(x0, y0) = (0, 0)  # pole startowe skoczka

if __name__ == "__main__":
    N = 6  # bok szachownicy
    for x in range(0, N):
        for y in range(0, N):
            RUCHY_SKOCZKA = 8

            # Inicjalizacja pustej planszy.
            plansza = {}
            for i in range(N):
                for j in range(N):
                    plansza[i, j] = 0

            zapisz(plansza, 1, x, y)

            if probuj(plansza, 2, x, y):
                print x, y, "TAK"
                # print "Mamy rozwiązanie"
                # rysuj()
            else:
                print x, y, "NIE"
                # print "Nie istnieje rozwiązanie"


# Sprawdzenie czy istnieje rozwiązanie dla planszy o wymiarach 6 x 6 z pozycją startową skoczka X Y:

# X Y TAK/NIE
# 0 0 TAK
# 0 1 TAK
# 0 2 TAK
# 0 3 TAK
# 0 4 TAK
# 0 5 TAK
# ...