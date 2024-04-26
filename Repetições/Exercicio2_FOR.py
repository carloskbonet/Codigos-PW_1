value = int(0);
result = int(0);

print('O algoritmo fará a tabuada do número digitado.');

value = int(input("Digite: "));

# Processamento

for counter in range( 1 , 11 , 1 ):
    result = value * counter;

    print(f'{value} x {counter} = {result}');