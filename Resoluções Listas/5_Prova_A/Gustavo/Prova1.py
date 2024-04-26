import os;
import random;

tries = int(4);
sortedNumber = int(0);
inputMenu = int(0);
selectedNumber = int(0);
number = int(0);
helps = int(5);

print("Esse é o jogo da advinhação !! Vamos ver se você consegue advinhar o número que eu escolhi !! As chances são 1% !! HAHAHAHAHAHAHA !!.");
print("Esses são as minhas regras,e vai tem que seguir para jogar,SE NÃO,cai fora seu mané.");
print("PRIMEIRO:Um número será gerado dependendo da dificuldade que escolher.");
print("SEGUNDO:Você pode receber até 5 dicas,por que não tenta advinhar de primeira seu fracote.");
print("TERCEIRO:Você terá 4 tentativas de advinhar o número que eu escolhi,SE NÃO já era");

print("BOOOORRRRAAAAA,HORA DO SHOW. . .");

print("Primeiro selecione as dificuldades! ");
print("O modo fácil é para iniciantes,apresenta números entre (1 e 30).");
print("O modo médio é para moderados,apresenta números entre (1 e 60).");
print("O modo difícil é para experientes,apresenta números entre (1 e 90).");

print("Selecione a dificuldade.");
print("Digite 1 para fácil.");
print("Digite 2 para médio.");
print("Digite 3 para difícil.");

selectedNumber = int(input("Digite:"));

if(selectedNumber == 1):
    sortedNumber = random.randint(1 , 30);
if(selectedNumber == 2):
    sortedNumber = random.randint(1 , 60);
if(selectedNumber == 3):
    selectedNumber = random.randint(1 , 90);
 

while(tries > 0):
    os.system('cls');
    print("\nMenu do jogo !! Selecione as opçcões abaixo se quiser continuar.");
    print(f"Digite 1 para receber dicas (Você tem {helps} restantes).");
    print(f"Digite 2 para advinhar o número (Você tem {tries} restantes). ");
    print(f"Digite 3 para desistir da partida atual. ");
    inputMenu = int(input("Digite: "));

    if(inputMenu < 0 or inputMenu > 3):
        print("\nDigite apenas números presentes no menu.");
    else:
        if(inputMenu == 1):
            print("Não consegue de sem ajuda né,HAHAHAHA,se me dizer um número posso te ajudar,se ele é MAIOR ou MENOR do que eu escolhi. ");
            number = int(input("Digite:"));
            if(number > sortedNumber): 
                print("\nO número que eu escolhi é menor");
            if(number < sortedNumber):
                print("\nO número que eu escolhi é maior");
        
            helps = helps - 1;
            
        if(inputMenu == 2):
            print("Vamos ver se você é inteligente o suficiente para advinhar o número que eu escolhi. ");

            number = int(input("Digite:"));

            if(number == sortedNumber):
                print("\nNão esperava isso de você,Mas parabéns,Você acertou,Calou a minha boca !!!.");

            else:
                print("\nNão consegue né,HAHAHAHAHA,tente de novo. ");
        
            tries = tries - 1;

        if(inputMenu == 3):
            print("Mas já desistiu,tão cedo,eu sabia que você não ia conseguir,HAHAHAHAHAHA,volte nunca mais.");
            break;

    if(tries < 1):
        print("\nGAME OVER,Seu fracote,Você não serve para jogar esse jogo.");
        print(f"O número era {sortedNumber}");
        exit();

    input('Digite ENTER para continuar.');


                


    
    