# Importações
import time;
from os import system;
from random import randint;

# Variáveis
inputMenu = int(0);
playerChoise = int(0);
computerChoise = int(0);
rounds = int(0);
playerName = str("Jogador");
computerName = str("Computador");

# Funções

def gameLogic( p1: int , p2:int , nameP1:str , nameP2:str):
    global rounds;
            
    if ( p1 == 1 and p2 == 2 ):
        print(f'{nameP1}: Pedra  //  {nameP2}: Papel');
        print(f'Vencedor: {nameP2}');
        rounds = rounds -1;
            
    if ( p1 == 1 and p2 == 3 ):
        print(f'{nameP1}: Pedra  //  {nameP2}: Tesoura');
        print(f'Vencedor: {nameP1}');
        rounds = rounds -1;
            
    if ( p1 == 2 and p2 == 3 ):
        print(f'{nameP1}: Papel  //  {nameP2}: Tesoura');
        print(f'Vencedor: {nameP2}');
        rounds = rounds -1;


# Explicação
print('Esse é o jogo Pedra - Papel - Tesoura (Jokenpô) !');
print('As regras são simples. Escolha entre pedra papel ou tesoura e vamos decidir o vencedor.');
print('Você jogará contra o computador. Serão 3 rodadas para decidir o vencedor.');

input('Aperte ENTER para Continuar . . .');

# Processamento

while (True):
    system('cls');
    print('Menu Inicial');
    print('Digite 1 para iniciar uma partida');
    print('Digite 0 para encerrar o jogo');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 0 ):
        break;

    if ( inputMenu == 1 ):
        rounds = 3;

        while ( rounds > 0 ):
            system('cls');
            print('Menu da Partida');
            print('O computador está escolhendo sua jogada . . .');
            print('Digite 1 para Pedra / 2 para Papel / 3 para Tesoura');

            playerChoise = int(input('Digite: '));

            computerChoise = randint(1 , 3);

            if ( playerChoise < 1 or playerChoise > 3 ):
                print('Escolha apenas números presentes no MENU.');
            
            if ( playerChoise == 1 and computerChoise == 1 ):
                print('Ambos escolheram Pedra. Foi um EMPATE');
    
            if ( playerChoise == 2 and computerChoise == 2 ):
                print('Ambos escolheram Papel. Foi um EMPATE');

            if ( playerChoise == 3 and computerChoise == 3 ):
                print('Ambos escolheram Tesoura. Foi um EMPATE');
            
            gameLogic(playerChoise , computerChoise, playerName, computerName);
            gameLogic(computerChoise , playerChoise , computerName, playerName);
            
    
            input('Aperte ENTER para Continuar . . .');