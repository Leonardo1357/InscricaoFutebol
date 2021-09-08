from Perguntas import ler


def inscricao():

    print('Bem vindo ao processo de inscrição, insira\nas seguintes informações:')

    aprovacao = None
    Nome = input('Insira seu nome: ')
    Altura = float(input('Insira a sua altura em m: '))
    Peso = float(input('Insira seu peso em kg: '))
    Idade = float(input('Insira a sua idade: '))
    Imc = round(Peso / (Altura * Altura))

    #Condiçã de aprovação
    if (Imc > 24.9):
        print('O seu imc está acima do requesitado, normalize-o e depois volte para\nrealizar novamente a inscrição.')
        aprovacao = False
    elif (Imc <= 24.9):
        treino_dias = int(input('Quantas vezes você treina por semana?'))
        minutos = float(input('Quantos minutos aproximadamente?'))

        total_treino = treino_dias * minutos

        if (total_treino <= 299):
            print('Obrigado pela participação!')
            aprovacao = False
        elif (total_treino >= 300):
            print('Parabéns, você passou em todos os nossos testes, agora você fará um teste'
                  '\npessoal em nossa sede, favor comparecer ao endereço: Rua dos Atletas, 43, '
                  '\nBairro do Futebol. Nos vemos lá!')
            aprovacao = True

    if (aprovacao == True):
        aprovado = 'Aprovado'
    elif (aprovacao == False):
        aprovado = 'Reprovado'

    #Escritura do arquivo
    frase1 = str(Nome)
    frase2 = str(Idade)
    frase3 = str(Imc)

    file = open('Inscrição.txt', 'a+')
    file.write('\n')
    file.write('Nome:'+frase1+'\n')
    file.write('Idade:'+frase2+'\n')
    file.write('Imc:'+frase3+'\n')
    file.write(aprovado)
    file.close()

#Inicio
def pergunta_inicial():
    inicio = int(input('Precione 1 para realizar o cadastro, 2 para verificar quem\nestá cadastrado e 3 para sair: '))

    if (inicio == 1):
        inscricao()
    elif (inicio == 2):
        ler()
        pergunta_inicial()
    elif (inicio == 3):
        print('Até mais!')
    else:
        print('Escolha entre 1 ou 2!')
        pergunta_inicial()


pergunta_inicial()