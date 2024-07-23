#Trabalho (prova2)     Prof. Luciano Silva     7/jul/2024

#função que inicializa o caixa
def inicializa(continuar):
    #Adquire a quantidade de cada nota no caixa
    quant_10 = int(input("Digite a quantidade de notas de R$10: "))     
    quant_20 = int(input("Digite a quantidade de notas de R$20: "))
    quant_50 = int(input("Digite a quantidade de notas de R$50: "))
    quant_100 = int(input("Digite a quantidade de notas de R$100: "))
    #Verifica se não ha nenhum valor negativo
    if quant_10 >= 0 and quant_20 >= 0 and quant_50 >= 0 and quant_100 >= 0:
        continuar = 1
    else:
        print("A quantidade não pode ser negativa")
            
    return quant_10, quant_20, quant_50, quant_100, continuar
#Função que mostra o saldo do cliente
def saldo(saldo):
    print("Saldo atual: R$ {}".format(saldo))
#Função saque
def saque(saldo, quant_10, quant_20, quant_50, quant_100):
    #Adquire o saque desejado
    saque = int(input("digite o valor que quer sacar: "))
    #Variavel reserva
    saque_total = saque
    #Verifica se é possivel sacar o valor solicitado
    if saque > saldo or saque < 0:
        print("não se pode sacar esse valor")
        return saldo,quant_10, quant_20, quant_50, quant_100 
    #Verifica se tem dinheiro suficiente no caixa
    if saque > (quant_10 * 10) + (quant_20 * 20) + (quant_50 * 50) + (quant_100 * 100):
        print("não tem dinheiro suficiente no caixa")
        return saldo,quant_10, quant_20, quant_50, quant_100   
    #Verifica se pode ser sacado com as notas disponiveis exemplo: não permite sacar 576 reais ou 8 reais ja que a menor nota possivel é 10 reais
    if saque % 10 != 0:
        print("Valor não pode ser sacado com as notas disponíveis.")
      
    celulas_100 = celulas_50 = celulas_20 = celulas_10 = 0

    #Atualiza o valor de saldo
    saldo = saldo-saque 
    #Verifica se é necessario utilizar a nota proposta fazendo a verificaçõ da maior para a menor
    if saque >= 100 and quant_100 > 0:
        celulas_100 = saque // 100 #Obtem a quantidade necessaria de celulas para saque
        if celulas_100 > quant_100:#Verifica se tem a quantidade ne notas necessarias no caixa
           celulas_100 = quant_100 #Se não há quantidade de notas suficiente no caixa então igualiza
        saque = saque - (celulas_100 * 100) #Diminui o valor do saque com o valor sacado
        quant_100 = quant_100 - celulas_100 #Diminui a quantidade utilizada de notas do caixa 
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

    if saque > 0: #Se mesmo após as operaçoes acima o saque for superior a zero , por exemplo: 1 nota de 100, 0 do resto das notas e valor de saque de 50 reais 
            print("Valor não pode ser sacado com as notas disponíveis.")
            saldo = saldo + saque_total
            return saldo, quant_10 + celulas_10, quant_20 + celulas_20, quant_50 + celulas_50, quant_100 + celulas_100 # puxa a variavel reserva 
            #Se tudo ocorrer bem informa qual valor sacado com quantas notas e o novo saldo
    print("A quantidade sacada é: {} com:\n{} cédulas de 100\n{} cédulas de 50\n{} cédulas de 20\n{} cédulas de 10\nSeu saldo restante é: R$ {}".format(saque_total, celulas_100, celulas_50, celulas_20, celulas_10, saldo))
    return saldo, quant_10, quant_20, quant_50, quant_100
#Função depósito
def depósito(saldo):
    deposito = int(input("digite o valor do deposito: "))
    #Verifica se o valor do depósito é maior que 0
    while deposito <= 0:
        deposito = int(input("o deposito não pode ser não positivo: "))
    #Adiciona o valor do deposifo ao saldo
    saldo = saldo + deposito
    print("Deposito realizado com sucesso\nO valor do saldo atual após o deposito: R${} é: R${}".format(deposito, saldo))
    return saldo
#Função sair 
def sair():
    #Tratas as exeções transfomando a resposta em maiusula
    resp = input("Tem certeza que quer encerrar o atendimento? (SIM/NÃO): ").upper()
    #Se a respota for positiva encerra o programa
    if resp == "SIM" or resp == "S":
        exit()
    #Se a resposta for negativa retorna ao programa original    
    elif resp == "NÃO" or resp == "NAO" or resp == "N":
        return
    else:
        print("resposta invalida tente de novo")

saldo_total = 1000 #Inicializa o programa com saldo de 1000 reais conforme solicitado jno trabalho
nota_10 = nota_20 = nota_50 = nota_100 = 0
cont = 0  # Condição que verifica se o inicializa ja foi feito , colocando como padrão não ou 0 
#Looping continuo 
while True:
    #Menu de escolha
    print("\nEscolha uma opção:")
    escolha = input("+--------------------+\n1 - Inicializar notas\n2 - Ver saldo\n3 - Realizar saque\n4 - Realizar depósito\n5 - Sair\n+--------------------+\nOpção: ")
    if escolha == "1":#Ao fazer esta escolha manda para a função inicializa e obtem a quantidade de notas
        nota_10, nota_20, nota_50, nota_100, cont = inicializa(cont)
    elif escolha == "2":#Ao fazer a escolha 2 puxa a função saldo
        saldo(saldo_total)
    elif escolha == "3":#Ao fazer a escolha 3 verifica se o caixa foi inicializado  se sim puxa a função saque 
        if cont == 0:
            print("primeiro inicialize o caixa")
        else:
            saldo_total, nota_10, nota_20, nota_50, nota_100 = saque(saldo_total, nota_10, nota_20, nota_50, nota_100)
    elif escolha == "4":#Ao fazer a escolha 4 chama a função depósito e atualiza o valor se saldo
        saldo_total = depósito(saldo_total)
    elif escolha == "5":#Ao fazer a esscolha 5 puxa a função sair 
        sair()
    else: #Tratamento de exeções
        print("Opção inválida. Escolha novamente.")