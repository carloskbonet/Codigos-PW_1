#importação das bibliotecas
import random;
from os import system;


#Declaração das variáveis
sortedNumber=int(0);
opInicial=int(-1);
nivel=int(0);
count=int(0);
palpite=int(0);
dica=int(-1);

#Menu
print("JOGO DA ADVINHAÇÃO");
print("\nNeste jogo você pode escolher os niveis que quer testar sua capacidade de Chico Xavier");
print("No nível iniciante os espíritos superiores irão te auxiliar trazendo apenas 30 opções para você se iluminar.");
print("No nível intermediário os espiritos superiores eleveram a dificuldade e as opções serão de 60 números.");
print("Por fim se você acredita que já é um ser supremo, então invoque suas entidades e tente adivinhar os 90 números disponíveis.\n");


#Condição para escolher a opção correta.
while(True):
    opInicial=int(input("Aperte 1 se tem o santo forte e continue ou 0 ser já de teu um arrepio e um espirito dos povos de baixos te encarnaram, e você vai sair fazer uma oração:  "))

    if(opInicial<0 or opInicial>1):
        print("\nEspirito encarnado, tá querendo ir direto para o inferno, ou 0 para sair ou 1 para iniciar!!!")
    else:
         break;

#Seleção da dificuldade.
while(True):
    nivel=int(input("\nEscolha seu nível de evolução, Lembrando que opção 1:Fácil, opção 2: Intermediário e opção 3: Difícil. "))
    if(nivel<1 or nivel>3):
        print("\nFilho abençoado presta atenção ou 1 ou 2 ou 3!!!")
    else:
        break;

#Sorteio do número.
sortedNumber=random.randint(1, nivel*30);

system('cls');    
#Menu do jogador
print("Neste jogo temos algumas regras.");
print("Primeiro um número escolhidos, pelos seres supremos ou não, será sorteado e vc deve invocar tuas entidades para advinhar este número.");
print("Mesmo você se achando o próprio Chico Xavier e tendo contato direto com os espíritos você receberá dicas, caso precise, e vai precisar!");
print("Você tem 4 tentativas para conseguir adivinhar. Se não acertar, as portar do inferno estão abertar para você! Sem pressão hehehe!!! ");
print(F"\nAgora que você fez sua escolha sobre sua capacidade mediunica, então faça sua tentativa de adivinhação: ");

while(count<4):
    
    palpite=int(input("\nDigite seu palpite: "));
    system('cls');    
    if(palpite==sortedNumber):
        print(f"\nTo assombrado, Pode subir direto para o céu, você acertou!!! ");
        exit();
    else:
        
        while(True):
            if( dica!=0 and  dica !=1 ):
                dica=int(input("\nEstá abusando da sorte, você tem opção de algumas dicas dos seus guias, digite 1 caso queira a dica, ou 0 se você se garante."))
            if(dica>=0 or dica<=1):
                if(palpite>sortedNumber):
                    print("\nO número sorteado é menor do que seu palpite");
                if(palpite<sortedNumber):
                    print("\nO número sorteado é maior que seu palpite");
                break;  
            else:
                print("\nMisericordia desta alma, somente 1 para dicas ou 0 sem dicas");
                     
    count+=1
    if(4-count==0):
        print("\nElevador para o inferno descennnnnndoooooo, Gamer Over")
    else:
        print(f"\nVocê tentou {count} vez(es) faltam apenas {4-count} tentativa(s).")




