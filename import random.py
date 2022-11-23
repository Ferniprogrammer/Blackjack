from random import choice, sample
baraja = { 
    chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10, 
} 
print("Cartas: {}".format(" ".join(baraja.keys())))
print("Puntos: {}".format(list(baraja.values())))

print("1\ Iteración estándar sobre un diccionario")
for carta, valor in baraja.items():
    print("la carta {} vale {}".format(carta, valor))

print("2\ Iteración ordenada sobre un diccionario")
for carta in sorted(baraja.keys()):
    print("la carta {} vale {}".format(carta, baraja[carta]))

print("3\ Black Jack")
lista_cartas = list(baraja)

main_banca = sample(lista_cartas, 2)
score_banca = sum(baraja[carta] for carta in main_banca)
print("La banca tiene: {} {}  >> su score es {}".format(main_banca[0],
                                                          main_banca[1],
                                                          score_banca))
print("Ha seleccionado:", end=" ")
carta = choice(lista_cartas)
score = baraja[carta]
print(carta, end=" ")
carta = choice(lista_cartas)
score += baraja[carta]
print(carta, end=" ")
print(" >>> su puntuación es de", score)



