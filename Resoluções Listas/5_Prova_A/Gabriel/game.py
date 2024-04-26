import  time ;
import random ;
from os import system ;

jogador_1 = int(0);
jogador_2 = int(0);
jogador_3 = int(0);
sortedNumber = int (0);
selecteNumber = int(0);
menudojogador = int(0);

print("O nivel fácil você pode escolher de 1 a 30");
print("O nivel médio você  pode escolher de 1 a 60");
print("O nivel dificil você pode escolher de 1 a 90");
print("Cada jogador terá 5 dicas em cada partida");
print("Você tem 4 tentativas para acertar. Se ultrapassar de 4 tentativas vai ser gamer over");


print("quero ver alguém ganhar o jogo");

print("/nDigite 1 nivel fácil");
print("/nDigite 2 nivel médio");
print("/nDigite 3 nivel dificil");

selecteNumber = int (input('Digite o nivel que você vai jogar'));

sortedNumber = random.randint(1 , selecteNumber * 30);


while(True > 0 ):
    system('cls');

    print('Digite 1 receberá 1 dica');
    print('Digite 2 para adivinhar ');
    print('Digite 3 desistir da partida');

    menudojogador = int(input("digite"));

    if( menudojogador > 3 ):
        print("3 desista seu cacão");
        exit();