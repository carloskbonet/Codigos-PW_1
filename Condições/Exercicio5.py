number = float(0);
div_by = float(0);
result = float(0);

print("O algoritmo verificará se o PRIMEIRO número digitado é múltiplo do SEGUNDO número digitado.");

number = float(input("Digite o PRIMEIRO número: "));
div_by = float(input("Digite o SEGUNDO número: "));

result = number % div_by;

if ( result == 0 ):
    print(f'\nO número {number} é divisível por {div_by}');
else:
    print(f'\nNão é divisível.');