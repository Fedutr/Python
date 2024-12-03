primeiro_termo = int(input('Digite o primeiro termo da PA: '))
razao = int(input('Digite a razão da PA: '))
contador = 10
levantamento = 0
termo = 10
while termo > 0:

    while contador > 0:
        print(primeiro_termo, end=' ')
        primeiro_termo += razao
        contador -= 1
        levantamento += 1

    termo -= 1
    termo = int(input('\nVocê quer mostrar mais quantos termos? '))
    contador = termo
print(f'Processo finalizado com {levantamento} termos mostrados.')