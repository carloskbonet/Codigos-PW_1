number_1 = int(0);
number_2 = int(1);
next_number = int(0);
limit = int(0);

print("O algoritmo abaixo calculará a sequência fibonacci.\n");

# Input
limit = int(input("Digite a quantidade de números a serem gerados: "));

# Processamento

print(number_1);
print(number_2);

limit = limit - 2;

for count in range(0 , limit , 1):

    next_number = number_1 + number_2;
    print(f'{next_number}');

    number_1 = number_2;
    number_2 = next_number;