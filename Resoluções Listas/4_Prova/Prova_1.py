import random;
import time;

def isBigger(numberToGuess: int, numberToGetTip: int) -> bool:
    if (numberToGetTip > numberToGuess):
        return True;
    else:
        return False;
        
    
def isLower(numberToGuess: int, numberToGetTip: int) -> bool:
    if (numberToGetTip < numberToGuess):
        return True;
    else:
        return False;

sortedNumber = 0;
numberOfTips = 5;
numberOfTries = 4;

#Variaveis usadas para verificações
inputDif = int(0);
inputSelection = int(0);
selectTip = int(0);
tipNumber = int(0);
result = bool(False);
numberTry = int(0);

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
print("O modo fácil apresenta números entre (1 e 30). \nO modo médio apresenta números entre (1 e 60). \nO modo dificil apresenta números entre (1 e 90).");

while True:
    print("Selecione a dificuldade.");
    print("Digite 1 para fácil.");
    print("Digite 2 para médio.");
    print("Digite 3 para dificil.\n");

    inputDif = int(input("Digite: "));

    if (inputDif < 1 or inputDif > 3):
        print("\nDigite apenas números presentes no menu !!!");
    else:
        sortedNumber = random.randint(1, inputDif * 30);
        break;


while True:
    print("-------------------------------------------------------------------");
    print(f'\nNúmero de tentativas restantes: {numberOfTries} / Número de dicas restantes: {numberOfTips}');
    print("Menu do Jogo. Selecione uma das opções abaixo:");
    print("Digite 1 para receber uma dica.");
    print("Digite 2 para tentar adivinhar o número.");
    print("Digite 3 para desistir da partida atual.\n");
    
    inputSelection = int(input("Digite: "));

    if (inputSelection < 1 or inputSelection > 3):
        print("\nDigite apenas números presentes no menu !!!");
    else:
        if (inputSelection == 1):
            if (numberOfTips > 0):
                selectTip = random.randint(1,2);
                numberOfTips -= 1;
                if (selectTip == 1):
                    print("\nAaaah, então você quer saber uma dica né? Bem... Se você me falar um número, \nposso te dizer se ele é MAIOR do que o número sorteado.");
                    tipNumber = int(input("Digite: "));
                    result = isBigger(sortedNumber , tipNumber);
                    if (result):
                        print("Sim... O número digitado é maior do que o número sorteado.\n");
                    else:
                        print("Haahahahaha nem na dica acerta né? O número digitado não é maior que o número sorteado.\n");
                if (selectTip == 2):
                    print("\nAaaah, então você quer saber uma dica né? Bem... Se você me falar um número, \nposso te dizer se ele é MENOR do que o número sorteado.");
                    tipNumber = int(input("Digite: "));
                    result = isLower(sortedNumber , tipNumber);
                    if (result):
                        print("Sim... O número digitado é MENOR do que o número sorteado.\n");
                    else:
                        print("Haahahahaha nem na dica acerta né? O número digitado não é MENOR que o número sorteado.\n");
            else:
                print("Ishh, você já usou todas as suas dicas !! Agora é só na sorte.");
                
        if (inputSelection == 2):
            print("Corajoso!! Vai tentar adivinhar o número então, é? Hehehe Boa sorte.");
            numberTry = int(input("Digite: "));
        
            if (numberTry == sortedNumber):
                print("\nUau, eu não estava esperando por essa!! HAHAHA você realmente acertou!!!!!!! Meus parabéns Vencedor.");
                exit();
            else:
                print("Buuuuuuh não foi dessa vez !!!");
                numberOfTries -= 1;

            if (numberOfTries < 1):
                print("Número de tentativas restantes 0. Game Over !");
                exit();
            

        if (inputSelection == 3):
            print("Uma pena !! Espero que tenha coragem para tentar novamente.");
            exit();