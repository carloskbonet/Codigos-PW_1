year = int(0);
result = int(0);

print("O algoritmo verificará se o ano digitado é Bissexto.\n");

year = int(input("Digite: "));

# Processamento

result = year % 4;

if ( result == 0 ):
    print("\nO ano é Bissexto");
else:
    print("\nO ano NÃO é Bissexto.");