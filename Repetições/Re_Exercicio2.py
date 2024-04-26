
count = int(1);
value = int(0);
result = int(0);

print("O algoritmo fará a tabuada do número digitado.\n");

# Input

value = int(input("Digite um número: "));

# Processamento

while ( count <= 10 ):
    
    result = value * count;

    print (f'{value} x {count} = {result}');

    count = count + 1;
