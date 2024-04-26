#imports
from time import sleep; from os import system;
from random import randint; 
#variavies
setenumber = int(0); 
varnumber1 = int(0); 
varnumber2 = int(0); 
varnumber3 = int(0); 
mainmenu = int(0);
tries = int(4);  


#explicação
system("cls"); 
sleep(1); 
print("Olá seja bem vindo ao teste!\nVamos ver o quanto você tem sorte hoje hahaahah!");
print("Esse e um jogo muito fácil, só adivinhar qual número que eu sortear e você ganha!"); 
print("('hahaha Até mesmo o tolo mais sabio consegue esse jogo')"); 
input("Aperte ENTER para ir ao menu do jogo!..."); 
sleep(1); 
system("cls"); 

#menu de apresentção
print("Você pode escolher entre 3 dificuldades!('Atenção escolha com sabedoria!')");
print("Você tem 4 tentativa LEMBRE-SE disso quanto estiver jogando!") 
print("nivel 1, eu vou sortear um número de 1 a 30. ('bebe da mamãe')"); 
print("nivel 2, eu vou sortear um numero de 1 a 60. ('você ta querendo um divirsão?!')"); 
print("nivel 3, eu vou sortear um número de 1 a 90. ('Olha só quem tá querendo aparecer hahaha!')"); 
print("ou digite 0 para desistir('Mas não vá desistir tão cedo!')"); 
print("selecione a dificudade."); 
print("digite 1, 2 ou 3 para escolher o nivel. "); 

#input
mainmenu = int(input("Digite:"));

#números sorteados
varnumber1 = randint(1, 30); 
varnumber2 = randint(1, 60);  
varnumber3 = randint(1, 90); 

#menu do game
while (tries > 0):
    sleep(1); 
    system("cls"); 
    # nivel facil 
    if(mainmenu == 1): 
        print("Você escolheu a dificuldade bebe de mamãe('que graçinha!'),"); 
        print(f"LEMBRE-SE:{tries}.")
        setenumber = int(input("sua tentativa digite aqui:")); 
        tries = tries - 1; 
        if(tries > 0 and tries < 3 ):
            if(setenumber > varnumber1 ): 
                print("Vou aliviar para você o número esta perto! \nO número que eu pensei é menor!");
                sleep(2);

            else:   
                print("Tava vamos lá, vou te ajudar!\nO número que eu escoli é maior!"); 
                sleep(2);      
        if(setenumber == varnumber1):
            print("Olha você conseguiu, mas não tem nada de especial nisso, e tal especial quanto um grão de areia num deserto!");
            exit(); 
        else:
            print("Você errou, nada mais que o esperado.");
            sleep(2); 
    if(mainmenu == 2):
        print("Vejam só ele quer se divirtir!"); 
        print(f"LEMBRE-SE:{tries}.")
        setenumber = int(input("sua tentativa digite aqui:")); 
        tries = tries - 1; 
        if(tries > 0 and tries < 2):
            if(setenumber > varnumber2 ): 
                print("Vou aliviar para você o número esta perto! \nO número que eu pensei é menor!");
                sleep(2);
            else:   
                print("Tava vamos lá, vou te ajudar!\nO número que eu escoli é maior!"); 
                sleep(2);
        if(setenumber == varnumber2):
            print("Olha seu acerto foi tão imprecionante quanto ver um cachorro pegar a bolinha, e legal mas nada demais!"); 
            exit(); 
        else:
            print("Você errou, Vamos lá até o tolo consegiu e voce ainda não!"); 
            sleep(2); 
    if(mainmenu == 3):
        print("Meus parabéns! Agora ta querendo jogar de verdade!"); 
        print(f"LEMBRE-SE:{tries}.")
        setenumber = int(input("sua tentativa digite aqui:")); 
        tries = tries - 1; 
        if(tries > 0 and tries < 2 ):
            if(setenumber > varnumber3): 
                print("Vou aliviar para você o número esta perto! \nO número que eu pensei é menor!");
                sleep(2);
            else:   
                print("Tava vamos lá, vou te ajudar!\nO número que eu escoli é maior!"); 
                sleep(2); 
        if(setenumber == varnumber3):
            print("Olha você acertou, muito bom. tiro meu chapel para você... de lenda para lenda!"); 
            exit(); 
        else:
            print("Você errou, esse errou vou dar um desconto");
            sleep(2); 
    if(mainmenu == 0):
        exit();
print("GAME OVER!"); 
print("Mais sorte na proxima, se tiver uma hahahaha!"); 
input("aperte Enter para encerrar..."); 
