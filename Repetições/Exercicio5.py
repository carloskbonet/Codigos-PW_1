number_1 = int(0);
number_2 = int(1);
next_number = int(0);

print("O algoritmo abaixo calculará a sequência fibonacci.\n");

# Input

# Processamento

print(number_1);
print(number_2);

while ( next_number < 100 ):

    #print(f'{next_number} = {number_1} + {number_2}');

    next_number = number_1 + number_2;

    print(f'{next_number}');

    number_1 = number_2;
    number_2 = next_number;

