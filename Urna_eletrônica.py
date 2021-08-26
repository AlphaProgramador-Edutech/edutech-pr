print ('URNA ELETRONICA')
print("1 - João")
print("2 - José")
print("3 - Jaco")
print("4 - Jobe")
print("5 - Nulo")
print("6 - Branco")

Joao = 0
Jose = 0
Jaco = 0
Jobe = 0
Nulo = 0
Branco = 0
Voto = -1
# Quando o usuário digitar 0, a votação irá parar e serão exibidos os resultados
while (Voto != 0):
    Voto = int(input("Qual o número (de 1 a 6) do seu voto? : "))
    if(Voto == 1):
        print ('1 - Joao')
        Joao = Joao + 1

    elif(Voto == 2):
        print ('2 - Jose')
        Jose = Jose + 1

    elif(Voto == 3):
        print ('3 - Jaco')
        Jaco = Jaco + 1

    elif(Voto == 4):
        print ('4 - Jobe')
        Jobe = Jobe + 1

    elif(Voto == 5):
        print ('5 - Voto Nulo')
        Nulo = Nulo + 1

    elif(Voto == 6):
        print ('6 - Voto em Branco')
        Branco = Branco + 1

print("João fez {} voto/s, José fez {} voto/s, Jacó fez {} voto/s, Jobe fez {} voto/s. Teve {} voto/s nulo/s e {} voto/s em branco.".format(Joao, Jose, Jaco, Jobe, Nulo, Branco))
