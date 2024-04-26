count = int(1);
soma = int(0);

print("O algoritmo fará a somatório dos números de 1 a 10.\n");

# Input

# Processamento

while ( count <= 10 ):

    print(f'{soma} + {count} = {soma+count}');

    soma = soma + count;

    count = count + 1;


# Output

print(f'\nA somatória final resultou em: {soma}');