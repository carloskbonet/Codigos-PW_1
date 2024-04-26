candidato_1 = int(0);
candidato_2 = int(0);
candidato_3 = int(0);
candidato_4 = int(0);
nulo = int(0);
branco = int(0);
num_pessoas = int(0);
inputNumber = int(0);

print('Urna Eletrônica.');
print('Digite o seu voto.');
print('1 para candidato xxxx , 2 para candidato yyyy, 3 para candidato zzzz, 4 para candidato pppp');
print('5 para Nulo, 6 para votar em Branco');

num_pessoas = int(input('Digite quantas pessoas irão votar na eleição: '));

for count in range(1 , num_pessoas + 1):
    
    while (True):
        inputNumber = int(input(f'Pessoa {count} digite seu voto: '));
    
        if ( inputNumber < 1 or inputNumber > 6 ):
            print('Digite apenas números presentes no menu.');
        else:
            break;

    if ( inputNumber == 1 ):
        candidato_1 = candidato_1 + 1;

    if ( inputNumber == 2 ):
        candidato_2 = candidato_2 + 1;

    if ( inputNumber == 3 ):
        candidato_3 = candidato_3 + 1;

    if ( inputNumber == 4 ):
        candidato_4 = candidato_4 + 1;

    if ( inputNumber == 5 ):
        nulo = nulo + 1;

    if ( inputNumber == 6 ):
        branco = branco + 1;


print(f'\nCONTAGEM DE VOTOS');
print(f'Candidato 1: {candidato_1} votos');
print(f'Candidato 2: {candidato_2} votos');
print(f'Candidato 3: {candidato_3} votos');
print(f'Candidato 4: {candidato_4} votos');
print(f'Votos Nulos: {nulo}  //  Votos em Branco: {branco}');

