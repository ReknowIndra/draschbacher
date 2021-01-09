#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 14:34:42 2021

@author: irvine
"""

from random import *

verbs = ["sitz","schreibt","platziert","unterstützt"]
verbp = ["stehen","gehen"]
o1 = ["der Manager","ein Key-Account-Manager","die Innovation","die klügsten Köpfe"]
o3 = ["dem Mitarbeiter","den Kunden","dem Wissen","einem Probeunternehmen"]
o4 = ["die Zielvorgabe","der Struktur","den Leuten","ein allgemein gültiges Leistungsmodell"]
erg = ["im Rahmen der Dissertationsarbeit","gerade im Top-Management","zum Beispiel","dieses Jahr","heute","morgen"]
hs = ["ja,","das ist definitiv so,"]

text = ""
sp = " "

Nsatz = 1000

for n in range(Nsatz):
    b = randint(1,8)
    if b%3 == 0:
        satz = o1[randint(0,len(o1)-1)] + sp + verbs[randint(0,len(verbs)-1)] + sp + o3[randint(0,len(o3)-1)]
    if b%3 == 1:
        satz = o1[randint(0,len(o1)-1)] + sp + verbs[randint(0,len(verbs)-1)] + sp + o4[randint(0,len(o1)-1)]        
    if b%3 == 2:
        satz = erg[randint(0,len(erg)-1)] + sp + verbp[randint(0,len(verbp)-1)] + sp + o1[randint(0,len(o1)-1)] + sp + o3[randint(0,len(o1)-1)]
    if b == 1:
        satz = hs[randint(0,len(hs)-1)] + sp + satz
    satz = satz[0].upper() + satz[1:] + "."
    text = text + satz + sp
    if randint(0,20) == 0:
        text = text + "\n\n"
        
print (text)