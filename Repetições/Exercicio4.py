count = int(1);
limit = int(0);
soma = int(1);

print('O algoritmo calculará o Fatorial do número digitado.\n');

limit = int(input("Digite: "));

# Processamento

while ( count <= limit ):

    soma = soma * count;

    print(soma);

    count = count + 1;