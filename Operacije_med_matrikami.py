
import random

def identiteta(n):
    matrika = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(1 if i == j else 0)
        matrika.append(vrstica)
    return matrika

def transponiraj(n):
    matrika = []
    for j in range(len(n[0])):
        vrstica = []
        for i in range(len(n)):
            vrstica.append(n[i][j])
        matrika.append(vrstica)
    return matrika

def ničelna_matrika(n):
    matrika = []
    for i in range(n):
        vrstica = []
        for j in range(n):
            vrstica.append(0)
        matrika.append(vrstica)
    return matrika

def sled_matrike(n):
    vsota = 0
    for i in range(len(n)):
               vsota += n[i][i]
    return vsota


def poljubna_matrika(vrstice, stolpci):
    matrika = []
    for i in range(vrstice):
        vrstica = []
        for j in range(stolpci):
            vrstica.append(random.randint(0, 99))
        matrika.append(vrstica)
    return matrika
                           
def vsota_matrik(a, b):
    matrika = []
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(len(a)):
            vrstica = []
            for j in range(len(a[i])):
                vrstica.append(a[i][j] + b[i][j])
            matrika.append(vrstica)
        return matrika
    else: return None
    

def razlika_matrik(a, b):
    matrika = []
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        for i in range(len(a)):
            vrstica = []
            for j in range(len(a[i])):
                vrstica.append(a[i][j] - b[i][j])
            matrika.append(vrstica)
        return matrika
    else: return None

def produkt_matrik(a, b):
    matrika = []
    if len(a[0]) == len(b):
        for i in range(len(a)):
            vrstica = []
            for j in range(len(b)):
                vsota = 0
                for k in range(len(a[i])):
                    vsota += a[i][k] * b[k][j]
                vrstica.append(vsota)
            matrika.append(vrstica)
    return matrika
