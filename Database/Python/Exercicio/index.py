import os;
import produtos;

inputMenu = int(0);

while( True ):
    os.system('cls');
    print('Menu de Seleção.');
    print('Digite 1 para criar um produto');
    print('Digite 2 para visualizar todos os produtos');
    print('Digite 3 para procurar');
    print('Digite 4 para atualizar');
    print('Digite 5 para excluir');
    print('Digite 0 para encerrar');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 0 ):
        break;


    input('Aperte ENTER para continuar.');