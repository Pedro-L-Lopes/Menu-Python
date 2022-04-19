from time import sleep
from modulos.dados.arquivo import lerArquivo, cadastrar
from modulos.dados.arquivo import criarArquivo
from modulos.dados.arquivo import arquivoExiste
from modulos.interface.inter import menu
from modulos.interface.inter import cabeçalho
from modulos.interface.inter import leiaint
arq = 'Cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    resposta = menu(['Ver pessoas cadastradas','Cadastrar nova pessoa', 'Sair do Sistema'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('NOME: '))
        print('IDADE: ', end='')
        idade = leiaint()
        cadastrar(arq, nome, idade)
    elif resposta == 3:
        sleep(1)
        cabeçalho('Saindo do sistema... Até logo!')
        break
    else:
        print('ERRO! Digite uma opção valida!')
    sleep(2)









#Crie um pequeno sistema modularizado 
#Cadastrar pessoas pelo seu nome/idade em um arquivo de texto simples
#O sistema so vai ter 2 opções: 
#Cadastrar um nova pessoa e listar todas as pessoas cadastradas
