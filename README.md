# AALprojekt
# Łukasz Wolanin
# lukaszwolanin98@gmail.com

# Pan K posiada prostokątny kawałek pola. Pan K chciałby ogrodzić możliwie największy kawałek swojej działki,
# niestety niektóre jego fragmenty pokryte są bagnami na których nie da budować się płotu. Twoim zadaniem jest
# znalezienie maksymalnej długości płotu który może odgrodzić prostokątny obszar pola.
# (lub podanie inforamacji że nie jest to możliwe)
# Przykładowo, dla poniższego pola o wielkości m * n na którym obszary bagienne zostały zaznaczone za pomocą x:
# ----
# --x-
# --x-
# x---
# Numerując wiersze i kolumny od 0 możemy zauważyć że do rozważenia są 2 główne obszary które można ogrodzić
# (0,0)-(1,2) oraz (1,0)-(3,3). Drugi - większy obszar ogrodzony będzie płotem o długości 10.
# Przykładowe rozwiązanie:
# Wejście: 4 5 (rozmiar pola) -----
# -x-x-
# -----
# -----
# Wyjście: 14