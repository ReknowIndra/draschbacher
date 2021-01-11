#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:34:42 2021

@author: irvine
"""

from random import *

fr = ["Wie","Wo","Wann","Was"]
verb1 = ["sehen","halten","stehen","prognostizieren"]
verb2 = ["es mit","zu","von"]
o1 = ["der Religion","dem Markt","der Innovation","den klügsten Köpfen"]
o3 = ["der Mitarbeiter","den Kunden","dem Wissen","eines Probeunternehmens"]
erg = ["ganz allgemein","im speziellen","heute","morgen","dieses Jahr"]

ant = ["ja","nein","ein bisschen","wahrscheinlich","relativ wenig","gar nicht"]

text = ""
sp = " "

Nsatz = 25

ran = lambda a : a[randint(0,len(a)-1)]

for n in range(Nsatz):
    b = randint(1,8)
    if b%3 == 0:
        frage = ran(fr) + sp + ran(verb1) + " Sie " + ran(o1)
    if b%3 == 1:
        frage = ran(fr) + sp + ran(verb1) + " Sie " + ran(verb2) + sp + ran(o1) + sp + ran(o3)
    if b%3 == 2:
        frage = ran(fr) + sp + ran(verb1) + " Sie " + ran(verb2) + sp + ran(o1) + sp + ran(o3) + sp + ran(erg)

    frage += "?\n"
    
    antwort = ""
    for a in ant:
        antwort += "o " + a + " (" + str(randint(0,3)) + " Punkte)" + "\n"
        if antwort.count("o") > 1 and randint(0,3) == 0:
            break

    text += frage + antwort + "\n"
        
print (text)