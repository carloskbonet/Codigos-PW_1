count = int(1);
soma = int(1);

print('O algoritmo calculará o Fatorial do número digitado.\n');

count = int(input("Digite: "));

# Processamento

while ( count > 1 ):

    soma = soma * count;

    print(soma);

    count = count - 1;