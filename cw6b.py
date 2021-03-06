# -*- coding: utf-8 -*-
#importujemy potrzebne moduły i klasy
import numpy as np
import pylab as py
from svm_modul import *
 
#==================================================================
#                 Program
#==================================================================
 
# wczytywanie danych
dane = np.loadtxt('Dane2.txt') # dane zorganizowane są w trzech kolumnach
N_przyk, N_wej = dane.shape 
X = dane[:,0:2] # pierwsze dwie kolumny to wejście
y = dane[:,2] # trzecia kolumna to etykiety klas
 
# narysujmy te dane
rysujDaneGrup(X, y, marker=('or','xb'), xlabel='x0', ylabel='x1',legend_list=('klasa0','klasa1'))
py.show()
 

# trenujemy model
#sigma = [0.1,0.2,0.4,0.8,1,2,4,8]

model  = svmTrain(X, y, C=60, kernelFunction = 'gaussianKernel', tol = 1e-3, max_passes = 20, sigma=0.1) 
py.title('Gaussian')
# prezentujemy podział przestrzeni wejść reprezentowany przez model
rysujDaneGrup(X, y, marker=('or','xb'), xlabel='x0', ylabel='x1',legend_list=('klasa0','klasa1'))
rysujPodzial(model,X)
    
py.show()