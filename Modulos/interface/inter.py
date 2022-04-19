def leiaint():
    while True:
        try:
            n = int(input())
        except (ValueError, TypeError):
            print('Por favor, digite um número válido')
        else:
            return n
            
def linha(tam = 42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{c} - {item}')
        c += 1 
    print(linha())
    print('Sua opção: ', end='')
    opc = leiaint()
    return opc
   