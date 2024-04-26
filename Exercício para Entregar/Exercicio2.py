from os import system;

from Temperaturas import celsiusToFahrenheit , fahrenheitToCelsius;
from Medidas import metrosToPes , PesToMetros ;
from Distancias import kmToMiles , milesToKm;


inputMenu = int(-1);
value = float(0);


while (inputMenu != 0):
    system('cls');

    print('Menu de conversões.\n');

    print('Digite 1 para converter temperaturas.');
    print('Digite 2 para converter medidas.');
    print('Digite 3 para converter distâncias.');
    print('Digite 0 para encerrar a aplicação.');

    inputMenu = int(input('Digite: '));

    system('cls');

    if ( inputMenu == 1 ):
        print('\nMenu para conversões de Temperaturas.');
        print('Digite 1 para converter °C para °F.');
        print('Digite 2 para converter °F para °C.');
    
        inputMenu = int(input('Digite: '));

        if ( inputMenu == 1 ):
            print('\nVamos converter a temperatura digitada em °C para °F.');
            value = float(input('Digite: '));
            celsiusToFahrenheit(value);
    
        if ( inputMenu == 2 ):
            print('\nVamos converter a temperatura digitada em °F para °C.');
            value = float(input('Digite: '));
            fahrenheitToCelsius(value);
    
        inputMenu = -1;


    if ( inputMenu == 2 ):
        print('\nVamos converter o valor digitado em Metros para Pés.');
        value = float(input('Digite: '));
    
        metrosToPes(value);

    if ( inputMenu == 3 ):
        print('\nVamos converter o valor digitado em KM para Milhas.');
        value = float(input('Digite: '));
    
        kmToMiles(value);

    if ( inputMenu == 0 ):
        print('Encerrando. . .');
        exit();

    input("\nDigite ENTER para continuar. . .");
