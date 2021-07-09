print('***********************')
print('* JOGO DA ADIVINHAÇÃO *')
print('***********************')

numero_secreto = 42
total_de_pontos = 1000

nivel = int(input('Escolha o nível de dificuldade de 1 a 3: '))
if(nivel==1):
    total_de_tentativas = 20
    print('Nível {} escolhido, você tem {} tentativas.'.format(nivel,
     total_de_tentativas))
elif(nivel==2):
    total_de_tentativas = 10
    print('Nível {} escolhido, você tem {} tentativas.'.format(nivel,
     total_de_tentativas))
elif(nivel==3):
    total_de_tentativas = 5
    print('Nível {} escolhido, você tem {} tentativas.'.format(nivel,
     total_de_tentativas))

for rodada in range(1, total_de_tentativas + 1):
    print('Tentativa {} de {}'.format(rodada, total_de_tentativas))

    chute = int(input('Digite o seu palpite: '))
    print('Seu palpite é: ', chute)

    acertou = chute == numero_secreto
    maior = chute > numero_secreto
    menor = chute < numero_secreto


    if(acertou):
        print('Você acertou!')
        break
    elif(maior):
        diferenca = chute - numero_secreto
        total_de_pontos = total_de_pontos - diferenca
        print('Você errou! O número inserido é maior que o número secreto.')
    elif(menor):
        diferenca = numero_secreto - chute
        total_de_pontos = total_de_pontos - diferenca
        print('Você errou! O número inserido é menor que o número secreto.')

print('Fim do jogo!!!\nSua pontuação foi de {} pontos'.format(
total_de_pontos))
