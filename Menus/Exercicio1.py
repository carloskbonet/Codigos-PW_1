import os;

# Contador e limite da repetição da tabuada
limit = int(10);
# Variáveis para calcular a tabuada
value = int(0);
result = int(0);
# Variáveis do Menu de seleção
inputMenu = int(1);

print('O algoritmo fará a tabuada do número digitado.');

while ( inputMenu != 0 ):
    print("\nMenu de seleção !!\n");
    print("Digite 1 para calcular a tabuada.");
    print("Digite 2 para alterar as regras da tabuada.");
    print("Digite 0 para encerrar a operação.");

    inputMenu = int(input("Digite: "));

    if ( inputMenu == 1 ):
        print("\nVamos calcular a tabuada...");
        value = int(input("Digite um número: "));
    
        # Processamento
        for counter in range( 1 , limit + 1 , 1 ):
            result = value * counter;
            print(f'{value} x {counter} = {result}');

    if ( inputMenu == 2 ):
        print("\nA tabuada por padrão calcula de 1 até 10.")
        print(f'Atualmente, ela está calculando de 1 até {limit}');
        limit = int(input("Digite um novo limite para a tabuada: "));

    if ( inputMenu == 0 ):
        print("Encerrando...");
        exit();


    input('\nDigite ENTER para continuar...');
    os.system('cls');


