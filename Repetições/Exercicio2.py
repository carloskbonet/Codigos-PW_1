counter = int(1);
value = int(0);
result = int(0);

print('O algoritmo fará a tabuada do número digitado.');

value = int(input("Digite: "));

# Processamento

while ( counter <= 10 ):
    result = value * counter;

    print(f'{value} x {counter} = {result}');

    counter = counter + 1;