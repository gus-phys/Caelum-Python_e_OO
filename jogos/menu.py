import adivinhacao
import forca
import adivinhacao_opcional

print('*********************************')
print('**********MENU DE JOGOS**********')
print('*********************************')
print("1. Adivinhação")
print("2. Forca")
print("3. Adivinhacão (nível)")
escolha = int(input("Qual jogo quer jogar? Digite o número: "))
if escolha == 1:
    adivinhacao.jogar()
elif escolha == 2:
    forca.jogar()
elif escolha == 3:
    adivinhacao_opcional.jogar()
