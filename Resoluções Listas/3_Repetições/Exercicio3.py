menor = float(0);
maior = float(0);
inputNumber = float(0);

print('O algoritmo solicitará que digite alturas. Ao final, serão exibidas a menor e maior respectivamente.');

for count in range(1 , 11 , 1):
    inputNumber = float(input(f'Altura da pessoa {count}: '));

    if ( menor == 0 and maior == 0 ):
        menor = inputNumber;
        maior = inputNumber;

    if ( inputNumber < menor ):
        menor = inputNumber;

    if ( inputNumber > maior ):
        maior = inputNumber;

    print(f'Menor: {menor}  //  Maior: {maior}\n')
