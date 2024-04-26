variavel_A = int(0);
variavel_B = int(0);
variavel_C = int(0);
result = int(0);

print('O algoritmo irá solicitar 3 números. Os 2 primeiros serão somados.');
print('Em seguida, será feita uma verificação para afirmar se a soma é maior ou menor que o último número digitado.');

variavel_A = int(input('Digite: '));
variavel_B = int(input('Digite: '));
variavel_C = int(input('Digite: '));

# Processamento

result = variavel_A + variavel_B;

print(f'\nA soma resultou em {result} e C vale {variavel_C}');

if ( result > variavel_C ):
    print('O valor é MAIOR que C.');

if ( result < variavel_C ):
    print('O valor é MENOR que C.');

if ( result == variavel_C ):
    print('O valor é IGUAL a C');