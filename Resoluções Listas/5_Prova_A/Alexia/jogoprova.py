import os;
import random;

#

inputMenu = int(0);
select_number = int(0);
chute = int(0);
tentativas = int(4);
dicas = int(5);

# 

print('================================================================================');
print('Este  é um jogo de adivinhação.!!');
print('Para jogar, temos algumas regras.');
print('Primeiro: Um número aleatório será gerado a partir da dificuldade selecionada.');
print('Segundo: O jogador recebrá até 5 dicas em cada partida.');
print('Terceiro: O jogador terá 4 tentivas de adivinhar o número.');

input('\nDigite ENTER para continuar.');
os.system('cls');

while (select_number < 1 or select_number > 3):
    print('\nAgora vamos para a seleção de dificuldade!');
    print('MODO FÁCIL: apresenta números entre (1 e 30);');
    print('MODO MÉDIO: apresenta números entre (1 e 60);');
    print('MODO DIFICIL: apresenta números entre (1 e 90);');
    print('Selecione a dificuldade que deseja:');
    print('Digite 1 para FÁCIL.');
    print('Digite 2 para MÉDIO.');
    print('Digite 3 para DIFICIL.');
    select_number = int(input('Digite sua opção: '));
        
    if (select_number == 1 or select_number == 2 or select_number ==3):
        break;



#


numero_secreto = random.randint(1, select_number * 30);


while (tentativas >=0):
    print(f'\nNúmero de tentativas restantes : {tentativas} / Número de dicas restantes : {dicas}.');
    print('================ MENU DO JOGO ================');
    print('Selecione uma das opções abaixo:');
    print('Digite 1 para receber uma dica.');
    print('Digite 2 para tentar adivinhar o número.');
    print('Digite 3 para desistir da partida atual.');
    inputMenu = int(input('Digite sua opção: '));
    
    if (inputMenu == 1 and dicas != 0):
        print('Huummm....\n Quer uma dica ? Mais já ? Me diz o número que está pensando :');
        chute = int(input('Digite seu palpite: '));
        if (chute < numero_secreto):
            print('Talvez um numero maior...');
            dicas = dicas -1;
        if (chute > numero_secreto):
            print('Talvez um numero menor...');
            dicas = dicas -1;
        if (chute == numero_secreto):
            print('Não conta pra ninguém, mas, eu acho que você acertou hihihihi :D');
            dicas = dicas -1;
        if (dicas == 0):
            print('Iiiih .... Já era, não tem dicas.');
                        
            
    if (inputMenu == 2):
        print('BOOOOAAAA gosto dos corajosos !!')
        chute = int(input('Diz ai, qual o número:'));
        if (chute == numero_secreto):
            print('Você acertou, parabéns !!!');
        if (chute != numero_secreto):
            print('Não foi dessa vez, mais sorte na próxima...');
            tentativas = tentativas -1;
                    
            
    if (inputMenu == 3):
        print('DESISTIR NÃO DEVERIA SER UMA OPÇÃO U.U');
        print('Encerrando.....');
        exit();
                
    if( tentativas == 0):
        print('GAME OVER');
        exit();