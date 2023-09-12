animais = ['ELEFANTE','LEAO','BALEIA','POMBA','TIGRE','TUCANO','GIRAFA','ZEBRA','TUBARAO','HIPOPOTAMO','MACACO','GORILA','CACHORRO','GATO','PAPAGAIO','PEIXE']
frutas = ['LARANJA','BANANA','PERA','ABACAXI','MELANCIA','UVA','MELAO','MORANGO','GOIABA','AMORA','PITANGA','MARACUJA','KIWI','LIMAO','MELAO']
cores = ['AZUL','VERMELHO','AMARELO','VERDE','BRANCO','ROXO','MARROM','PRETO','CINZA','LARANJA','ROSA']
esportes = ['FUTEBOL','VOLEI','NATACAO','BASQUETE','GOLFE','TENIS','HANDBOL']


#escolher o grupo de palavras

import random

print('Olá!\nAbaixo estão as opções de grupos para o jogo, por favor escolha um!')
print('\n')
qual_opção = {1:"ANIMAIS", 2: "FRUTAS", 3:"CORES", 4:"ESPORTES"}
for lista, qual_opção in qual_opção.items():
    print(lista, qual_opção),

print("\n")

opcao_escolhida = input("Qual o grupo escolhido? 1, 2, 3 ou 4? ")

grupo = opcao_escolhida
if grupo == '1':
  print('O grupo escolhido foi o grupo 1 - Animais')
  escolhido = random.choice(animais)
elif grupo == '2':
  print('O grupo escolhido foi o grupo 2 - Frutas')
  escolhido = random.choice(frutas)
elif grupo == '3':
  print('O grupo escolhido foi o grupo 3 - Cores')
  escolhido = random.choice(cores)
else:
  print('O grupo escolhido foi o grupo 4 - Esportes')
  escolhido = random.choice(esportes)
print('\n')
print('Vamos começar o jogo!')


quantidade_de_letras = len(escolhido)

print('Quantidade de letras: ' , quantidade_de_letras)


print('\n')

comecar = escolhido

def jogar_forca(palavra):
    # Cria uma lista vazia para armazenar as letras adivinhadas
    letras_adivinhadas = []
    letras_erradas = []
    # Contador de tentativas
    tentativas = 6

    # Loop principal do jogo
    while True:
        # Exibe a palavra oculta com as letras adivinhadas
        palavra_oculta = ''
        for letra in escolhido:
            if letra in letras_adivinhadas:
                palavra_oculta += letra + ' '
            else:
                palavra_oculta += '_ '
        print(palavra_oculta)

        # Verifica se o jogador ganhou
        if '_' not in palavra_oculta:
            print('Parabéns! Você venceu!')
            break

        # Verifica se o jogador perdeu
        if tentativas == 0:
            print('Você perdeu! A palavra correta era:', escolhido)
            break

        # Solicita uma letra ao jogador
        letra_jogador = input('Digite uma letra: ').upper()

        # Verifica se a letra já foi adivinhada
        if letra_jogador in letras_adivinhadas:
            print('Você já tentou essa letra. Tente novamente!')
            continue

        # Adiciona a letra à lista de letras adivinhadas
        letras_adivinhadas.append(letra_jogador)

        # Verifica se a letra está na palavra
        if letra_jogador in escolhido:
            print('Letra correta!')
        else:
            tentativas -= 1
            letras_erradas.append(letra_jogador)
            print('Letra incorreta! Você tem mais', tentativas, 'tentativas.')
            print('Lista de letras erradas: ', letras_erradas)


jogar_forca(comecar)
