import unicodedata
import re

def normalizar_username(nombre):
    nfkd = unicodedata.normalize('NFD', nombre)
    sin_tildes = ''.join(([c for c in nfkd if not unicodedata.combining(c)]))

    sin_ene = sin_tildes.replace('ñ', 'n').replace('Ñ', 'N')

    limpio = re.sub(r'[^a-zA-Z0-9]', '', sin_ene)

    return limpio.lower()
