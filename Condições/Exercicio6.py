number = float(0);
test_3 = float(0);
test_5 = float(0);

print('O algoritmo verificará se o número digitado é múltiplo de 3 e 5.\n');

number = float(input("Digite: "));

# Processamento

test_3 = number % 3;
test_5 = number % 5;

if ( test_3 == 0 and test_5 == 0 ):
    print('\nO número é múltiplo de 3 e 5.');
else:
    if ( test_3 == 0 ):
        print('\nO número é múltiplo APENAS de 3.');
        exit();

    if ( test_5 == 0 ):
        print('\nO número é múltiplo APENAS de 5.');
        exit();

    print('\nO número NÃO é múltiplo de 3 ou 5.');

