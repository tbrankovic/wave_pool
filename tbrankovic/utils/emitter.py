from math import *
from numpy import *
from scipy import *

def emitter(message, surechantillonnage, formant):
    # Le signal est égal au message convolué avec le formant. Cependant,
    # il faut au préalable ajuster le message :
    # - le formant doit être muliplié par -1 ou +1 (et non 0 ou 1)
    # - la fréquence d'échantillonnage doit être la même.
    #
    # Ajustement des valeurs :
    message = 2 * message - 1
    n = size(message)
    # Fréquence d'échantillonnage : on commence par créer un vecteur
    # contenant des 0 partout avec la bonne taille.
    signal = zeros(surechantillonnage * (n - 1) + 1)
    # Puis on remplace les éléments à la bonne position par
    # les valeurs du signal d'origine.
    signal[::surechantillonnage] = message

    # Pour finit, il suffit de convoluer ce signal avec le formant :
    signal = convolve(signal, formant)
    taille_formant = size(formant)

    # Cette fonction renvoie un triplet contenant le signal, 
    # la position de l'origine et le coefficient de surechantillonnage.    
    return (signal, (taille_formant - 1) / 2, surechantillonnage)
