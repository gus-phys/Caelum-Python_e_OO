def jogar():
    print('***********************')
    print('* JOGO DA ADIVINHAÇÃO *')
    print('***********************')

    numero_secreto = 42
    total_de_tentativas = 3

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
          print('Você errou! O número inserido é maior que o número secreto.')
        elif(menor):
          print('Você errou! O número inserido é menor que o número secreto.')

    print('Fim do jogo')
