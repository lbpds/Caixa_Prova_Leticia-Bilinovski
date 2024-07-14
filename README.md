Escreva um programa que simule um caixa eletrônico de um banco com apenas 1 (um) cliente, cuja conta_corrente
tem saldo inicial seja R$1000,00. O programa deve ter uma interface de opções seguindo as funções:

Função inicializa(). Esta função faz a inicialização do caixa eletrônico com notas de R$10, R$20, R$50 e R$100,
onde a quantidade de cada uma é solicitada ao usuário. Você pode usar variáveis para armazenar estas quantidades.
A função deve verificar se alguma quantidade informada pelo usuário for negativa, e neste caso, encerrar a
execução do programa emitindo mensagem de erro apropriada.

Função saque(). Esta função realiza o saque de um valor da conta_corrente do cliente. Esta função recebe como
parâmetros: o saldo, o valor do saque e as quantidades de cédulas de cada valor disponíveis no caixa.
A função deve imprimir mensagens em cada caso: saque efetivado com sucesso caso a operação seja realizada com
sucesso, ou seja, cliente tem saldo e caixa tem notas disponíveis para o saque; ou saque inválido quando valor
solicitado for nulo ou negativo; saque indisponível quando o caixa não consegue um conjunto de cédulas para
compor o valor do saque; ou saldo insuficiente quando o cliente não tem saldo para o valor do saque; ou
valor indisponível quando o caixa não possui o valor disponível para saque. Esta função deve imprimir a
quantidade de cédulas de cada valor que serão entregues ao cliente caso o saque seja
realizado. A função deve calcular o menor número possível de cédulas para compor o valor do saque.
Realizado o saque com sucesso, a quantidade de cédulas de cada valor no caixa deve ser atualizada.

Função depósito(). Esta função faz a atualização do saldo da conta_corrente do cliente adicionando o valor do
depósito. A função deve imprimir mensagem de erro apropriada caso o valor de depósito seja negativo ou nulo, caso
contrário imprimir mensagem de depósito realizado com sucesso.

Função saldo(). Esta função imprime o saldo da conta do cliente.

Função sair(). Esta função simplesmente encerra a execução do programa.

O programa deve ter um menu inicial com as 5 opções de uso (inicializa, saque, depósito, saldo e sair).
Lembre-se de que a função saque deve calcular a menor quantidade de notas possível para cada saque. Por exemplo,
se o cliente pedir um saque de 130 reais, e o caixa tem todas as notas em boa quantidade, você não deve
entregar 13 notas de R$10, e sim uma de R$100, uma de R$20 e uma de R$10. Outro exemplo, considerando que o caixa
não tem mais notas de R$100, neste caso, deve entregar duas de R$50, uma de R$20 e uma de R$10.
