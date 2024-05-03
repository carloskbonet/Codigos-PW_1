codes = [ 104 , 111 , 91 , 55 , 192 , 491 , 22 , 40 ];
inputNumber = int(0);
check = bool(False);

print('Algoritmo da Loja de Peças.');
print('Digite um código para verificar se a peça está disponível.');

while (True):
    try:
        inputNumber = int(input('Digite: '));
        break;

    except:
        print('Digite apenas números inteiros.');

# Processamento

for i in range(0 , len(codes)):
    if ( inputNumber == codes[i] ):
        check = True;
        break;
    else:
        check = False;

# Saída de Dados

if (check == True):
    print('\nPeça encontrada.');
else:
    print('\nA peça NÃO foi encontrada.');