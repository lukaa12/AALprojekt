# AALprojekt
# Łukasz Wolanin
# lukaszwolanin98@gmail.com

Usage: -m1 
or -m2 -n{width}x{height} -d{density}
or -m3 -n{start size} -k{tests quantity} -step{step} -r{repeats for one size}

 Pan K posiada prostokątny kawałek pola. Pan K chciałby ogrodzić możliwie największy kawałek swojej działki,
 niestety niektóre jego fragmenty pokryte są bagnami na których nie da budować się płotu. Twoim zadaniem jest
 znalezienie maksymalnej długości płotu który może odgrodzić prostokątny obszar pola.
 (lub podanie inforamacji że nie jest to możliwe).

 Dla poniższego pola o wielkości m * n na którym obszary bagienne zostały zaznaczone za pomocą x:
 ----
 --x-
 --x-
 x---
 Numerując wiersze i kolumny od 0 możemy zauważyć że do rozważenia są 2 główne obszary które można ogrodzić
 (0,0)-(1,2) oraz (1,0)-(3,3). Drugi - większy obszar ogrodzony będzie płotem o długości 10.
 Rozwiązanie:
 Wejście: 4 5 (rozmiar pola) -----
 -x-x-
 -----
 -----
 Wyjście: 14
 
 Algorytm optymalny

    Działanie algorytmu jest następujące. Dla każdego wiersza zaczynając od dołu przechodzi przez niego i odpowiednio
    dla każdego elementu wpisuje numer grupy do której należy. Grupy są ciągami pól wolnych, które zcynają się w
    pierwszej kolumnie wiersza lub po wystąpieniu bagna, a kończą na ostatniej kolumnie lub przed wystąpieniem bagna.
    Dla przykładu następujący wiersz [--X---XX--X] zostanie pogrupowany: [11_222__33_]
    Następnie dla wszystkich wierszy położonych wyżej od obecnie rozpatrywanego zostaną w kolumnach zorpropagowane
    wartości grup według wzoru, że jeśli punkt wiersz niżej rozpatrywanego punktu (który nie jest zajęty) należy
    do danej grupy to punkt rozpatrywany też do niej należy Na koniec musimy tylko jeszcze raz przejść po wierszach i
     sprawdzić czy są tam możliwości stworzenia ogrodzenia np. [11___1X_1_X22] mamy dwa możliwe ogrodzenia: jedno o
     szerokości 6 z grupy 1 i drugie o szerokości 2 z grupy 2. Tak otrzymamy wszystkie możliwe ogrodzenia, musimy tylko
     zapamiętać i zwrócić to najlepsze.
 
 
 Pliki:
 brutal.py
 fence.py
 function.py
 main.py
 generator.py
 loadTab.py
 
 Packages:
cycler==0.10.0
kiwisolver==1.1.0
matplotlib==3.1.2
numpy==1.17.3
pip==19.0.3
pyparsing==2.4.6
python-dateutil==2.8.1
setuptools==40.8.0
six==1.13.0
virtualenv==16.7.6
