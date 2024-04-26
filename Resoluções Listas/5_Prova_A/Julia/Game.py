import time;
from random import randint;
from os import system;

#Variáveis
sortedNumber = int(0);
selectedNumber = int(0);
numberChosen = int(0);
namePlayer = str('');
inputMenu = int(0);
numberAttempts = int(8);


#Explicação
print("\nEsse é o meu jogo da adivinhação!!");
print("\nAs regras são as seguintes:")
time.sleep(1);
print("Será gerado um número aleatório depois da dificuldade escolhida.");
print("O jogador terá 8 chances para acertar o número.");

print("\nCarregando...");
time.sleep(2);


print("\nDigite seu nome de jogador:");
namePlayer = str(input("Digite: \n"));


while(True):
    system('cls');

    print("\nMenu do jogo:");
    print("Digite 0 para jogar.");
    print("Digite 1 para desistir do jogo.");

    inputMenu = int(input("\nDigite: "));


    if(inputMenu == 0):
        print(f"\nEita! Vamos começar {namePlayer}!!");
        print(f"\nNúmero de tentativas: {numberAttempts} ");
        numberAttempts = numberAttempts - 1;
        input('\nAperte ENTER para continuar');

    if(inputMenu == 1):
        exit();

    else:
        break;

print(f"\nAgora irei mostrar os níveis de dificuldade para escolher {namePlayer}:");
time.sleep(1);
print("O modo fácil terá números de (1 a 40).");
print("O modo médio terá números de (1 a 80).");
print("O modo dificil terá números de (1 a 120).");
print("Digite 1 para modo fácil.");
print("Digite 2 para médio.");
print("Digite 3 para dificil.");

selectedNumber = int(input("\nDigite: "));
input('Aperte ENTER para continuar');
system('cls');

if(selectedNumber == 1):
    print(f"\nÉ {namePlayer}...Não deve ter tanta coragem para escolher o dificil hahaha. Mas vamos começar.");
    sortedNumber = randint (1 , 40)


if(selectedNumber == 2):
    print("\nEstá mediano...Vamos ver se é bom.");
    sortedNumber = randint (1 , 80);


if(selectedNumber == 3):
    print("\nOlha só, escolheu o nível mais dificil, vamos ver se é tão bom quanto acha!");
    sortedNumber = randint (1 , 120);


while(inputMenu == 0):

    numberChosen = int(input("Digite: "));
    print(f"\nNúmero de tentativas: {numberAttempts} ");
    numberAttempts = numberAttempts - 1;
    
    if(numberChosen == sortedNumber):
        print(f"Uau, parabéns {namePlayer}!! Você conseguiu ganhar o jogo.");
        exit();

    if(numberChosen != sortedNumber):
        print("Não foi dessa vez...");
    
    if(numberAttempts < 1):
        print("Suas chances acabaram...")
        print("GAME OVER.");
        