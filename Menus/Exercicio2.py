import os;
import random;

# Variáveis
tries = int(0);
inputMenu = int(0);
sortedNumber = int(0);
inputNumber = int(0);

# Explicação
print("Esse é o jogo da adivinhação !! Digite o número de tentativas que desejar.");
print("O jogo irá gerar um número entre (1 e 100).");


# Inputs
tries = int(input("Digite: "));


# Processamento

sortedNumber = random.randint(1 , 100);

while (tries >= 0):
    print("\nMenu do Jogo!! Selecione uma das opções abaixo.");
    print(f"Digite 1 para tentar adivinhar o número (Você tem {tries} tentativas restantes).");
    print("Digite 0 para DESISTIR do jogo.");
    inputMenu = int(input("Digite: "));

    if ( inputMenu < 0 or inputMenu > 1 ):
        print("\nDigite apenas números presentes no Menu.");
    else:
        if ( inputMenu == 1 ):
            print("\nVejo que tem coragem !! Vai tentar acertar o número que escolhi? Boa sorte.");
            inputNumber = int(input("Digite: "));

            tries = tries - 1;

            if ( inputNumber == sortedNumber ):
                print("O que???? Você acertou? Não esperava por essa... Bem, ao menos posso te parabenizar. Parabéns !!");
                break;
            else:
                print("Nada fora do comum hahaha Você ERROU\n");

                print("Você precisa melhorar muito para conseguir ser apenas ruim... vou precisar te dar uma dica: ");
                if ( sortedNumber > inputNumber ):
                    print("O número que escolhi é maior");
                else:
                    print("O número que escolhi é menor.");
                    
        
        if ( inputMenu == 0 ):
            print("\nDesistiu tão cedo? Uma pena, esperava muito mais de você... Volte Logo (Ou não =/)");
            exit();
    
    if( tries < 1 ):
        print("\nGAME OVER");
        print(f"O número era: {sortedNumber}");
        exit();

    input('\nDigite ENTER para continuar.');
    os.system('cls');