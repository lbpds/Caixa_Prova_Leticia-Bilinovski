def inicializa(continuar):
    
    quant_10 = int(input("Digite a quantidade de notas de R$10: "))     
    quant_20 = int(input("Digite a quantidade de notas de R$20: "))
    quant_50 = int(input("Digite a quantidade de notas de R$50: "))
    quant_100 = int(input("Digite a quantidade de notas de R$100: "))

    if quant_10 >= 0 and quant_20 >= 0 and quant_50 >= 0 and quant_100 >= 0:
        continuar = 1
    else:
        print("A quantidade não pode ser negativa")
            
    return quant_10, quant_20, quant_50, quant_100, continuar

def imprimir_saldo(saldo):
    print("Saldo atual: R$ {}".format(saldo))

def saque(saldo, quant_10, quant_20, quant_50, quant_100):
    
    saque = int(input("digite o valor que quer sacar: "))

    if saque > saldo or saque < 0:
        print("não se pode sacar esse valor")
        return saldo,quant_10, quant_20, quant_50, quant_100 
    if saque > (quant_10 * 10) + (quant_20 * 20) + (quant_50 * 50) + (quant_100 * 100):
        print("não tem dinheiro suficiente no caixa")
        return saldo,quant_10, quant_20, quant_50, quant_100   
    if saque % 10 != 0:
        print("Valor não pode ser sacado com as notas disponíveis.")
      
    celulas_100 = celulas_50 = celulas_20 = celulas_10 = 0

    
    saldo = saldo-saque 
    if saque >= 100 and quant_100 > 0:
        celulas_100 = saque // 100
        if celulas_100 > quant_100:
           celulas_100 = quant_100
        saque = saque - (celulas_100 * 100)
        quant_100 = quant_100 - celulas_100
    if saque>= 50 and quant_50 > 0:
        celulas_50 = saque // 50
        if celulas_50 > quant_50:
           celulas_50 = quant_50
        saque = saque - (celulas_50 * 50)
        quant_50 = quant_50 - celulas_50
    if saque >= 20 and quant_20 > 0:
        celulas_20 = saque // 20
        if celulas_20 > quant_20:
           celulas_20 = quant_20
        saque = saque - (celulas_20 * 20)
        quant_20 = quant_20 - celulas_20
    if saque >= 10 and quant_10 > 0:
        celulas_10 = saque // 10
        if celulas_10 > quant_10:
           celulas_10 = quant_10
        saque = saque - (celulas_10 * 10)
        quant_10 = quant_10 - celulas_10

    if saque > 0:
            print("Valor não pode ser sacado com as notas disponíveis.")
            return saldo + ((celulas_100 * 100) + (celulas_50 * 50) + (celulas_20 * 20) + (celulas_10 * 10) + saque), quant_10 + celulas_10, quant_20 + celulas_20, quant_50 + celulas_50, quant_100 + celulas_100
    
    print("A quantidade sacada é: R$ {} com:\n{} cédulas de 100\n{} cédulas de 50\n{} cédulas de 20\n{} cédulas de 10\nSeu saldo restante é: R$ {}".format(saque, celulas_100, celulas_50, celulas_20, celulas_10, saldo))
    return saldo, quant_10, quant_20, quant_50, quant_100

def deposito(saldo):
    deposito = int(input("digite o valor do deposito: "))
    while deposito <= 0:
        deposito = int(input("o deposito não pode ser não positivo: "))
    saldo = saldo + deposito

    print("Deposito realizado com sucesso\nO valor do saldo atual após o deposito: R${} é: R${}".format(deposito, saldo))
    return saldo

def sair():
    resp = input("Tem certeza que quer encerrar o atendimento? (SIM/NÃO): ").upper()
    if resp == "SIM" or resp == "S":
        exit()
    elif resp == "NÃO" or resp == "NAO" or resp == "N":
        return
    else:
        print("resposta invalida tente de novo")

saldo_total = 1000
nota_10 = nota_20 = nota_50 = nota_100 = 0
cont = 0

while True:
    print("\nEscolha uma opção:")
    escolha = input("+--------------------+\n1 - Inicializar notas\n2 - Ver saldo\n3 - Realizar saque\n4 - Realizar depósito\n5 - Sair\n+--------------------+\nOpção: ")
    if escolha == "1":
        nota_10, nota_20, nota_50, nota_100, cont = inicializa(cont)
    elif escolha == "2":
        imprimir_saldo(saldo_total)
    elif escolha == "3":
        if cont == 0:
            print("primeiro inicialize o caixa")
        else:
            saldo_total, nota_10, nota_20, nota_50, nota_100 = saque(saldo_total, nota_10, nota_20, nota_50, nota_100)
    elif escolha == "4":
        saldo_total = deposito(saldo_total)
    elif escolha == "5":
        sair()
    else:
        print("Opção inválida. Escolha novamente.")