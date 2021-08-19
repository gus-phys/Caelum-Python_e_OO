
lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3,-52]

print('Seja a lista: ', lista)

# Declarando variávies
valor_max = lista[0]
valor_min = lista[0]
ocorrenciasItem1 = 0
pares = []
media = 0
soma_negativos = 0

# Iniciando o loop:
for idx in range(0, len(lista)):

    # Maior valor:
    if(valor_max < lista[idx]):
        valor_max = lista[idx]

    # Menor valor:
    if(valor_min > lista[idx]):
        valor_min = lista[idx]

    # Número de ocorrências:
    if(lista[idx] == lista[0]):
        ocorrenciasItem1 = ocorrenciasItem1 + 1

    # Números pares:
    if(lista[idx]%2==0):
        pares.append(lista[idx])

    # Soma dos números negativos:
    if(lista[idx]<0):
        soma_negativos = soma_negativos + lista[idx]

    # Média dos elementos:
    media =+ media + lista[idx]

media = media/len(lista)

# Impressão dos resultados:
print("Contém o maior valor", valor_max)
print('Contém o menor valor ', valor_min)
print('O primeiro ítem da lista ({}) aparece {} vezes'.format(
lista[0], ocorrenciasItem1))
print('Contém so seguintes valores pares: ', pares)
print('A média de seus elementos é dada por ', round(media, 2))
print('A soma de seus negativos é de: ', soma_negativos)
