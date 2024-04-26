# Importações
import time;
import random;
import os;

# Variáveis

inputDif = int(0);
sortedNumber = int(0);
numberOfTries = int(4);
numberOfTips = int(2);
inputMenu = int(0);
inputTry = int(0);
inputTip = int(0);

# Print Explicativo

print("Esse é o Jogo de Adivinhação !!");
print("Para jogar, temos algumas regras.");
print("Primeiro: Um número aleatório será gerado a partir da dificuldade selecionada.");
print("Segundo: O jogador receberá até 5 dicas em cada partida.");
print("Terceiro: O jogador terá 4 tentativas de adivinhar o número.");
print("\n");

time.sleep(1);
print("Começando...\n");
time.sleep(1);

print("Agora vamos para a seleção de dificuldade !")
print("O modo fácil apresenta números entre (1 e 30).");
print('O modo médio apresenta números entre (1 e 60).');
print('O modo dificil apresenta números entre (1 e 90).');

# Seleção de Dificuldade

while (inputDif < 1 or inputDif > 3):
    print("Selecione a dificuldade.");
    print("Digite 1 para fácil.");
    print("Digite 2 para médio.");
    print("Digite 3 para dificil.\n");

    inputDif = int(input('Digite: '));

    if (inputDif < 1 or inputDif > 3):
        print('\nDigite apenas números presentes no menu.\n');

# Gameplay

while(True):
    print('\nMenu do Jogo.');
    print('Digite 1 para iniciar uma partida.');
    print('Digite 2 para sair do jogo.');

    inputMenu = int(input('Digite: '));

    if ( inputMenu == 2 ):
        print('\nFechando o jogo . . .');
        exit();

    if ( inputMenu == 1 ):
        numberOfTries = 4;
        numberOfTips = 2;

        if ( inputDif == 1 ):
            sortedNumber = random.randint(1 , 30);
        if ( inputDif == 2 ):
            sortedNumber = random.randint(1 , 60);
        if ( inputDif == 3 ):
            sortedNumber = random.randint(1 , 90);

        while(True):
            os.system('cls');

            print(f'Número de tentativas restantes: {numberOfTries} / Número de dicas restantes: {numberOfTips}');

            print("\nVamos tentar adivinhar o número? Boa sorte !! Digite sua tentativa abaixo.");
            print("Digite 0 para desistir da partida atual.\n");

            inputTry = int(input('Digite: '));
            
            if ( numberOfTries > 0 ):
            
                if ( inputTry == sortedNumber ):
                    print("\nUau, eu não estava esperando por essa!! HAHAHA você realmente acertou!!!!!!! Meus parabéns Vencedor.");
                    break;
                else:
                    print("Buuuuuuh não foi dessa vez !!!");
                    numberOfTries = numberOfTries - 1;
            
                if (numberOfTries <= 0):
                    print('\nGAME OVER.\n');
                    break;

                if ( numberOfTips > 0 ):
                    inputTip = str(input('Você quer uma dica? (y/n): '));
                
                    if ( inputTip == 'y' or inputTip == 'Y' ):
                        print('Tá precisando de dica então né? não se garante hahaha vou verificar.\n');
                        numberOfTips = numberOfTips - 1;
                    
                        if ( inputTry < sortedNumber and (inputTry + 5) > sortedNumber ):
                            print('Ta muuuito quente, tenta um número maior');
                        elif ( inputTry < sortedNumber and (inputTry + 10) > sortedNumber ):
                            print('Ta friozinho, tenta um número maior');
                        elif ( inputTry > sortedNumber and (inputTry - 5) < sortedNumber ):
                            print('Ta muuuito quente, tenta um número menor');
                        elif ( inputTry > sortedNumber and (inputTry - 10) < sortedNumber ):
                            print('Ta friozinho, tenta um número menor');
                        else:
                            print('Ta muuuuuuito longe, nem vou te ajudar');

                    else:
                        print('Caramba, tá confiante em filho !! Boa sorte então.');
            
            if ( inputTry == 0 ):
                print("Uma pena !! Espero que tenha coragem para tentar novamente.");
                break;


            input('\nAperte ENTER para continuar . . . ');
