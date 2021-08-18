print("--------------------------------")
print("Bem vindo ao jogo de Advinhação!")
print("--------------------------------")

import random
numero_secreto = random.randrange(1, 100)
print("Dica: o número secreto está entre", numero_secreto-random.randrange(1, 11) ,"e", numero_secreto+random.randrange(1, 11))
tentativas = 1

while(tentativas <= 3):
    chute = input("Chute um número:")
    numeroChutado = int(chute)
    if(numero_secreto == numeroChutado):
        print("Parabéns, você acertou!")
        break #<--- Usei a função "break" como parametro de quebra do loop#
    else:
        if(numeroChutado > numero_secreto):
            print("Sinto muito, você errou! Seu chute saiu mais alto")
        else:
            print("Sinto muito, você errou! Seu chute saiu mais baixo")
            print("Tentativa", tentativas ,"de 3")
            tentativas= tentativas + 1
print("O número secreto era", numero_secreto)
print("FIM DO JOGO!")
