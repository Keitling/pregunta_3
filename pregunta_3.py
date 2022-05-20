# -*- coding: utf-8 -*-

"""
Spyder Editor

This is a temporary script file.
"""

from pyswip import Prolog
prolog = Prolog()

prolog.assertz("padre(juan,mario)")
prolog.assertz("padre(juan,julio)")
prolog.assertz("padre(mario,luis)")
prolog.assertz("padre(mario,nena)")
prolog.assertz("padre(julio,brenda)")
prolog.assertz("padre(julio,margarita)")

print ("RELACION DE TODOS LOS PADRES:")
for elemento in prolog.query("padre(X,Y)"):
    print (elemento["X"],"Es el padre de:", elemento ["Y"])
    
    #relacion de los abuelos
    print ("RELACION DE TODOS LOS ABUELOS:")
    for elemento in prolog.query("padre(X,Y),padre(Y,Z)"):
        print (elemento["X"],"Es el abuelo de:", elemento ["Z"])
 
       
    #relacion de los nietos
    print ("RELACION DE TODOS LOS NIETOS:")
    for elemento in prolog.query("padre(X,Y),padre(Y,Z)"):
        print (elemento["Z"],"Es el nieto de:", elemento ["X"])
        
    #relacion de primos
    print ("RELACION DE TODOS LOS PRIMOS:")
    for elemento in prolog.query("padre(X,Y),padre(A,B),padre(C,A),not(X==A)"):
        print (elemento["Y"],"Es el primo de:", elemento ["B"])    