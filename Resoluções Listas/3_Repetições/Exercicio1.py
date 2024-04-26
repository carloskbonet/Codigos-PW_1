count = int(0);
inputNumber = float(1);
sum = float(0);
media = float(0);


print('O algoritmo calculará a média dos números digitados.');

print('Digite 0 para encerrar.');

while (inputNumber > 0):
    inputNumber = float(input('Digite: '));

    if ( inputNumber > 0 ):
        sum = sum + inputNumber;
        count = count + 1;


print(f'\nA soma dos valores resultou em {sum}');
print(f'Quantidade de números digitados: {count}');

media = sum / count;

print(f'A média dos números é: {media}');