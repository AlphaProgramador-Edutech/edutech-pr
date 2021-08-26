Salário_str = input("Qual é o seu salário? (sem arredondamentos) : ")
Salário = float(Salário_str)

if (Salário > 0 and Salário <= 280):
    valorAumento = (Salário * 0.2)
    salárioConvertido = Salário + valorAumento
    print("De acordo com o seu salário, o aumento será de 20%, portanto o acréscimo será de R${} e ele passará a ser de R${}".format(valorAumento, round(salárioConvertido, 2)))

elif (Salário > 280 and Salário <= 700):
    valorAumento = (Salário * 0.15)
    salárioConvertido = Salário + valorAumento
    print("De acordo com o seu salário, o aumento será de 15%, portanto o acréscimo será de R${} e ele passará a ser de R${}".format(valorAumento, round(salárioConvertido, 2)))

elif (Salário > 700 and Salário <= 1500):
    valorAumento = (Salário * 0.1)
    salárioConvertido = Salário + valorAumento
    print("De acordo com o seu salário, o aumento será de 10%, portanto o acréscimo será de R${} e ele passará a ser de R${}".format(valorAumento, round(salárioConvertido, 2)))

elif (Salário > 1500):
    valorAumento = (Salário * 0.05)
    salárioConvertido = Salário + valorAumento
    print("De acordo com o seu salário, o aumento será de 5%, portanto o acréscimo será de R${} e ele passará a ser de R${}".format(valorAumento, round(salárioConvertido, 2)))
