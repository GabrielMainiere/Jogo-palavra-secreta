"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

print('Bem vindo ao jogo da adivinhação!')
palavra_secreta = "sofa"
letras_acertadas = ''
qtd_tentativas = 0
max_tentativas = 12

while True:
    letra = input('Digite uma letra: ')
    qtd_tentativas += 1

    if len(letra) > 1: #verificando se o usuário digitou apenas uma letra
        print('Digite apenas uma letra.')
        continue

    if letra in palavra_secreta:
        letras_acertadas += letra #verificando se a letra digitada está na palavra secreta
    
    palavra_formada = ''

    for verificacao in palavra_secreta:
        if verificacao in letras_acertadas: #percorrendo a palavra secreta e verificando em cada
            palavra_formada += verificacao  #posição existe alguma letra acertada pelo usuário
        else:
            palavra_formada += '*'

    print('Palavra formada: ',palavra_formada)#exibe a palavra formada a partir da concatenuação

    if palavra_formada == palavra_secreta:
        os.system('cls')
        print('Parabénss, você ganhou!!')
        print('A palavra era:', palavra_secreta)
        print('Total de tentativas para ganhar:',qtd_tentativas)
        break

    elif qtd_tentativas >= max_tentativas:
        os.system('cls')
        print('Você perdeu :(')
        print('A palavra era:', palavra_secreta)
        saida = input('Gostaria de tentar novamente? Se sim digite (sim): ')
        if saida.lower() == 'sim':
            qtd_tentativas = 0
            letras_acertadas = ''
            continue
        else:
            break