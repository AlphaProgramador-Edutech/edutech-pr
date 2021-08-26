print ('Especificacao    Codigo  Preco')
print ('Cachorro Quente  100     R$ 1,20')
print ('Bauru Simples    101     R$ 1,30')
print ('Bauru com Ovo    102     R$ 1,50')
print ('Hamburger        103     R$ 1,20')
print ('Cheeseburger     104     R$ 1,30')
print ('Refrigerante     105     R$ 1,00')
print ("")
print ("Quando terminar o seu pedido, tecle 0")

Codigo = -1
Qtde = 0
CQ = 0
BS = 0
BO = 0
HB = 0
CB = 0
RF = 0

while(Codigo != 0):
    Codigo = int(input("Qual o código do seu pedido? "))
    if(Codigo == 100):
        Qtde = int(input("Quantos cachorros quentes você vai querer? "))
        CQ = Qtde * 1.2

    elif(Codigo == 101):
        Qtde = int(input("Quantos baurus simples você vai querer? "))
        BS = Qtde * 1.3

    elif(Codigo == 102):
        Qtde = int(input("Quantos baurus com ovo você vai querer? "))
        BO = Qtde * 1.5

    elif(Codigo == 103):
        Qtde = int(input("Quantos hamburgers você vai querer? "))
        HB = Qtde * 1.2

    elif(Codigo == 104):
        Qtde = int(input("Quantos cheeseburgers você vai querer? "))
        CB = Qtde * 1.3

    elif(Codigo == 105):
        Qtde = int(input("Quantos refrigerantes você vai querer? "))
        RF = Qtde * 1

    Total = CQ + BS + BO + HB + CB + RF

print("O valor total do seu pedido será de R$", Total)